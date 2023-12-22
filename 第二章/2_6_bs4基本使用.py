#安装
#pip install bs4 -i 清华
#pip install bs4
#1.拿页面源代码
#2.使用bs4进行解析，拿到数据
import requests
from bs4 import BeautifulSoup
import csv
url="http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp=requests.get(url)
f=open(".html",mode="w",encoding="utf-8")
csvwriter=csv.writer(f)
print(resp.text)
#解析数据
#1.把页面源代码交给beautifulsoup进行处理，生成bs对象
#告诉beautifulsoup我给的是html源代码就不会有警告了
page=BeautifulSoup(resp.text,"html.parser")
#2.从bs对象中查找数据
#find找一个跟正则的有search一样
# find(标签，属性=值)
#findall找全部
#findall(标签，属性=值)
# table=page.find("table",class_="hq_table")#但是class是python里面的关键字，所以报错在属性后面加上一个下划线可以区别关键字与html
table=page.find("table",attrs={"class":"hq_table"})#很麻烦，解决方法就是用字典封装
#<table是表格的刚刚开始的那个标签eg:<table class="hq_table>
#print(table)
trs=table.find_all("tr")[1:0]#不要第一行，找表格里面所有的tr，tr是行的数据
#格式是这样的，不一样的是它的品名啥的，价格变为数字什么的
#所有我们看第一行的表一般可以看出很多东西
#步骤第一个fand用来定位，第二个用来，排数据
# <tr class="tr_1">
# <td class="td 1" width="90">品名</td><td width="90">最低价</td><td width="90">平均价</td><td width="90">最高价</td><td width="90">规格</td><td width="80">单位</td><td width="90">发布日期</td><td width="10"> </td>
# </tr>
for tr in trs:
    tds=tr.find_all_next("td")#拿到每行中的所有td
    name=tds[0].text#拿到被标签标记的内容
    low=tds[1].text#拿到被标签标记的内容
    avg=tds[2].text#拿到被标签标记的内容
    hight=tds[3].text#拿到被标签标记的内容
    guige=tds[4].text#拿到被标签标记的内容
    kind=tds[5].text#拿到被标签标记的内容
    data=tds[6].text#拿到被标签标记的内容

    csvwriter.writerow(name,low,avg,hight,guige,kind,data)
f.close()