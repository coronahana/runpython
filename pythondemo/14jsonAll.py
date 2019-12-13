#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import sys
import time
import os
import sys
import re


class Demo:
    # 一个类变量，它的值将在这个类的所有实例之间共享
    age = 28
    empCount = 9

    def __init__(self, name, salary):
        # __init__()方法类的构造函数或初始化方法
        # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        print ("I am init")
        self.name = name
        self.salary = salary
        Demo.empCount += 1

    def displayCount(self):
        print
        "Total Employee %d" % Demo.empCount

    def displayEmployee(self):
        print
        "Name : ", self.name, ", Salary: ", self.salary

    def demotime(self):
        # 时间
        ticks = time.time ()
        # print("当前时间戳为:", ticks)
        return ticks;
        import calendar

        # cal = calendar.month(2016, 1)
        # print("以下输出2016年1月份的日历:")
        # print(cal)
    def jsondata(self):
        obj = """ 
                [{"aqi":46,"area":"成都","pm2_5":32,"pm2_5_24h":33,"position_name":"金泉两河","primary_pollutant":null,"quality":"优","station_code":"1431A","time_point":"2018-09-05T09:00:00Z"},
                {"aqi":29,"area":"成都","pm2_5":20,"pm2_5_24h":26,"position_name":"十里店","primary_pollutant":null,"quality":"优","station_code":"1432A","time_point":"2018-09-05T09:00:00Z"},
                {"aqi":30,"area":"北京","pm2_5":20,"pm2_5_24h":26,"position_name":"海淀","primary_pollutant":null,"quality":"优","station_code":"1432A","time_point":"2018-09-05T09:00:00Z"}]
              """
        #<class 'str'>
        print (type (obj))
        #str类型转化成python object
        jsondata=json.loads(obj)
        #< class 'list'>
        print(type(jsondata))
        print(jsondata)
        #python object 转换成str类型
        kk=json.dumps(jsondata)
        print (type(kk))
        print (kk)



    def demoNumber(self):
        # Number(数字)
        var2 = 10
        v3 = -21.9
        print ("v3=" + str (v3) + " is " + str (type (v3)))
        v4 = 9.322e-36j
        print ("v4=" + str (v4) + " is " + str (type (v4)))
        print ("var2=" + str (var2) + " is " + str (type (var2)))
        islike = True
        print ("islike=" + str (islike) + " is " + str (type (islike)))
        data01 = None
        print ("data01=" + str (data01) + " is " + str (type (data01)))

        dic = {"ggg": "ddd", "dsf": 45}
        print ("dic=" + str (dic) + " is " + str (type (dic)))
        ardata = ["ggg", "ddd", {"ggg": "ddd", "dsf": 45}, True]
        print ("ardata=" + str (ardata) + " is " + str (type (ardata)))

    def demoifelse(self):
        flag = False
        name = "python"
        if (name == "python"):
            print ("you  like python")
        else:
            print ("you do not like python")

        age = 85;
        if (age == 21):
            print ("you are young!")
        elif (age > 22):
            print ("you are middle")
        elif (age > 26 and age < 80):
            print (" you are old")
        elif (age >= 80):
            print ("you are really old")
        url = ""
        if not url:
            raise RuntimeError ("no url been set")

    def demoWhile(self):
        a = 1
        while (a < 10):
            print ("a= " + str (a))
            a = a + 1
            if (a == 8):
                break

    def demoString(self):
        # String
        str = 'Hello World!'

        print (str)  # 输出完整字符串
        print (str[0])  # 输出字符串中的第一个字符
        print (str[2:5])  # 输出字符串中第三个至第五个之间的字符串
        print (str[2:])  # 输出从第三个字符开始的字符串
        print (str * 2)  # 输出字符串两次
        print (str + "TEST")  # 输出连接的字符串

    def demoList(self):
        # List（列表苦力）
        list = ['runoob01', 78602, 2.2303, 'john04', 70.205]
        print(list)  # 输出完整列表
        print(list[0])  # 输出列表的第一个元素
        for lll in list:
            print(lll)  # 输出列表的每一个个元素

    def demoTuple(self):
        # Tuple（元组-不能修改）Python的元组与列表类似，不同之处在于元组的元素不能修改。
        tup1 = ('physics', 'chemistry', 1997, 2000)
        tup2 = (1, 2, 3, 4, 5, 6, 7)
        print ("tup1[0]: ", tup1[0])
        print ("tup2[1:5]: ", tup2[1:5])

    def demoDictionary(self):
        # Dictionary（字典)
        # 首先定义一个空字典dict={}

        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
        print ("dict['Alice']: ", dict['Name']);
        del dict['Name'];  # 删除键是'Name'的条目
        dict.clear ();  # 清空词典所有条目
        del dict;  # 删除词典
        dic = {}
        dic.setdefault ('sex', 'male')
        dic.setdefault ('name', 'lili')
        datadic = {"id": 16240,
                   "fakeId": "S016240",
                   "name": "sdfsdf",
                   "userId": "1",
                   "projectId": 10364,
                   "canvasData": "",
                   "dispatchData": "{\"periodSelect\":\"\",\"dispattime\":\"\",\"periodCount\":\"\",\"parallelParams\":\"{\\\"REDO_DRIVE\\\":1,\\\"QUARTZ_DRIVE\\\":1,\\\"PARAM_DRIVE\\\":1}\",\"policy\":\"parallel\"}",
                   "timerFlow": False,
                   "jobGenerated": False,
                   "gmtCreate": "2018-08-03",
                   "gmtModified": "2018-08-03",
                   "nodes": None,
                   "edges": None,
                   "alarmParams": None,
                   "globalParams": None,
                   "lastQuartzTime": None,
                   "raceFlow": 0,
                   "flowRank": 0}
        dic.setdefault ('data', datadic)

        print (dic)

    def demoJSON(self):

        print (sys.argv)
        data01 = [{'uuu': 1, 'bbb': 2, 'ccc': 3, 'ddd': 4, 'eee': 5}]
        json01 = json.dumps (data01)
        print (json01)
        dic02 = {}

        tt = True;
        # 字典
        dic01 = {"success": True, "data": json.dumps (data01)}
        res01 = json.dumps (dic01)
        print (res01)
        """
    
        {
            "success": True,
            "data": {
                "id": 16240,
                "fakeId": "S016240",
                "name": "sdfsdf",
                "userId": "1",
                "projectId": 10364,
                "canvasData": "",
                "dispatchData": "{\"periodSelect\":\"\",\"dispattime\":\"\",\"periodCount\":\"\",\"parallelParams\":\"{\\\"REDO_DRIVE\\\":1,\\\"QUARTZ_DRIVE\\\":1,\\\"PARAM_DRIVE\\\":1}\",\"policy\":\"parallel\"}",
                "timerFlow": false,
                "jobGenerated": false,
                "gmtCreate": "2018-08-03",
                "gmtModified": "2018-08-03",
                "nodes": null,
                "edges": null,
                "alarmParams": null,
                "globalParams": null,
                "lastQuartzTime": null,
                "raceFlow": 0,
                "flowRank": 0
            }
        }
        """
    def demofile(self, writetime):
        # str = input("请输入：")
        # print("你输入的内容是: ", str)
        dirname = "hanafile"
        filename = "hh.txt"
        if (os.path.exists (dirname) == False):
            print ("文件夹不存在,马上创建")
            os.mkdir (dirname)

        fo = open (dirname + "/" + filename, "a+")
        fo.write (str (writetime) + ":www.runoob.com!\n")
        print ("文件名: ", fo.name)
        print ("是否已关闭 : ", fo.closed)
        print ("访问模式 : ", fo.mode)
        # 好习惯
        if fo.closed == False:
            fo.close ()
        fo02 = ''
        try:
            fo02 = open (dirname + "/" + filename, "r", encoding='utf-8')
            strRead = fo02.read (2)
            print ("读取文件内容" + strRead)
        except Exception:
            print ("什么异常")
        finally:
            print ('>>>>>>finally')
            if fo02.closed == False:
                print ("关闭文件", )
                fo02.close ()

        with open (dirname + "/" + filename) as f:
            for line1 in f:
                name = "119"
                if "119" in line1:  # 包含
                    print ("这行，找到" + line1)  # 每行末尾会有一个换行符
                else:
                    print ("这行 not fonud 119")  # 每行末尾会有一个换行符
            print ('------------')

    def demoexception(self, num):
        try:
            renum = int (num)
        except ValueError:
            print ("异常：it is  not a number")
        else:
            # 如果没有异常发生
            print ("没有异常" + "this is a number inputs")
            return renum
        finally:
            print ("总要执行")

    def gggg(self):
        proresp_data = {
            "data": "{\"id\":1248,\"status\":\"success\",\"path\":\"manager?project=proname1903\",\"action\":\"redirect\"}",
            "success": "true"}

        # print(json.dumps(proresp_data))

        print (str (proresp_data))
        # strmm = str(proresp_data).replace("\"{\\", "ppp")
        # str(strmm).replace ("\"}", "}")
        print (proresp_data)

    def kkk(self):
        pppp = {"data": {"id":1248,"status":"success","path":"manager?project=proname1903","action":"redirect"},
                'success': True}
        res01 = json.dumps (pppp)
        dd= json.loads(res01)
        kk= dd["data"]["status"]
        print(kk)

    def getExecutionJobIdForModel(self):
        resp02222 = {
           "success" : True,
          "data" : {
        "modelFlowId" : 3945,
        "executionFlowId" : 220894,
        "nodeStatus" :   {
          "nodeId" : 12232,
          "uuid" : "b3fb17ce-b7e1-4ea7-a133-63df16481745",
          "status" : "finished",
          "jobId" : 10071,
          "executionJobId" : 333431,
          "resultFiles" : None
        } }}


        executionJobId = 0
        res01 = json.dumps (resp02222)
        rjs = json.loads(res01)
        print(rjs)
        #rjs = json.dumps(resp02)
        listdata = rjs["data"]["nodeStatus"]
        for nodeone in listdata:
            print ("uuid:" + nodeone["uuid"])
            if (nodeone["uuid"].endswith('model')==False):
                executionJobId = nodeone["executionJobId"]
        return int(executionJobId)

    def getprojectid_re(self):
        proresp_data = {"data": "{\"id\":12685,\"status\":\"success\",\"path\":\"manager?project=proname1903\",\"action\":\"redirect\"}","success": "true"}
        id = 0;
        p = re.compile (':\d+')
        dd = p.findall (json.dumps (proresp_data))
        # print(dd.__len__())
        if (dd.__len__ () == 1):
            mm = re.compile ('\d+').findall (dd[0])
            id = mm[0]
            print (id)
        return id

if __name__ == '__main__':
    d = Demo ("ddd", 23)
    #d.getExecutionJobIdForModel()
    #d.kkk()
    #d.getprojectid_re()
    # d.demofile(d.demotime())
    # d.demoWhile()
    # d.demotime()
    # d.demoNumber()
    # d.demoifelse()
    # d.demoexception("sdsd")
    # d.demoexception(25)
    # print(d.demoexception("8765"))
    # d.demoDictionary()
    #d.gggg ()

    # json  = d.demoJSONnewflow()
    # print(json)
    d.jsondata()