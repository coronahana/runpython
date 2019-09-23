
print("----------------------------------------------------------------------------------------")
bb=["北京","上海","广州","深圳","长春"]
print(type(bb))
print("list----------------------------------------------------------------------------------------")
list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
list.append('Runoob')
print(list)

print("tuple----------------------------------------------------------------------------------------")
tup001 = ('physics', 'chemistry', 1997, 2000)
print(type(tup001))

print("dict(json数据应用较多)----------------------------------------------------------------------------")
def demoDictionary():
    # Dictionary（字典)
    # 首先定义一个空字典dict={}

    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    dict02 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print (type (dict))
    print (str(dict))
    projectid = ""
    for str01 in dict:
        if(dict[str01]=="Zara"):
            projectid = str01
    print(projectid)
demoDictionary()

print("Number----------------------------------------------------------------------------")
print()
x=22.88
print(int(x))      #将x转换为一个整数
print(float(x))               #将x转换到一个浮点数
print(complex(x)) #创建一个复数
print(str(x))               #将对象 x 转换为字符串

print("----------------------------------------------------------------------------")