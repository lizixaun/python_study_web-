#拿页面源代码
#提取和解析数据
import requests
from lxml import etree
url="https://www.zbj.com/fw/?k=saas"
headers={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
resp=requests.get(url=url,headers=headers)
# print(resp.text)
#解析
html=etree.HTML(resp.text)
#代码思路模块化处理
#定位第一块，用开发者工具，往上找一层#然后再右键xpath.//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div[1]将这个最后一个1干掉就是全部div
#这就是拿到全部服务商的信息
divs=html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div')
#正常网站id不可以重复
for div in divs:
    a=div.xpath("./div/a/div[2]/div[1]/div/text()")#//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div[1]/div/a/div[2]/div[1]/div
    b=div.xpath("./div/div[3]/div[1]/span/text()")[0].strip("¥")#列表里面拿出来[0],去掉￥
#-------------------------------------------------------------------------------------------------------
    #以下代码无法执行，只用于学习
    price = div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")[0].strip("￥")
    #title = div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()")
    #title出来的格式为['xxx','xxx'],从html里面可以看到saas为关键字，做一个高量显示，就是搜索显示
    title = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))#直接拼起来就完事
    com_name = div.xpath("./div/div/a[2]/div[1]/p/text()")[0]
    location = div.xpath("./div/div/a[2]/div[1]/div/span/text()")[0]
#不要
    print(b)


