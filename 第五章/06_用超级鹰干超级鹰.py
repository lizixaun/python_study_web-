#该文章结合chaojiying.py一起观看
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
#第一次使用自己的模块#from 文件名 import 模块名
from chaojiying import Chaojiying_Client#误报，直接将文件夹，标记成sources root(资源根)
import time
web=Edge()
web.get("https://www.chaojiying.com/user/login/")
time.sleep(1)
#处理验证码
img=web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png#screenshot截屏成png
chaojiying = Chaojiying_Client('3105489241', '047973lzx', '914467')
dic=chaojiying.PostPic(img, 1902)
#我们运行chaojiyinf得到{'err_no': 0, 'err_str': 'OK', 'pic_id': '1237420061274780001', 'pic_str': '7261', 'md5': 'b73789916ad1ab81bcd64e05f7ef76be'}
#我们需要pic_str里面的内容
verify=dic['pic_str']
#向页面中填入用户名，密码 ，验证码
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('3105489241')
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('047973lzx')
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify)
time.sleep(5)
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

#点击登入






input("enter")