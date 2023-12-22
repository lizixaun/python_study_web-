import requests
from bs4 import BeautifulSoup
#bs4思路一直缩小范围
url="https://www.umeit.cc/bizhitupian/weimeibizhi/"
resp=requests.get(url)
resp.encoding='utf-8'
print(resp.text)
#把源代码交给bs
main_page=BeautifulSoup(resp.text,"html.parser")
#bs4第一次处理html,记得class要加上_，不然一直报错
alist=main_page.find("div",class_="TypeList").findall("a")#竟然可以一次性处理文件
#findall再找a标签
for a in alist:
    #print(a.get('href'))#直接通过get拿到属性的值
    href=a.get('href')
    #拿到值页面的源代码
    child_oage_resp=requests.get(href)
