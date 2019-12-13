
import  json
"""
1、json.dumps : dict转成str
2、json.dump是将python数据保存成json
3、json.load是将文件中的json数据读取出来
"""


truedata= True
falsedata=False
nulldata=None

gg={
  "success" : truedata,
  "data" : [ {
    "departmentName" : "null",
    "roles" : nulldata,
    "groups" : nulldata,
    "referee" : "false",
    "userId" : "yuanbopeng",
    "super" : "true",
    "permissions" : "ADMIN",
    "deptmentId" : "0",
    "loginName" : "yuanbopeng",
    "chineseName" : "彭远波",
    "expireDate" : nulldata,
    "VIP" : "false",
    "issueDate" : nulldata,
    "class" : "class azkaban.user.User",
    "email" : nulldata
  } ,{
    "departmentName" : "null",
    "roles" : nulldata,
    "groups" : nulldata,
    "referee" : "false",
    "userId" : "yuanbopeng02",
    "super" : "true",
    "permissions" : "ADMIN",
    "deptmentId" : "0",
    "loginName" : "yuanbopeng02",
    "chineseName" : "彭远波02",
    "expireDate" : nulldata,
    "VIP" : "false",
    "issueDate" : nulldata,
    "class" : "class azkaban.user.User",
    "email" : nulldata
  }]
}

list02 = gg["data"]
name = ""
list03=[]
if(list02==[]):
    print ("查无此人")
    #return  "查无此人"
    for lll in list02:
        print ("userId:"+lll["userId"])  # 输出列表的每一个个元素
        if(lll["userId"])=="yuanbopeng":
            name = lll["chineseName"]
            print("chineseName:"+name)
            #return  name


ggg={u'alarmParams': None, u'gmtModified': u'2019-01-14', u'name': u'python20190114155040', u'flowRank': 0, u'projectId': 1558, u'globalParams': None, u'userId': u'p_zhhuasun', u'timerFlow': False, u'edges': None, u'fakeId': u'S005181', u'nodes': None, u'jobGenerated': False, u'canvasData': u'', u'gmtCreate': u'2019-01-14', u'lastQuartzTime': None, u'dispatchData': u'{"periodSelect":"","dispattime":"","periodCount":"","parallelParams":"{\\"REDO_DRIVE\\":1,\\"QUARTZ_DRIVE\\":1,\\"PARAM_DRIVE\\":1}","policy":"parallel"}', u'id': 5181, u'raceFlow': 0}
dddd=  json.dumps(ggg)
print(dddd)
print(type(dddd))
oo= json.loads(dddd)
print(type(oo))
print(oo["gmtModified"])
