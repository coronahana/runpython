def tuptest():
    #Python的元组与列表类似，不同之处在于元组的元素不能修改。
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5)
    tup3 = "a", "b", "c", "d"


    list01 = [666,222,444,]
    #将列表转换为元组
    print (list01)
    tup02 = tuple(list01)
    print(tup02)
    print(max(tup02))  #如元组内所有元素都是int可以使用 max min
    print (min (tup02))
    print (len (tup02))
    print (tup2)
    try:
        del tup2  #元组虽然不能修改但是整个元祖可以删除
        print(tup2)
    except Exception:
        print("except Exception" )

    finally:
        print("finally")

tuptest()

import math

import random


def newuuid():
    uuid02 = 'jsxxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx'  #
    strname = list (uuid02)  # 将字符串转换为列表，列表的每一个元素为一个字符
    print (strname)
    for inv in range (len (strname)):
        #随机产生一个16进制数
        r = int ((random.random ()) * 16) |0
        print ("r=" + str(r))
        if strname[inv] == 'x':
            vv = str (hex (r))
        else:
            vv = str (hex (r & 0x3 | 0x8))
        print ("vv:" + str (vv))
        indexvalue = str(vv.replace ("0x", ''))
        print ("indexvalue:" + indexvalue)  # indexvalue:e
        if strname[inv] == 'x':
            strname[inv] =indexvalue
    print (strname)
    uuidnew = "".join (strname)
    print ("uuidnew="+uuidnew)

newuuid()







