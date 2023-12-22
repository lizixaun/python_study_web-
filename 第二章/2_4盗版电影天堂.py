# 1.定位到2023必看片
# 2.从2023必看片中提取到子页面的链接地址
# 3.亲求子页面的链接地址，拿到我们先要的下载链接
import requests
import re
domain="https://www.dytt89.com/"
#要提取的html部分代码，在"2023必看.html"
#去掉安全验证，resp=requests.get(domain,verify=False)
resp=requests.get(domain)
resp.encoding='gb2312'#指定字符集
# print(resp.text)
#定位一部分html，匹配里面的每一行的一部分思路
#拿到ul里面的的
obj1=re.compile(r'2023必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
#开始操作这个是第10行开始写的
#跟前面一样不需要全部写下来
obj2=re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3=re.compile(r'<tbody>.*?<a href="(?P<url>.*?)">magnet:',re.S)
result1=obj1.finditer(resp.text)
child_href_list=[]
for it in result1:
    ul=it.group('ul')
#html中a标签把htmL括起来了，仔细看a标签里面存放着超链接
#链接放在herf里面，里面的title，是鼠标悬浮之后的下面的字
    #提取子页面链接：
    result2=obj2.finditer(ul)
    for itt in result2:
        #拼接子页面的url
        child_href=domain+itt.group('href').strip("/")#把前面的/给去掉
        child_href_list.append(child_href)
        # print(child_href)


#提取子页面的内容
for href in child_href_list:
    # print(href)
    child_resp=requests.get(href)
    child_resp.encoding='gb2312'
    # print(child_resp.text)
    result3=obj3.finditer(child_resp.text)
    print(result3.group("url"))


