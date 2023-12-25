#注意点1.xpath返回列表2.xpath的位置锁定3.数据处理
#-----------------------------------
#1.如何提取单页面的数据
#2.上线程池，多个网页同时抓取
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor
f=open("data.csv",mode="w",encoding="utf-8")
csvwriter=csv.writer()
def download_one_page(url):
    resp=requests.get(url)
    encodings="utf-8"#主要看charset里面写什么
    html=etree.HTML(resp.text)
    #print(resp.text)
    #我们这个时候要找壳子，也就是table,（见图片table）
    table=html.xpath("./html/body/div[2]/div[4]/div[1]/table")[0]#要加上一个[0]，虽然只有一个元素，但是列表无法进行下一步xpath
    trs=table.xpath("./tr")[1:]#看有多少行，当然我们第一行不要所以加上
    #换一种写法xpath的延申#锁定位置，xpath的结构是从一开始数的
    #trs=table.xpath("./tr[position()>1]")
    # print(len(trs))
    #拿到每一个tr
    for tr in trs:
        txt=tr.xpath("./td/text()")#得到的数据并不好所以我们需要做简单的处理图片见（td得到的数据）
        #去掉\\ /，3数据处理
        txt=(item.replace("\\","").replace("/","") for item in txt)
        print(list(txt))#生成器表达式是一种节省内存的方式，因为它不会立即生成所有结果，
        # 而是在需要时逐个生成。但是，当你想要一次性查看所有生成的结果时，可以通过将生成器转换为列表来实现。
        #使用list()是基于需要将生成器的结果转换为一个有序、可修改的数据结构，以便后续操作。
        #print(txt)
        #csv文件写到前面去,数据存放
        csvwriter.writerow(txt)
    print(url,"完成")
if __name__ == '__main__':
    #效率低下，一共200页
    # for i in range(1,14870):
    #     download_one_page(f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            t.submit(download_one_page,f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    print("全部下载完毕")