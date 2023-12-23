from lxml import etree
#parse
tree=etree.parse("b.html")
# result=tree.xpath('/html')
# result=tree.xpath('/html/body/ul/li/a/text()')
#只要第一个,xpath开头是从1开始数的，
# result=tree.xpath('/html/body/ul/li[1]/a/text()')
#xpath里面的bs4，[@xxx=xxx]属性的筛选
# result=tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")
# print(result)

# #遍历：方法1
ol_li_list=tree.xpath("/html/body/ol/li")

for li in ol_li_list:
    #要查找哪一个一个就得留到他的前的一个节点，比如我要找飞机，大炮，火车啥的就得到li
    # < ol >
    # < li > < a
    # href = "feiji" > 飞机 < / a > < / li >
    # < li > < a
    # href = "dapao" > 大炮 < / a > < / li >
    # < li > < a
    # href = "huoche" > 火车 < / a > < / li >
    # < / ol >
    #从每一个li中提取到文字信息
    result=li.xpath("./a/text()")#在li中继续寻找，相对查找要加上./
    print(result)#['飞机']['大炮']['火车']
    #接下来拿属性的值,与bs4的属性筛选差不多
    result2=li.xpath("./a/@href")
    print(result2)
#遍历方法2：当然也可以直接找
print(tree.xpath("/html/body/ul/li/a/@href"))#三个路径都符合
"""<body>
    <ul>
        <li><a href="http://www.baidu.com">百度</a></li>
        <li><a href="http://www.google.com">谷歌</a></li>
        <li><a href="http://www.sogou.com">搜狗</a></li>
    </ul>
"""
#直接用检查代码里面的copy,xpath
print(tree.xpath('/html/body/div[1]'))

