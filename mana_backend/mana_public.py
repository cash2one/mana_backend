#!/usr/bin/env python
#coding: utf-8

import Queue 
import time

import mana_log
LOG = mana_log.GetLog(__name__)

DATA_QUEUE = Queue.Queue()
ALARM_QUEUE = Queue.Queue()


class msg_item:
    def __init__(self, alarm_obj = None, instance_id = None, instance_name = None,\
                 project = None, user = None, device_name = None, max_data = None, \
                 unit = None, region = None, contacts = None):
        self.alarm_obj = alarm_obj
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.project = project
        self.user = user
        self.device_name = device_name
        self.max_data = max_data
        self.unit = unit
        self.region = region
        self.contacts = contacts

class data_item:
    def __init__(self, instance = None, alarm_obj = None, threshold = None, region = None, data = None, contacts = None):
        self.instance = instance
        self.alarm_obj = alarm_obj
        self.threshold = threshold
        self.region = region
        self.data = data
        self.contacts = contacts


class period_task:
    def __init__(self, name = None, interval = None):
        self.name = name
        self.interval = interval

    def set_fun(self, fun, *args):
        self.fun = fun
        self.args = args

    def run(self):
        while True:
            try:
                time_pre = time.time()
                self.fun(*self.args)
                time_now = time.time()
                monitor_time = time_now - time_pre
                if monitor_time < self.interval:
                    LOG.info("Thread:--%s-- work use time = %ss" %(self.name, monitor_time))
                    time.sleep(self.interval + time_pre - time_now)
                else:
                    pass
                    LOG.warn("Thread:--%s-- work use too long time = %ss" %(self.name, monitor_time))
            except Exception, e:
                LOG.error(e)
