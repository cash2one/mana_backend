#!/usr/bin/env python
#coding: utf-8

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

import threading
import time

from mana_admin_collection import admin_collection
from mana_monitor import monitor
from mana_alarm import alarm
from mana_collection import collection

def start_AdminCollection_thread():
    Admin_Collection = threading.Thread(target = admin_collection, name = "AdminCollection")
    Admin_Collection.setDaemon(True)
    Admin_Collection.start()

def start_Monitor_thread():
    Monitor = threading.Thread(target = monitor, name = "Monitor")
    Monitor.setDaemon(True)
    Monitor.start()

def start_Alarm_thread():
    Alarm = threading.Thread(target = alarm,  name = "Alarm") 
    Alarm.setDaemon(True)
    Alarm.start()

def start_Collection_threads():
    #Collection_min = threading.Thread(target = collection, name = "min", args = ("min", 60))
    Collection_five_mins = threading.Thread(target = collection, name = "five_mins", args = ("five_mins", 300))
    #Collection_quarter_hour = threading.Thread(target = collection, name = "quarter_hour", args = ("quarter_hour", 10))
    #Collection_half_hour = threading.Thread(target = collection, name = "half_hour", args = ("half_hour", 15))
    #Collection_hour = threading.Thread(target = collection, name = "hour", args = ("hour", 20))

    #Collection_min.setDaemon(True)
    Collection_five_mins.setDaemon(True)
    #Collection_quarter_hour.setDaemon(True)
    #Collection_half_hour.setDaemon(True)
    #Collection_hour.setDaemon(True)

    #Collection_min.start()
    Collection_five_mins.start()
    #Collection_quarter_hour.start()
    #Collection_half_hour.start()
    #Collection_hour.start()

def start():
    start_AdminCollection_thread()
    start_Monitor_thread()
    start_Alarm_thread()
    #start_Collection_threads()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    start()
