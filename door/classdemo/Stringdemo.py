

def demoString():
    # String
    str = 'Hello World!'
    print (str)  # 输出完整字符串
    print (str[0])  # 输出字符串中的第一个字符
    print (str[2:5])  # 输出字符串中第三个至第五个之间的字符串
    print (str[2:])  # 输出从第三个字符开始的字符串
    print (str * 2)  # 输出字符串两次
    print (str + "TEST")  # 输出连接的字符串

def hhh(strS,contstr):
    #s = "This be a string"
    if strS.find (contstr) == -1:
        print ("Found " + contstr + " not in " + strS)
        print(strS.find (contstr) )
        return False
    else:
        print("Found "+contstr+" in "+strS)
        print (strS.find (contstr))
        return True

def strop():
    str= "eb22fc18-0c83-48aa-a836-daae53b8ad89_model"
    print (str[0:-6])  # 截取从头开始到倒数第6个字符之前
    print(str[0:3])  # 截取第一位到第三位的字符
    print(str[:])  # 截取字符串的全部字符
    print(str[6:]  )# 截取第七个字符到结尾
    print(str[:-3]  )# 截取从头开始到倒数第三个字符之前
    print(str[2]  )# 截取第三个字符
    print(str[-1])  # 截取倒数第一个字符
    print(str[::-1] ) # 创造一个与原字符串顺序相反的字符串
    print(str[-3:-1])  # 截取倒数第三位与倒数第一位之前的字符
    print(str[-3:] ) # 截取倒数第三位到结尾
    print(str[:-5:-3])  # 逆序截取，具体啥意思没搞明白？
strop()
hhh("I like reading","like")

projectId=555
moduleId=444
modelFlowId=333
resourcename=222
fileup_data = {'projectId': (None, int (projectId)), 'moduleId': (None, int (moduleId)),
               'modelFlowId': (None, int (modelFlowId)), 'flag': (None, 1),
                }
# 'modelflow_resource_file': (resourcename, open ( '/data/home/nfs/autotest/data_file/65/136/2399/flow_module/d_spark/tdw-spark-examples-1.0.1.jar', 'rb'),  'application/octet-stream')}
print(fileup_data)


