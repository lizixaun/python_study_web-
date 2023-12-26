#学习点1：time.time的计算算法时间。2：一次启动多个任务（协程）
#---------------------------------------------------
# import time
# def func():
#     print("我爱黎明")
#     time.sleep(3)   #让当前的线程处于阻塞状态，cpu是不为我工作的。也泡脚时候技师，不按脚一样
#     print("我真的爱黎明")
# if __name__ == '__main__':
#     func()
#input（）程序也是处于阻塞状态
#resquest.get（）在网络返回数据之前，程序也是处于阻塞状态
#一般情况下，当程序处于IO操作的时候，线程都会处于阻塞状态

#协程：当程序遇见IO操作的时候，可以选择性的切换到其他任务上
#在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
#在宏观上，我们能看到的其实是多个任务一起在执行
#多任务异步操作

#上方所讲的一切，都是在单线程上操作
#---------------------------------------------------------
# import asyncio#异步，非同步（asynchronous）
# async def func():#带点东西，函数就变了
#     print("你好啊，我叫赛利亚")
#
# if __name__ == '__main__':
#     g=func()  #此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     # print(g)
#     asyncio.run(g)#协程程序运行需要asyncio模块的支持
#----------------------------------------------------------
#这个只是为了方便理解，python最好还是下下部分那么写代码
# import asyncio
# import time
#
#
# async def func1():
#     print("你好好，我叫潘金莲")
#     #time.sleep(3)#当程序出现同步操作的时候，异步就中断了
#     await asyncio.sleep(3)#异步操作代码要表示，电脑又不是人，不知道哪个代码是异步的，如果不给电脑反应慢一点，都会以为自己是异步，直接跳完了
#     print("你好啊，我叫潘金莲")
# async def func2():
#     print("你好啊，我叫王建国")
#     #time.sleep(2)
#     await asyncio.sleep(2)
#     print("你好啊，我叫王建国")
# async def func3():
#     print("你好啊，我叫李子煊")
#     #time.sleep(4)
#     await asyncio.sleep(4)
#     print("你好啊，我叫李子煊")
# if __name__ == '__main__':
#     f1=func1()
#     f2=func2()
#     f3=func3()
#     tasks=[f1,f2,f3]#装列表里面同时开启
#     t1=time.time()
#     asyncio.run(asyncio.wait(tasks))#固定搭配（列表开始跑）
#     t2=time.time()
#     print(t2-t1)#9.032524824142456，同步效果
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#主流代码，说白了就是讲代码的启动跟加载拆分开，让我们后面代码可以好操作
import asyncio
import time


async def func1():
    print("你好好，我叫潘金莲")
    await asyncio.sleep(3)
    print("你好啊，我叫潘金莲")


async def func2():
    print("你好啊，我叫王建国")
    await asyncio.sleep(2)
    print("你好啊，我叫王建国")


async def func3():
    print("你好啊，我叫李子煊")
    await asyncio.sleep(4)
    print("你好啊，我叫李子煊")
async def main():#协程函数
    #第一种写法
    #f1=func1()
    # await f1  #一般await挂起操作放在协程对象前面，前面我有用到看一下
    tasks = [
        asyncio.create_task(func1()),#py.38yi'h
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]#版本改了要将协程对象先包装成task（任务）对象，再丢给可以使用task函数的代码，为了严谨吧
    await asyncio.wait(tasks)
if __name__ == '__main__':
    asyncio.run(main())#协程函数一跑得到一个协程对象