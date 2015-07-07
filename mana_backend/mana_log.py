#!/usr/bin/env python
#coding: utf-8

import logging 
import os

"""
LOG_FILE = 'monitor.log'
#LOG_FILE = '/var/log/mana/monitor.logepa '
#logging.basicConfig(filename = os.path.join(os.getcwd(), LOG_FILE), 
logging.basicConfig(filename = LOG_FILE,
                    level = logging.DEBUG, 
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', 
                    datefmt= '%m-%d %H:%M') 

console = logging.StreamHandler()  
console.setLevel(logging.INFO) 
logging.getLogger('').addHandler(console)  
"""
def SetLog(logname):
    LOG_FILE = '/var/log/mana/'  + logname + '.log'
    #LOG_FILE = logname
    logging.basicConfig(filename = LOG_FILE,
                        level = logging.DEBUG, 
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', 
                        datefmt= '%m-%d %H:%M') 

    console = logging.StreamHandler()  
    console.setLevel(logging.INFO) 
    logging.getLogger('').addHandler(console)  



def GetLog(logname, name):
    SetLog(logname)
    log = logging.getLogger(name)
    return log 


if __name__ == "__main__":
    log  =  GetLog('alarm',__name__)
    log.info("hello world!")
    log.debug("hello python!")
    log.warn("warn!!!!")
    log.error("error!!") 


