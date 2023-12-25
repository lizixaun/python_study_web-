#线程，进程
#进程是一个资源单位（跑一个网页系统会分内存区域，这里面有变量啥的）
# 线程是一个执行单位：一个进程里面会有若干个线程帮我们工作，cpu在执行跑一个线程
#进程相当于公司，线程相当于员工，一个公司至少有一个员工

#启动一个程序默认会有一个主线程，
# def func():
#     for i in range(1000):
#         print("func",i)
# if __name__=='__main__':
#     func()
#     for i in range(1000):
#         print("main",i)
#____________________________________这段代码其实还是一根线的，还是一个人在干，
#代码结果，上面那个程序跑完之后，下面才开始跑
# func 996
# func 997
# func 998
# func 999
# main 0
# main 1
# main 2
# main 3
#-----------------------------------------------------------------------------------------------------------------------
#多线程（第一套写法）
# from threading import Thread
# def func():
#     for i in range(1000):
#         print("func",i)
# if __name__=='__main__':
#     t=Thread(target=func)#创建线程，并给线程安排任务
#     t.start()           #多线程状态为可以开始工作状态，具体执行时间由cpu决定，就像老板给你安排工作，但是这个员工可能还得去上厕所
#     #t2=Thread(target=xxxx)
#     #t2.start()
#     for i in range(1000):
#         print("main",i)
#---------------------------------------------------------------------------------------------------
# #多线程（第二套写法）--------
# from threading import Thread
# class MyThread(Thread):         #继承Thread：我们写的MyThread继承了Thread那么我们就会有他的特性
#     def run(self):              #重写run这个函数，固定的#当线程被执行的时候，被执行的就是run
#         for i in range(1000):
#             print("子线程",i)
# if __name__=='__main__':         #输入main+tab快速补齐
#     t=MyThread()                #先造对象，不要t.run()，不然就变成方法的调用了，就变成单线程了。
#     t.start()                   #开启线程
#     for i in range(1000):
#         print("主线程",i)
#---------------------------------------------------------
# #下面讲解一下多线程的多线程，没有名字这个解决方法，也就是传参
# from threading import Thread
# def func(name):         #name传参方式
#     for i in range(1000):
#         print(name,i)
# if __name__ == '__main__':              #args中文意思参数
#     t1=Thread(target=func,args=("周杰伦",))#传参必须是元组，也就是两个，如果没有两个，那我们要加上','号
#     t1.start()
#     t2=Thread(target=func,args=("王力宏",))
#     t2.start()
#---------------------------------------------------------------------
#多线程（第二套写法）--------的加名字
from threading import Thread
class MyThread(Thread):
    def run(self):
        for i in range(1000):
            print(f"子线程 {self.getName()} - {i}")
if __name__ == '__main__':
    jay_thread = MyThread()
    jay_thread.setName("周杰伦")  # 设置周杰伦线程名字
    wang_thread = MyThread()
    wang_thread.setName("王力宏")  # 设置王力宏线程名字
    jay_thread.start()
    wang_thread.start()
    for i in range(1000):
        print("主线程", i)

