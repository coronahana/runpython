

def newlist():
    # 2-列表生成式
    #     1- aftertax=[int(one*0.9) for one in beforetax]
    #     2- 过滤条件：aftertax=[one*0.9 for one in beforetax if one>=10000]
    print ([one * 0.9 for one in range (10009) if one >= 10000])
    print ([one * 0.9 for one in range (11)])

def listjishu():
    li=[1,1,2,3,4,5,6,7,8,9]
    for i in li:
        if i%2!=0:
            li.remove(i)
    print(li)
if __name__ == '__main__':
    # newlist()
    listjishu()