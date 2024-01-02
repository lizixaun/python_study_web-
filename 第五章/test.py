from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
web=Edge()
web.get("baidu.com")
a=web.find_element(By.XPATH,"").text
print(a)
input("enter")