# 注意1：iv字节格式（搜索iv）2.视频文件这些读取写法都需要加上mode="wb",mode="rb"3.将列表以一定规律拼接起来：a="".join(列表)3.系统指令格式：os.system()copy 是一个用于复制文件的命令。
# /b 表示二进制复制，告诉命令提示符这是一个二进制文件。4.AES解密加密
#______________________________________________________________________________________________________________________________
#前提无法直接在html里面找到我们需要的东西，需要借助开发者工具，
#1.找到最外面看一下有没有一个叫iframe，网页框架，在一个html中嵌入一个html（"综合训练图片存放\iframe.png"）,
"""
思路：
    1.拿到主页面的页面源代码，找到iframe
    2.从iframe的页面源代码中拿到m3u8文件的地址---页面源代码查询方式（图片：全屏后面的页面源代码查询方式，未经过脚本)
    3.下载第一层m3u8文件-->下载第二层m3u8文件（视频顺序1.2）#我们上面拿到的m3u8是第一层
    4.下载视频
    5.第二层，下载密钥进行解密
    6.合并所以ts视频为一个mp4文件
"""
import re
import asyncio
import aiohttp
import aiofiles
import requests
from Crypto.Cipher import AES
from bs4 import BeautifulSoup
import os
def get_iframe_src(url):
    # resp=requests.get(url)
    # main_page=BeautifulSoup(resp.text,"html.parser")
    # src=main_page.find("iframe").get("src")
    # # print(resp.text)#结果见（ifranme标签）
    # print(src)
    # # return src
    return "https://boba.52kuyun.com/share/xfPs9NPHvYGhNzFP"#为了做测试,就是得到src
    # return "https://my3.1980dyy.com/xun.php?url=https://vip.ffzy-online2.com/20230924/44663_620a896f/index.m3u8"
def get_first_m3u8_url(url):
    resp=requests.get(url)
    print(resp.text)
    obj=re.compile(r'var main="(?P<m3u8_url>.*?)"',re.S)
    m3u8_url=obj.search(resp.text).group("m3u8_url")
    #print(m3u8_url)
    return m3u8_url
def download_m3u8_file(url,name):
    resp=requests.get(url)
    with open(name,mode="wb")as f :
        f.write(resp.content)
async def download_ts(url,name,session):
    # async with aiohttp.ClientSession() as session:#如果这个的话我们每次都需要几百条request，很浪费时间
    async with session.get(url) as resp:
        async with aiofiles.open(f"video2/{name}",mode="wb")as f:
            await f.write(await resp.content.read())#把下载的内容写入文件中#两个await因为文件请求，和保存都是异步请求
    print(f"{name}下载完毕")#下载完毕，开始解码环节（图片：开始解码环节）
async def aio_download(up_url):#拼接加下载#https://bobao.52kuyun/201270906/Moh219zV/hls/
    tasks=[]
    async with aiohttp.ClientSession() as session:#提取准备好session
        async with open("越狱二人组_second_m3u8.txt",mode="r",encoding="utf-8")as f :
            async for line in f:
                if line.startswith("#"):
                    continue
                else:
                    line.strip()#去掉没用的换行
                #拼接真正的ts的路径
                ts_url=up_url+line#因为读一行一个任务，读一行一个任务，所以我们需要准备一个任务列表task
                task=asyncio.create_task(download_ts(ts_url,line,session))#对象是一个协程对象#创建任务#我们将本来这个内容读取到的部分，设置为名字
                tasks.append(task)
            #整个结束之后我们需要await一下
            await asyncio.wait(tasks)#等待任务结束（图片：开始解码环节）
def get_key(url):
    resp=requests.get(url)
    # print(resp.text)
    return resp.text
async def dec_ts(name,key):
    #加密方式在key里面有写（图片：解码读文件夹.jpg）
    #EXT-X-KEY:METHOD=AES-128,URI="key.key"
    #导入AES加密包
    aes=AES.new(key=key,IV=b"0000000000000000",mode=AES.MODE_CBC)#iv放字节，key多长就放多长，一般为16的倍数，字节格式
    #接下来：1.文件读出来2.通过key来解密3.然后存起来
    # async with aiofiles.open(f"video2/{name}",mode="rb")as f1,aiofiles.open(f"video2/temp_{name}",mode="wb")as f2:
    async with aiofiles.open(f"video2/{name}",mode="rb")as f1,\
        aiofiles.open(f"video2/temp_{name}",mode="wb")as f2:        #这么写好看点，将文件读出来，然后写到其他地方去（）
        bs=await f1.read()  #从源文件读取内容
        # aes.encrypt()加密
        aes.decrypt(bs)#解密
        await f2.write(aes.decrypt(bs))#把解密好的内容写入文件即可
    print(f"{name}处理完毕")
async def aio_dec(key):
    tasks=[]
    #解密，我们需要将文件夹里面所有的文件全部读出来（解码读文件夹.jpg），图片左边的为一个个的文件，右边为一个文件，我们现在只需要名字，然后使用名字将在async def dec_ts(name,key):中把文件内容按照名字的顺序读出来，所以我们现在直接读一整个文件的名字，然后传给其他函数
    async with aiohttp.open("越狱二人组_second_m3u8.txt",mode="r",encoding="utf-8")as f :
        async for line in f:
            if line.startswith("#"):
                continue
            else:
                line=line.strip()
            #开始异步任务
            task=asyncio.create_task(dec_ts(key,line))#访问+解密dec这个文件
            tasks.append(task)
        await asyncio.wait(tasks)
def merge_ts():
    #mac:cat 1.ts 2.ts 3.ts > xxx.mp4
    #windows:copy /b 1.ts+2.ts+3.ts xxx.mp4
    #思路：将文件名那个文件也就是（"越狱二人组_first_m3u8.txt"）读取之后将名字拼接起来
    lst=[]
    with open("越狱二人组_first_m3u8.txt",mode="r",encoding="utf-8")as f :
        for line in f :
            if line.startswith("#"):
                continue
            line.strip()
            #上面只是得到名字的一部分，但是没有路径，路径是我们最后一次保存的文件，解密后的路径也就是（f"video2/{name}"）
            lst.append(f"video2/{line}")#名字是新的，使用列表拼接起来
    #——————————————————————————————————————————————————————————————————————————————————————————————————————------
    #对于mac而言，需要每一个加上空格拼接起来
    s=" ".join(lst)#1.ts 2.ts 3.ts
    #然后执行命令，导入os模块，os可以执行一些简单的命令
    os.system(f"cat {s} > movie.mp4")
    print("搞定！！")
    #————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————-
    s = "+".join(lst)
    #"+".join(lst) 是一个字符串的方法，它将列表 lst 中的所有元素按照指定的连接符 + 进行连接成一个新的字符串。
    # 然后执行命令，导入os模块，os可以执行一些简单的命令
    os.system(f"copy /b {s} movie.mp4")
    print("搞定！！")
def main(url):
    #1.拿到主页面的页面源代码，找到iframe对应的url地址
    iframe_src=get_iframe_src(url)
    #2.拿到第一层m3u8文件的下载地址
    first_m3u8_url=get_first_m3u8_url(iframe_src)#我们拿到的地址只拿到一半，没有域名（图片：first_m3u8_url）
    #我们得加上域名，域名长什么样，打开这个m3u8的request看url，因为这个视频是由iframe的src网站地址的前半段，再加上后面的我们得到的first_m3u8_url拼接成的
    #拿到iframe的域名"https://boba.52kuyun.com/share/xfPs9NPHvYGhNzFP"，就是我们上面得到的src
    iframe_domian=iframe_src.split("/share")[0]
    #拼接出真正的m3u8的下载路径
    first_m3u8_url=iframe_domian+first_m3u8_url
    #"https://boba.52kuyun.com/20170906/Moh2l9zV/index.m3u8?sign=548ae366a075f0f9e7c76af215aa18e1"
    # print(first_m3u8_url)
    #3.1下载第一层m3u8文件
    download_m3u8_file(first_m3u8_url,"越狱二人组_first_m3u8.txt")#得到效果视频顺序1（图片）
    #3.2
    with open("越狱二人组_first_m3u8.txt",mode="r",encoding="utf-8")as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line=line.strip()#去掉空白或者换行符
            #我们得到第一层m3u8内容为（第一层m3u8内容和第二层m3u8地址的关系）#内容：hls/index.m3u8
            #准备拼接第二层m3u8的下载路径
                second_m3u8_url=first_m3u8_url.split("index.m3u8")[0]+line
                download_m3u8_file(second_m3u8_url,"越狱二人组_second_m3u8.txt")
                print("第二层下载完毕")#第二层打开之后就是视频顺序2的样子，但是ts是相对路径，我们需要打开视频里面的其他ts看一下他们的url的绝对路径，（图片：第二层ts绝对路径）
                #https://bobao.52kuyun/201270906/Moh219zV/hls/cFN8o3436000.ts,对比第二层，m3u8路径我们得出，ts最终路径为第二层路径的前面加上，我们得到第二层ts内容进行拼接，（参考图片：第一层m3u8内容和第二层m3u8地址的关系）
    #4.下载视频
    second_m3u8_url_up=second_m3u8_url.replace("index.m3u8","")
    #看内容我们得到，一个视频任务量很大，直接异步操作吧
    asyncio.run(aio_download(second_m3u8_url_up))#测试的时候可以注释掉
    #5.1拿到密钥（E:\study_web\第四章\综合训练图片存放\课件\开始解码环节.jpg）
    #key.key的url("E:\study_web\第四章\综合训练图片存放\课件\key.key文件的url.jpg")
    key_url=second_m3u8_url_up+"key.key"#这个key的链接url,等于前面一个url+密钥#偷懒写法，正常应该去m3u8文件里面去找
    key=get_key(key_url)#函数下载key密钥，我们得到的就是(key.key的preview)
    #5.2解密。将每一个文件读出来，然后再解密，最后放到一个新文件里面去,所以我们也使用异步操作
    asyncio.run(aio_dec(key))
    #6.合并ts文件为MP4文件
    merge_ts()
if __name__ == '__main__':
    url="https://www.91kanju.com/vod-play/541-2-1.html"
    main(url)