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
    task.set_fun(period_run, pool, name)
    task.run()

def period_run(pool, name):
    _collection(pool, name)
    pool.waitall()

def _collection(pool, name):
    tasks = get_task()
    for task in tasks:
        pool.spawn_n(hello, name)

def get_task():
    return [1,2,3,4]

def hello(name):
    LOG.info("get the data, i am %s thread!!!"%name)


if __name__ == "__main__":
    collection()

