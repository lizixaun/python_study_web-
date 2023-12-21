#network里面的sug可以拿到翻译的内容，
#sug的headers里面可以查看新网页，因为输入可以改变网页地址，包括是post
#post的链接：传参方式是直接拼接在链接后面，post不是直接拼接
import requests
url="https://fanyi.baidu.com/sug"
#由于是匹配的为字典from data
s=input("请输入你要翻译的单词")
dat={
    "kw":s
}
resp=requests.post(url,data=dat)
#print(resp.text)
print(resp.json())#服务器返回的直接转换成python里面的字典