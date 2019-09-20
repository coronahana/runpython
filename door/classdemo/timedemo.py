import time

import random
def timesign():
    #1541054165487
    current_milli_time = int(round(time.time() * 1000))
    print(current_milli_time)
def timeyyymmdd():

    """



    hsm01 = time.strftime ('%Y%m%d%H%M%S', time.localtime (time.time ()))  #20181018161602

    yyyy=random.randint(2015,2018)
    mm=random.randint(10,12)
    dd=random.randint(10,29)

    ymd=str(yyyy)+str(mm)+str(dd)
    print(ymd)
    hsm02 = time.strftime ('%H%M%S', time.localtime (time.time ()))
    """
    yyyy = random.randint (2015, 2018)
    mm = random.randint (10, 12)
    dd = random.randint (10, 29)
    ymdhms=str(yyyy)+str(mm)+str(dd)+time.strftime ('%H%M%S', time.localtime (time.time ()))
    print(ymdhms)

#timesign()
#timeyyymmdd()
def timedd():
    print(time.time())
    print(time.localtime(time.time ()))
    nowtime=time.strftime('%Y%m%d%H:%M:%S',time.localtime (time.time ()))
    print(nowtime)
    #暂停一秒
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime (time.time ())))
    print(nowtime)
#时间戳
def Get_A_Timesign():
    #1541054165487
    current_milli_time = int(round(time.time() * 1000))
    print(current_milli_time)
    return  current_milli_time
print(Get_A_Timesign())


nowtime=time.strftime('%Y%m%d%H%M%S',time.localtime (time.time ()))
print(nowtime)
time.sleep(2)
nowtime=time.strftime('%Y%m%d%H%M%S',time.localtime (time.time ()))
print(nowtime)
time.sl

