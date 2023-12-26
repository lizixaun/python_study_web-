#1.await与wait的使用地方不同2.协程对象先包装成task（任务）对象3.关闭循环
#——————————————————————————————————————————————————————————————————————————————————————————
#request.get()同步的代码
#pip install aiohttp
import asyncio
import aiohttp
#直接给html吧，就只是单纯演示一下怎么操作
urls=[
    "https://pic.3gbizhi.com/uploadmark/20231225/2eb080e4d1bdadd772c1a6e1f851e6fe.jpg",
    "https://pic.3gbizhi.com/uploadmark/20231225/8ee4f35b485d518ab17ff41c197c4f2f.jpg",
    "https://pic.3gbizhi.com/uploadmark/20231225/bbf17c51a791adbc4f40f35000d5f40e.jpg"
]
async def aiodownload(url):
    #发生请求
    #得到图片
    #保存图片
    # s=aiohttp.ClientSession() <==>request.session()
    #reqiest.get()  .post()
    #s.get()    .post()
    # with open("abc.csv",)as f:#*****重点这个with是上下管理器，连接上下的，当上面结束了，下面也会自动关闭
    #     f.write()
    name = url.rsplit("/", 1)[1]  # 从右往左，最多切割一次。我们拿切割后面的第1个，也就是最后面的（详细见E:\study_web\第四章\split与rsplit的区别）
    async with aiohttp.ClientSession() as session:#requests
        # session.get()
        # session.post()
        async with session.get(url) as resp:#resp=requests.get()
            #resp.content.read() #等价于之前的resp.content,读取内容
            #resp.text()#等价 与之前的resp.text
            #resp.json()
            #可以学习模块，aiofile
            with open(name,mode="wb")as f:
                f.write(await resp.content.read())#读取内容是异步的，需要await挂起
    print(name,"搞定")
async def main():#url打开，创建aiodownload任务
    tasks=[]
    for url in urls:
        d=asyncio.create_task(aiodownload(url))
        tasks.append(d)
    await asyncio.wait(tasks)
if __name__ == '__main__':
    # asyncio.run(main())  # 原本会报错，改成下面就不会报错了
    # 获取当前事件循环
    loop = asyncio.get_event_loop()
    # 运行直到完成所有任务
    loop.run_until_complete(main())

