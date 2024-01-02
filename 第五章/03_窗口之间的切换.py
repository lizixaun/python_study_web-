import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
web=Edge()
web.get("http://lagou.com")
# web.find_element(By.XPATH,)
time.sleep(1)
input("enter")
