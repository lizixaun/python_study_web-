from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options #option选择
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
#准备好参数配置
opt=Options()
opt.add_argument("--headless")#无头#argument争论，争吵；论据，理由,论点
opt.add_argument("--disbale-gpu")#显卡不显示gpu,disbale：丧失能力
web=Edge(options=opt)#吧参数配置设置到浏览器中
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")
"""
#下拉列表，css动态的类似下拉列表的（图片：下拉列表与css动态区别.png），下拉列表也叫select标签
#定位到下来列表
sel_el=web.find_element(By.XPATH,'//*[@id="OptionDate"]')
#对元素进行包装，包装成下拉菜单
sel=Select(sel_el)
#让浏览器调整选项（也就是选择年份）
for i in range(len(sel.options)):#循环列表的索引
    sel.select_by_index(i)#包装进行切换的三种模式（图片：三种切换方式）
    time.sleep(2)#每次切换都要等一会
    table=web.find_element(By.XPATH,'//*[@id="WrapInfo"]/div')
    print(table.text)#打印所以的文本信息
    print("-----------------------------")


input("enter")
web.close()"""
time.sleep(2)
#如何拿到页面代码Elements(经过数据加载以及js脚本执行之后的结果的html内容)
print(web.page_source)