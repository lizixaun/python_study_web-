#有的网站的m3u8有时效性，会有一定的时间间隔之后刷新（网站m3u8时效性）
"""
流程：
    1，拿到548121-1-1.html的页面源代码
    2。从源代码中提取到m3u8的url
    3，下载m3u8
    4，读取m3u8文件，下载视频
    5.合并视频
"""
"""
import re

import requests
obj=re.compile(r"url:'(?P<url>.*?)',",re.S)#用来提取m3u8的url地址
url="https；//www.91kanju.com/vod-play/54812-1-1.html"
resp=requests.get(url)
# print(resp.text)
resp.close()#记得关啊
m3u8_url=obj.search(resp.text).group("url")#拿到m3u8的地址
print(m3u8_url)
#下载m3u8文件
resp2=requests.get(m3u8_url)
with open("片面.m3u8",mode="wb")as f:
    f.write(resp2.content)
resp2.close()
print("下载完毕")
"""
#——————————————————————————————————————————————————————————————————————————————————————————————————
#接下来的片段我们找一个可以播放的网站来验证学习m3u8，已爬取完
import requests
"""

url="https://v3.1080pzy.co/20230212/qbJbaSxv/1100kb/hls/index.m3u8"
resp=requests.get(url)
with open("爱恋依存痴.m3u8",mode="wb")as f :
    f.write(resp.content)
resp.close()
"""

#解析m3u8文件
n=1
with open("爱恋依存痴.m3u8",mode="r",encoding="utf-8")as f:
    for line in f:
        line=line.strip()#先去掉空格，空白，换行符
        if line.startswith("#"):#如果以#开头，我们不要
            continue            #直接下一行
        # print(line)#无论结果是什么都必须访问
        resp3=requests.get(line)
        f=open(f"video/{n}.ts",mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        n=n+1
        print("完成了一个")
#---------------------------------------------------------------------------------
#视频拼接，（重要里面）
