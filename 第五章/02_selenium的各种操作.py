#有时候报错，多开几个页面#还是用xpath的当前位置吧，不然太容易报错了1.(锁定当前框架之前我们需要做一个事情也就是需要先 使用selenium登录网页，拿到自动化的网页代码)当前定位锁定框架2.其他方式查找位置
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By#common共同的，共享的；常见的，普遍的
from selenium.webdriver.common.keys import Keys
import time

web=Edge()#造个浏览器出来
web.get("http://lagou.com")

#检查复制xpath路径
#找到某个元素，点击它
el=web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a')#格式已经修改为driver.find_element(By., 'xpath地址')详细见重要（查找修改）
el.click()#点击

time.sleep(1)#让浏览器缓一会（一定要的，因为上面代码执行完了（但是网页模拟人为操作很慢，所以导致内容还没刷新出来））
#找到输入框，输入python =>输入回车/点击搜索按钮
#接下来演示回车
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("pyhton",Keys.ENTER)#想要输入键盘上的按钮，我们需要导入一个包from selenium.webdriver.common.keys import Keys
#查找存放数据的位置，进行数据提取
#思路：找到大框架，循环每一个框架拿到我们想要的内容（图片循环框架），将大框架全部全部复制过来
#找到页面中存放数据的所有的<div
time.sleep(5)
li_list=web.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div')#我们找一堆，加个s#//*[@id="jobList"]/div[1]/div[1]路径需要将[1]去掉，因为我们要找第一个，绝对位置，虽然我们前面复制相对位置，但是还是复制一下全部位置看一下，他们之间的关系来对比下面的相对位置怎么写
time.sleep(3)
for li in li_list:
    #然后每一个div，接着往里面寻找#（图片：找我们需要的）
    #job_name=li.find_element(By.XPATH,'./div[1]/div[1]/span/div/div[1]/a'
    job_name=li.find_element(By.ID,'openWinPostion').text#通过这些标签里面的属性查找我们需要的内容#路径也可以用上面那种方法
    # job_price=li.find_element(By.XPATH,'./div[1]/div[1]/span/div/div[2]/span').text
    job_price=li.find_element(By.CLASS_NAME,'money__3Lkgq').text
    print(job_price,job_name)

input("enter")

