#!/usr/bin/env python
#coding: utf-8

import simplejson
import eventlet

from mana_http import HttpCon
import mana_log
LOG = mana_log.GetLog(__name__)

import  mana_conf
CONF = mana_conf.GetConf()

from mana_public import DATA_QUEUE
from mana_public import data_item
from mana_public import period_task

def collection(name, interval):
    pool = eventlet.GreenPool()
    LOG.info("Begin collection_%s thread,cycletime is %ss" %(name, interval))
    task  = period_task(name, interval)
    task.set_fun(period_run, pool, name, interval)
    task.run()

def period_run(pool, name, interval):
    _collection(pool, name, interval)
    pool.waitall()

def _collection(pool, name, interval):
    regions = CONF.get('regions')
    for region in regions:
        tasks = get_task(region, interval)
        for task in tasks:
            pool.spawn_n(_collection_datas, task, interval)

def get_task(region, interval):
    url = CONF.get('url').get('get_task_url') %(region,interval)
    api_host = CONF.get('api_host')
    api_port = CONF.get('api_port')
    try:
        httpclient = HttpCon(api_host, api_port, url, "GET")
        body = httpclient.get()
        if body:
            tasks = simplejson.loads(body).get('data')
    except Exception, e:
        LOG.error(e)
        return None
    return tasks 

def _collection_datas(task, interval):
    try:
        instance = task.get('instance')
        region = task.get('region')
        alarm_obj = task.get('alarm_obj')
        threshold = float(task.get('threshold'))
        sms_receiver = task.get('contacts').get('sms')
        email_receiver = task.get('contacts').get('email')
        contacts = {"email_receiver":email_receiver, "phone_receiver":sms_receiver}
        instance_id = instance.get('instance_id')
        data = get_datas_from_api(region, instance_id, alarm_obj, interval)
        item = data_item(instance, alarm_obj , threshold, region, data, contacts)
        DATA_QUEUE.put(item)
        LOG.info("item = %s,%s,%s,%s,%s,%s,%s"%(instance,region,alarm_obj,threshold,contacts,instance_id,data))
    except Exception, e:
        LOG.error(e) 

def get_datas_from_api(region, instance_id, alarm_obj, time):
    url = CONF.get('url').get('get_metric_url') %(region, alarm_obj, instance_id, time)
    api_host = CONF.get('api_host')
    api_port = CONF.get('api_port')
    try:
        httpclient = HttpCon(api_host, api_port, url, "POST")
        body = httpclient.get()
        if body:
            data = simplejson.loads(body)
    except Exception, e:
        LOG.error(e)
        return None
    return data

if __name__ == "__main__":
    collection('min', 300)
