from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
web=Edge()
web.get("https://wenku.csdn.net/answer/247i59i60w#:~:text=%E5%A6%82%E4%BD%95%E4%B8%8B%E8%BD%BDcsdn%E5%8D%9A%E5%AE%A2%201%20%E6%89%93%E5%BC%80%E6%82%A8%E6%83%B3%E8%A6%81%E4%B8%8B%E8%BD%BD%E7%9A%84%E5%8D%9A%E5%AE%A2%E6%96%87%E7%AB%A0%E9%A1%B5%E9%9D%A2%E3%80%82%202%20%E6%8C%89%E4%B8%8B%E5%8A%9F%E8%83%BD%E9%94%AE%20F12%EF%BC%8C%E6%89%93%E5%BC%80%E6%8E%A7%E5%88%B6%E5%8F%B0%E3%80%82%203,%E5%9C%A8%E6%8E%A7%E5%88%B6%E5%8F%B0%E4%B8%AD%EF%BC%8C%E7%B2%98%E8%B4%B4%E4%BB%A5%E4%B8%8B%E4%BB%A3%E7%A0%81%EF%BC%9A%20...%204%20%E6%8C%89%E4%B8%8B%E5%9B%9E%E8%BD%A6%E9%94%AE%E6%89%A7%E8%A1%8C%E4%BB%A3%E7%A0%81%E3%80%82%205%20%E9%80%89%E6%8B%A9%E4%BF%9D%E5%AD%98%EF%BC%8C%E5%8D%B3%E5%8F%AF%E5%BE%97%E5%88%B0%E4%BB%A5%20PDF%20%E6%A0%BC%E5%BC%8F%E4%BF%9D%E5%AD%98%E7%9A%84%E6%96%87%E4%BB%B6%E3%80%82")
a=web.find_element(By.XPATH,'//*[@id="chatgpt-article-detail"]/div[1]/div[1]/div[2]/div[2]/div/div/ol/li[3]/pre/code').text
print(a)
input("enter")