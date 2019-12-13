# -*- coding: UTF-8 -*-
import random
import time
def timeyyymmddhms():
    yyyy = random.randint (2015, 2018)
    mm = random.randint (10, 12)
    dd = random.randint (10, 29)
    ymdhms=str(yyyy)+str(mm)+str(dd)+time.strftime ('%H%M%S', time.localtime (time.time ()))
    #print(ymdhms)
    return  ymdhms

def datas(splitstr,datatotal ):
    #组装一条数据
    #id,消费金额，时间
    #20002,21,20171115223855
    id = random.randint (100001,100001+int(datatotal))
    money=random.randint (10,99)
    ymdhms =timeyyymmddhms()
    dataone=str(id)+splitstr+str(money)+splitstr+str(ymdhms)+"\n"
    return  dataone

def makedata(splitstr,datatotal,filename):
    #打开文件
    #filename ="test.txt"
    fo = open (filename, "w", encoding="UTF-8")
    print ("文件名为: ", fo.name)

    counter=1
    for counter in range(1,datatotal) :
        print (counter)
        dataone = datas (splitstr, datatotal)
        print (dataone)
        fo.write (dataone)
    # 关闭文件
    fo.close ()

makedata("|",100000,"threedata")