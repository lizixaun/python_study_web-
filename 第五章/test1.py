from selenium.webdriver import Edge
from selenium.webdriver.common.by import By#common共同的，共享的；常见的，普遍的
from selenium.webdriver.common.keys import Keys
import time

web=Edge()#造个浏览器出来
web.get("http://lagou.com")
"""
#检查复制xpath路径
#找到某个元素，点击它
el=web.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div/a[1]')#格式已经修改为driver.find_element(By., 'xpath地址')详细见重要（查找修改）
el.click()#点击
"""
time.sleep(1)

web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("pyhton",Keys.ENTER)

time.sleep(1)
li_list=web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')
for li in li_list:
    job_name=li.find_element(By.ID,'openWinPostion').text
    job_price=li.find_element(By.XPATH,'./div[1]/div[1]/span/div/div[2]/span').text
    print(job_price,job_name)
    print("1")
input("enter")

