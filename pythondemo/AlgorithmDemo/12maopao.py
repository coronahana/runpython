def maopao():
    list01=[1,4,6,66,2,3]
    list02=[]
    for i in range(list01.__len__()) :
        for j in  range(list01.__len__()-i-1):
            if list01[j]>list01[j+1]:
                list01[j], list01[j + 1]=list01[j+1],list01[j ]
        list02.append(list01[list01.__len__()-i-1])
    print(list02)
    alist = [1, 5, 0, 9, 2]
    for i in range (0, len (alist) - 1):  # 0 ~4 ----  0 1 2 3--取最大值的次数
        for j in range (0, len (alist) - i - 1):
            # 只是交换的次数，但要不要交换取决于   相邻值的大小  temp
            if alist[j] < alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    print (alist)

if __name__ == '__main__':
    maopao()
    alist = [1, 5, 0, 9, 2]
    alist.sort(reverse=False)
    print(alist)

    alist02 = [1, 5, 0, 9, 6]
    alist02.reverse() #反转
    print(alist02)

