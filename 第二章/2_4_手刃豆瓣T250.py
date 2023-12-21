#页面源代码里面写的也就是服务器get
import requests
import re
#以逗号做分割a,b,c,d,为了数据分析
import csv
url="https://movie.douban.com/top250"
headers={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
resp=requests.get(url=url,headers=headers)
page_content=resp.text
#html写成这样的,见top250text.html文件里面匹配部分
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
               r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" '
               r'property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)</span>',re.S)
result=obj.finditer(page_content)
#with open("firefox1.html", mode="w", encoding="utf-8") as f:
#f.write(content)
f=open("data.csv", mode="w", encoding="utf-8")
#csvwriter再往里面写文件就会这么写了
csvwriter=csv.writer(f)
for it in result:
    # print(it.group("name"))
    # print(it.group("score"))
    # print(it.group("year").strip())
    # print(it.group("num"))
    #字典形式全部出来
    dic=it.groupdict()
    #year单独处理，因为之前看了，它前面有空格
    dic['year']=dic['year'].strip()
    #写进去
    csvwriter.writerow(dic.values())
f.close()
