def copylist():
    a = [1, 2, 3]
    b = a[:]
    #b = a
    print(b)

copylist()

def demoList():
    # List（列表苦力）

    list02 = ['runoob01', 78602, 2.2303, 'john04', 'happy','happy','happy',70.205,{"name":"v_hhh"}]
    print(list02)  # 输出完整列表
    print(list02[0]) # 输出列表的第一个元素
    #更新列表
    jsondata={"sex":"nnnn"}
    list02.append (jsondata)  ## 使用 append() 添加元素
    #['runoob01', 78602, 2.2303, 'john04', 70.205, {'name': 'v_hhh'}, 'Google']
    print (list02)
    #删除列表元素
    indexlist= 2
    del [indexlist] #0 1 2 3 4 5
    print (list02)
    #['runoob01', 2.2303, 'john04', 70.205, {'name': 'v_hhh'}, 'Google']
    for lll in list02:
        print(lll)  # 输出列表的每一个个元素
    #统计某个元素在列表中出现的次数 n
    n = 0
    n = list02.count("happy")
    print(n)
x=[4,6,2,1,7,9,4]
x.sort()
print(x[-1])
print(x)


mm=[]
print(mm)
mm.append(1)
print(mm)
