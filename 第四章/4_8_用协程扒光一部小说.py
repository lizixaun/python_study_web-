#注意内容：1.拿到json的部分内容（包括属性内容）2.转换成json格式（重要里面有）3.异步的文件读写
#pip install aiofiles
#——————————————————————————————————————————————————————————————————————————————————————————————
#1.第一个链接同步操作,得到章节的cid和名称2.下面链接异步操作，下载文章的内容
# Request URL:
#http://dushu.baiducom/api/pc/getCatalog?data=["book id":"4306063500")=> 所有章节的内容(名称，cid)
#章节内部的内容
# http://dushu.baidu.com/api/pc/gethapter(ontent?data=("book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}
import requests
import asyncio
import aiohttp
import json
import aiofiles
async def aiodownload(cid,b_id,title):#看一下第二个链接需要哪些东西拼接出来
    data={
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data= json.dumps(data)#得到一个urljson格式#为什么需要变为json解释有点长，我放在"为什么需要变为json格式"文本里面
    url=f"http://dushu.baidu.com/api/pc/gethapter(ontent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with aiohttp.get(url) as resp:
            dic=await resp.json()
            async with aiofiles.open(title,mode="w",encoding="utf-8")as f:
                await f.write(dic['data']['novel']['content'])#把小说内部写出

            # dic['data']['novel']['content']文章的具体内容，也就是小说内容
async def getCatalog(url):
    resp=requests.get(url)
    # print(resp.text)#得到结果看4_8扒光小说第一条链接
    #想要拿到的话需要
    # print(resp.json())
    dic =resp.json()
    tasks=[]
    for item in dic['data']['novel']['item']:#item对应每一个章节的名称和cid#注意内容：1.拿到json的部分内容
        title=item['title'] #目的为了拿到小说的名字，我们后期将小说内容保存的跟名字放一起   #1.拿到json的属性内容,在第一条链接preview里面
        cid =item['cid']
        #准备异步任务
        tasks.append(aiodownload(cid,b_d,title))
    await asyncio.wait(tasks)
        # print(cid,title)
if __name__ == '__main__':
    #bookid在下面这个url可以用，在第二个url也可以用上。所有单独拿出来方便后期代码的修改
    b_d="4306063500"
    url='http://dushu.baiducom/api/pc/getCatalog?data=["book id":'+b_d+')'#单引号拼接起来
    asyncio.run(getCatalog(url))