def f3():#区
    print('in f3 - begin')
    b = 4/0
    print('in f3 - end')
def f2():#市
    print('in f2 - begin')
    f3()
    print('in f2 - end')
def f1():#省
    print('in f1 - begin')
    f2()
    print('in f1 - end')

f1()#广东
"""
Traceback (most recent call last):
  File "E:/PycharmProjects/runpython/pythondemo/funapp.py", line 16, in <module>
    f1()#广东
  File "E:/PycharmProjects/runpython/pythondemo/funapp.py", line 13, in f1
    f2()
  File "E:/PycharmProjects/runpython/pythondemo/funapp.py", line 8, in f2
    f3()
  File "E:/PycharmProjects/runpython/pythondemo/funapp.py", line 3, in f3
    b = 4/0
ZeroDivisionError: division by zero
in f1 - begin
in f2 - begin
in f3 - begin
"""
#函数调用：f1-f2-f3--从上往下---发一个通知
#异常抛出：从下往上抛--事故处理

#如果你调用是一个第三库的方法：
#函数调用---上--->下---通知的发布
#异常的抛出  下--->上---事故的处理