#用50个线程爬取北京新发地的全部资源
#线程池：一次性开辟一些线程，我们用户直接给线程池提交任务
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
#concurrent共同发生，future未来
def fn(name):#url
    for a  in range(10):
        print(name,i)
if __name__ == '__main__':
    #创建线程池
    with ThreadPoolExecutor(5) as t:
        for i in range(10):#100个任务
            t.submit(fn,name=f"线程：{i}")#执行fn这个任务，名字线程编号
    #等待线程池中的任务全部完成才执行下面的（守护）
    print("123")