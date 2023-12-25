#对比多线程，资源消耗的多
from multiprocessing import Process
def func():
    for i in range(10):
        print("子进程",i)

if __name__ == '__main__':
    # p=Process(target=func())代码错误：这样就会传递函数 func 的引用给 target 参数，而不是执行函数并将其返回值传递给 target
    p=Process(target=func)
    p.start()
    for i in range(10):
        print("主进程",i)