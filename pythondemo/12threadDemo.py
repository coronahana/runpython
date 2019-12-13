from time import ctime,sleep
import threading
def music(func):
    for i in range(2):
        print(str(i)+",I was listening to music."+func +","+ctime())
        sleep(2)#每首音乐播放需要1秒钟
def move(func):
    for i in range(2):
        print(str(i)+",I was at the movies!"+func +","+ctime())
        sleep(7)#每一场电影需要5秒钟
threads = []
t1 = threading.Thread(target=music, args=('爱情买卖',))
threads.append (t1)
t2 = threading.Thread(target=move, args=('阿凡达',))
threads.append (t2)

if __name__ == '__main__':
    #子线程（muisc 、move ）和主线程（print "all over %s" %ctime()）
    for t in threads:
        print(t)
        t.setDaemon(True)
        t.start ()
    t.join ()#join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。

    print("退出主线程" + ctime())
"""
<Thread(Thread-1, initial)>
0,I was listening to music.爱情买卖,Mon Sep 23 18:55:53 2019
<Thread(Thread-2, initial)>
0,I was at the movies!阿凡达,Mon Sep 23 18:55:53 2019
1,I was listening to music.爱情买卖,Mon Sep 23 18:55:55 2019
1,I was at the movies!阿凡达,Mon Sep 23 18:56:00 2019
退出主线程Mon Sep 23 18:56:07 2019
"""