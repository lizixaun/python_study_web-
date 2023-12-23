#cookie就是你给服务器密码，服务器会给你的cookie里面写入一个代码，就是身份卡一个比如说”10086“，后面你再向服务器请求就会带着10086，服务器知道你是谁
#1.登入->得到cookie
#2.带着cookie，去请求到书架url -> 书架上的内容
#必须得把两个操作连在一起
#我们可以使用session进行请求 ->session你可以认为是一连串的请求，并且在这个过程中cookie不会丢失
import requests
#会话，聊天，会记得刚刚我们说过什么
session=requests.session()
data={
    "loginName": "18206009589",
    "password": "047973Lzx"
}
#1.登录
url="https://passport.17k.com/ck/user/login"#在login里面有写
# resp=session.post(url,data=data)#payload里面有data信息
session.post(url,data=data)#将resp去掉，放下面
# print(resp.text)
#print(resp.cookies) #看cookie
#2.拿书架上的数据#preview里面页面源代码，xhr里面找，找到的就是能直接找到书架上的url（在headers里面）
#刚才的那个session里面是有cookies的
resp=session.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919')
# print(resp.text)
print(resp.json())
#----------------------------------------------------------------------------
#也可以方法二
resp=requests.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919",headers={
    'Cookie':'GUID=757c0f18-08fb-4e4b-be5c-cfe9c74f7453; sajssdk_2015_cross_new_user=1; _openId=ow-yN5nV74Ja0F4Hjv8aNPAPIadw; c_channel=0; c_csc=17KH5; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F07%252F87%252F39%252F102743987.jpg-88x88%253Fv%253D1703323758000%26id%3D102743987%26nickname%3D%25E4%25B9%25A6%25E5%258F%258B6Rt8e6QTG%26e%3D1718877101%26s%3D594e96788a12cff4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22102743987%22%2C%22%24device_id%22%3A%2218c95e5ba8412c-0e913da546c285-4c657b58-921600-18c95e5ba85c2d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22757c0f18-08fb-4e4b-be5c-cfe9c74f7453%22%7D'
})
print(resp.text)