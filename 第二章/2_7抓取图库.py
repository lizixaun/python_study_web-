#1.拿到主页面的源代码，然后提取到子页面的链接地址，href
#2.拿到子页面下载地址
#3.下载图片（这个重要）,为了防止服务器不把我们干掉，加一个time,休息一会
##下载就是：访问图片,将访问图片的content保存到文件中
import time
import re
import requests
url="https://desk.3gbizhi.com/"
heaeds={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
resp=requests.get(url=url,headers=heaeds)
s=resp.text
obj=re.compile(r'<i class="fa-regular fa-heart">.*?<a href="(?P<image>.*?)" class=',re.S)
obj1=re.compile(r'<div class="showcontw mtw dispflex">.*?<a href="(?P<picture>.*?)" class="arrows" target="_blank">',re.S)
its=obj.finditer(s)
for it in its:
    its_url=it.group('image')
    resp = requests.get(url=its_url, headers=heaeds)
    s1 = resp.text
    its1=obj1.finditer(s1)
    for it1 in its1:
        print(it1.group('picture'))
        src=it1.group('picture')#链接
        #访问图片,将访问图片的content保存到文件中
        img_resp=requests.get(src)
        #下载图片
        img_name=src.split("/")[-1]#拿文件url的最好一个/以后的内容做文件名字
        #当然也可以加路径with open(img_name,mode="wb") as f:
        with open("image/"+img_name,mode="wb") as f:#wb写入视频图片，MP3
            f.write(img_resp.content)
        print("over",img_name)
        time.sleep(1)
print("overall")

