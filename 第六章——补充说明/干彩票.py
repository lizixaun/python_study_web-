#pip install matplotlib
#pip install pandas
import pandas as pd#做数据处理和分析，清洗
import matplotlib.pyplot as plt#用来做可视化的工具 ->能把数据变成图表
#引入数据,由于没有数据，所以我们随便自己爬一个网站
"""from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
web=Edge()
web.get("https://datachart.500.com/ssq/history/history.shtml")
text=web.find_element(By.XPATH,'//*[@id="tdata"]').text
with open("data_彩票.text",mode="w",encoding="utf-8")as f:
    f.write(text)"""