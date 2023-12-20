#pip install requests安装
#pip清华源比较稳定
import requests
#get方式,地址栏里面一定是get
query=input("输入人名")
#f高级用法
url=f"https://www.sogou.com/web?query={query}"

#network的wed里面有一个User-Agent
headers={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
resp=requests.get(url,headers=headers)#获得响应状态

print(resp)#得到200
print(resp.text)#拿到源代码