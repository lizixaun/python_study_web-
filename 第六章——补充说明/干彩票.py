#获取csv文件也是，第一列叫index,后面叫values。使用方法直接(内容.index/内容.values)如print(blue_ball_count.index)
#df.loc[:,1:5]需要数据怎么取得
#————————————————————————————————————————————————————————————————————————————————————————————————————
#pip install matplotlib
#pip install pandas
import pandas as pd#做数据处理和分析，清洗
import matplotlib.pyplot as plt#用来做可视化的工具 ->能把数据变成图表    #mapplotlib画图，Python 和 plot 两个词的结合。Python 是这个绘图工具库的编程语言，而 plot 则指的是绘制图表或图形的行为
import numpy as np#用来做数据处理的
#pip install --upgrade matplotlib更新一下画图工具

#写数据,由于没有数据，所以我们随便自己爬一个网站
"""from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
web=Edge()
web.get("https://datachart.500.com/ssq/history/history.shtml")
text=web.find_element(By.XPATH,'//*[@id="tdata"]').text
with open("data_彩票.csv",mode="w",encoding="utf-8")as f:
    f.write(text)"""
#csv:文件的行列关系是从0开始的，但是由于我们下面代码是将0列做为索引。可以将csv文件的理解为（图片：csv文件的理解.png）
#引入数据                       处理表头       处理列  索引列：column
df=pd.read_csv("data.csv",header=None,index_col=0)#数据处理，首先我们看 一下数据的格式（图片）#处理内容1：我们的第一行被csv文件做为，表头了 2：我们这第一列，希望是彩票号
# print(df)
#把红球的号码拿出来
#所以我们这个
#列：从1到5拿到数据
#行：所有的行的数据都是想要的数据
#loc[]前面行，后面列，要几行就以索引的方式拿数据。比如拿全部[:,:]
red_ball=df.loc[:,1:5]
# print(red_ball)#大概我们下面这样的二维数据
"""        1   2   3   4   5
0                        
24002   4   9  10  17  19
24001   3   7  16  26  27
23151   1  15  16  20  25
23150  10  17  25  26  30
23149   2  10  19  24  26
23148   3   5   7   9  19
23147   5   6  14  16  19
23146   2   3   6  11  20
23145   7  10  21  22  23
"""

#把蓝球的号码拿出来
blue_ball=df.loc[:,6]#只写个6，就是只拿第六列
#统计每一个号码出现的次数
#处理一下一维数据                        .values拿到所有的数据 flatten数据变为一维的（也就是变成一个列表）         flatten变平；把…弄平；摧毁
red_ball_count=pd.value_counts(red_ball.values.flatten())#pandas帮我们统计内容个数，本来里面只需写red_ball就可以了，但是这个函数只可以统计一维的数据，我们这个数据有行有列，属于二维数据#处理一下
# print(red_ball_count)#得到每一个数字出现的次数
#蓝球只有一列，虽然是列但是也是一维的所有，不需要额外处理一次
blue_ball_count=pd.value_counts(blue_ball)
# print(blue_ball_count)
"""这个就是二维的表格直接输出出来的样子
[[1,2,3],
[3,5,7]]"""
#可视化展示 ->制作成图表
#subplot创建子图；情节副线
"""fig,ax=plt.subplots(2,1)#一次创建很多个图标#一个蓝，一个红.上面一个，下面一个所有是两行一列
# print(ax)#图表在这里
#                       美化内容可以看一下红球得到的数据（print(red_ball_count)）(图片:美化前看一下需要美化什么内容)
#用饼图来展示             美化一下：label每一个数据写出对应的号码#radius半径#wedge翻译过来即三角木，楔子，即表示饼图中的每一块儿(图片解释：楔子解释将扇形打入木头)(图片得到效果楔子改变后面的效果.png)，如果想把图表放一起直接改成一张图就可以
ax[0].pie(red_ball_count,labels=red_ball_count.index,radius=1,wedgeprops={"width":0.3})#0代表第一个图表，画一个饼图，画饼图得有数据所以将红球的数据丢给它
ax[1].pie(blue_ball_count,labels=blue_ball_count.index,radius=0.5,wedgeprops={"width":0.2})
"""
colors = ['#FF5733', '#66CCCC', '#FFD700', '#8A2BE2', '#32CD32']  # 定义一个颜色列表，可以根据需要添加更多颜色
#如果就画一张图片就不需要fig,ax=plt.subplots(2,1)来接收参数了，直接用plt来直接画                  颜色引入np的random选择colors中的颜色，一共需要的个数次选择颜色
plt.pie(red_ball_count,labels=red_ball_count.index,radius=1,wedgeprops={"width":0.3},colors=np.random.choice(colors,len(red_ball_count)))
plt.pie(blue_ball_count,labels=blue_ball_count.index,radius=0.5,wedgeprops={"width":0.2})
plt.show()#图表展示一下
