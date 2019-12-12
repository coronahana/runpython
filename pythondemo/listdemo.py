

def newlist():
    # 2-列表生成式
    #     1- aftertax=[int(one*0.9) for one in beforetax]
    #     2- 过滤条件：aftertax=[one*0.9 for one in beforetax if one>=10000]
    print ([one * 0.9 for one in range (10009) if one >= 10000])
    print ([one * 0.9 for one in range (11)])

if __name__ == '__main__':
    newlist()