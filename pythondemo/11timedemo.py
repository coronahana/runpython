#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import random

def time_YmdHMS():
    #2019-09-23 18:34:48
    print(time.time())
    print(time.localtime(time.time ()))
    nowtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime (time.time ()))
    print(nowtime)
    #暂停一秒
    time.sleep(2)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime (time.time ())))
    print(nowtime)

def Get_A_Timesign():
    # 时间戳(13位)1541054165487
    current_milli_time = int(round(time.time() * 1000))
    print(current_milli_time)
    return  current_milli_time

Get_A_Timesign()
time_YmdHMS()