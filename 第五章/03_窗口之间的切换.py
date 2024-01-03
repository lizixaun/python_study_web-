import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
web=Edge()
web.get("http://lagou.com")
"""# web.find_element(By.XPATH,)
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="cboxClose"]').click()
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="openWinPostion"]').click()
time.sleep(1)
#如果进入到新窗口中进行提取
#再selenium眼中，新窗口默认是不切换过来的
web.switch_to.window(web.window_handles[-1])#handles--把；柄；控键
#在新窗口中提取内容
job_detail=web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div').text#格式没问题，可能就是数据无法刷新出来，还是用，非绝对位置定位好一点
# print(job_detail)#打印出内容
#关掉子窗口
web.close()
#变更selenium的窗口视角
web.switch_to.window(web.window_handles[0])
"""
#如果页面中遇到iframe怎么处理（一个网页中有：两个网页）
web.get("https://www.91kanju.com/vod-play/541-2-1.html")
#处理iframe的话，必须先拿到iframe，然后切换视角到iframe，再然后才可以拿数据
iframe=web.find_element(By.XPATH,'//*[@id="player_iframe"]')
web.switch_to.frame(iframe)
#接下来可以正常使用了，也就是说，一个网页有多个iframe的时候，我们需要想进去其中一个iframe，告诉系统我们在哪一个里面
web.switch_to.default_content()#iframe切换出来因为外面看起来是一个网页，所以我们需要切换到默认的窗口default:不履行，默认










input("enter")
