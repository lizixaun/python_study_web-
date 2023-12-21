#选择xhr增加数据一般都是，二次请求,（all里面的）
#找问号，问号前面链接，后面参数
#Request URL:
#https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20
import requests
url="https://movie.douban.com/j/chart/top_list?"
#太长了，重新封装,?后面的放到其他地方
#query string parameters（询问因素字符）详细信息在playload，也就是headers旁边那个
#top_list往下拉，对比
"""type: 24
interval_id: 100:90
action: 
start: 20
limit: 20"""
#客户端的鼠标滚轮改变，服务器渲染是html直接把内容打斗到html里面
param={
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start":" 0",
    "limit": "20",
}
#1UA
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
#headres里面有具体信息
resp=requests.get(url=url,params=param,headers=headers)
#request是响应，由发起resp的，它的url是什么
#print(resp.request.url)
#print(resp.text)
#返回空的，说明网站有反扒机制
#1.查看UserAgents
#print(resp.request.headers)
#{'User-Agent':
# 'python-requests/2.31.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
print(resp.json())
#请求关闭
resp.close()


