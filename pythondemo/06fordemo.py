for i in range(10,16):
    #[)10 15
    print("f"+str(i)+"oooo varchar(255),")
def iselse(number):
    num = number
    if num == 3:            # 判断num的值
        print ('boss')
    elif num == 2:
        print ('user')
    elif num == 1:
        print ('worker')
    elif num < 0:           # 值小于零时输出
        print ('error')
    else:
        print ('roadman')     # 条件均不成立时输出

nums=[0,1,2,3,4]
for number in nums:
    iselse(number)

print("-------------------------------------------------------")
fruits = ['banana', 'apple', 'mango']
#通过序列索引迭代
for index in range(len (fruits)):
    print(index)
    print('当前水果 :', fruits[index])
print("Good bye!")

print("-------------------------------------------------------")

for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果 :', fruit)

print("Good bye!")
print("-------------------------------------------------------")
i=0
j=0
k=0
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            #print("ijk="+str(i)+str(j)+str(k))
            mmm = i * i * i + j * j * j + k * k * k
            # print ("mmm" + str (mmm))
            nnn = 100 * i + 10 * j + k
            # print("nnn"+str(nnn))
            if (99 < mmm < 1000):
                #print(mmm)
                if (nnn == mmm):
                    print("水仙花:"+str(nnn))
                    print(type(str(nnn)))
print("----------------------------------------------------------------------------------")
