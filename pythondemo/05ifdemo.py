# -*- coding: UTF-8 -*-
"""
   题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
   """
def  threenum():
    a=1
    b=1
    c=1
    for a in range(1,5):
        for b in range (1, 5):
            for c in range (1, 5):
                if((a!=b)and (b!=c)and (c!=a)):
                    print(a*100+b*10+c)
                    #print (a , b , c)
    """
    123
    124
    132
    134
    142
    143
    213
    214
    231
    234
    241
    243
    312
    314
    321
    324
    341
    342
    412
    413
    421
    423
    431
    432
    """
"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

"""

def getlrjj(d):
    if(d<=0):
        return "请输入正数"
    endd = 0
    if(d<=100000):
        endd= d*10/100
    if(100000<d<200000):
        endd = 100000*10/100 +(200000-d)*7.5/100
    if (200000 <= d < 400000):
        endd = 100000 * 10 / 100 + (200000 - 100000) * 7.5 / 100+(400000 - d) * 5 / 100
    if (400000 <= d < 600000):
        endd = 100000 * 10 / 100 + (200000 - 100000) * 7.5 / 100+(400000 - 200000) * 5 / 100+ (600000 - d) * 3 / 100
    if (600000 <= d < 1000000):
        endd = 100000 * 10 / 100 + (200000 - 100000) * 7.5 / 100+(400000 - 200000) * 5 / 100+(600000 - 400000) * 5 / 100 + (1000000 - d) * 1.5 / 100
    if (d >= 1000000):
        endd = 100000 * 10 / 100 + (200000 - 100000) * 7.5 / 100+(400000 - 200000) * 5 / 100+(600000 - 400000) * 5 / 100 + (1000000 - 600000) * 1.5 / 100+( d- 1000000) * 1/ 100
    print ( endd  )
    print(str(endd/10000)+"万")
    return endd

    #print(getlrjj(10000))

"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""
def sortnum():
    numa =[]
    for i in range(3):
        a = int(input('integer:\n'))
        numa.append(a)
    print(numa)
    numa.sort()
    print(numa)

def fibs(n):
    print("执行fn"+str(n))
    #第N个斐波那契数
    if n==1 or n==2:
        return 1
    return fibs(n-1)+fibs(n-2)
print(fibs(9))

name = "python"
name02 = "python02"
if (name == "python"):
    print("you  like python")
if (name02 == 'python02'):
    print("you do not like python")
print("----------------------------------------------------------------------------------------")
def iscontain(strS,contstr):
    if strS.find (contstr) == -1:
        print ("Found " + contstr + " not in " + strS)
        #print(strS.find (contstr) )
        return False
    else:
        print("Found "+contstr+" in "+strS)
        #print (strS.find (contstr))
        return True
ww= iscontain("ianname","name")
print("ww")
print(ww)
print("----------------------------------------------------------------------------------------")
aa=["cos","本地"]
bb=["北京","上海","广州","深圳","长春"]
cc=["新增","已有版本"]
print(aa.__contains__("a"))
cases=[]
for str01 in aa:
    case=""
    for str02 in bb:
        for str03 in cc:
            case = str01 + "-" + str02 + "-" + str03
            if cases.__contains__(case)==False:
                cases.append(case)
                print(case)


print(cases.__len__())
print(cases)
print("----------------------------------------------------------------------------------------")




