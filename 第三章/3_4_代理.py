#原理：通过第三方的机器去发送亲求
import requests
#58.20.82.103,端口2323
proxies={
    #"http":"",#http的时候走这个
    # "https":""#https的时候走这个
    "https": "8.130.39.155:3389"  #现在得加上https://----如"https": "https://8.130.39.155:3389"
    #但是我不知道为什么我们这个不加
}
resp=requests.get("https://www.baidu.com",proxies=proxies)
resp.encoding='utf-8'
print(resp.text)