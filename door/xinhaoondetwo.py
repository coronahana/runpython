

#* 函数接收参数为元组
def myfun01(*args): #相当于 def myfun(1,2,3)    ==> args 就相当于（1,2,3）
    a=""
    for a in args:
        print(a)

#** 表示函数接收参数为一个字典
def myfun02(**args) :#相当于 def myfun({a:1,b:2,c:3}) ==>args 就相当于{a:1,b:2,c:3}
    k=""
    v=""
    for k,v in args:
        print(k,":",v)


myfun01(2,3,4)
#kk={"gg":1,"bb":2,"cc":3}
#myfun02(kk)

url = '/home/register'
print(url)
print(url.format([]))