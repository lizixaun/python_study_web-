import requests
import re
domain="https://www.dytt89.com/"
#去掉安全验证，
resp=requests.get(domain,verify=False)
resp.encoding='gb2312'#指定字符集
print(resp.text)