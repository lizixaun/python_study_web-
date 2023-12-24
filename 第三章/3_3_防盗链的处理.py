#1.开发者工具找视频的链接，复制下来保证可以播放（记住链接）
#但是我们在htlm（原生服务器）里面找不到<video所以这个视频是后期，用js脚本等等生成出来的，而是二次加载
#所以开发者工具是实时的，页面源代码不是实时的
#2.打开开发者工具的network的xrh刷新一下，得到vidoe，然后他的前端有信息，链接对比以下。因为链接是拿到后面进行加工的
#得到结果（第二个地址加首页地址拼接——将中间换掉）
        ##首页地址：                           https://www.pearvideo.com/video_1748691
        ##1地址（可播放）：https://video.pearvideo.com/mp4/short/20220130/cont-1748691-15822443-hd.mp4
        ##2地址：        https://video.pearvideo.com/mp4/short/20220130/1703397073812-15822443-hd.mp4
#------------------------------------------------------------------------------------------------------------
#思路1.拿到contid
#2.拿到videoStatus的返回json.->srcURL
#3.srcURL里面的内容进行修改
#4.下载视频
import requests

url="https://www.pearvideo.com/video_1748691"
conId=url.split("_")[1]#通过_来切割，https://www.pearvideo.com/video为第0个------  1748691为第一个，我们要第一个
#改的原因是因为我们想要爬很多视频，所以要改成一个不是固定的，这样可以方便后面修改
# videStatusurl="https://www.pearvideo.com/videoStatus.jsp?contId=1748691&mrd=0.013562337280739634"#地址2的headers地址
videStatusurl=f"https://www.pearvideo.com/videoStatus.jsp?contId={conId}&mrd=0.013562337280739634"#开始组合
headres={
"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
#防盗链是指：系统会查看你上一个页面。因为我们打开网站是先，打开首页，再加上后面的链接，系统看完发现你的链接是突然出现的就是认为是有问题的(防盗链在user-AG上面)
#也就是溯源，当前本次请求的上一级是谁
# "Referer":"https://www.pearvideo.com/video_1748691"
"Referer":url#两种写法都可以

}
resp=requests.get(url=videStatusurl,headers=headres)
#print(resp.text)#还是显示该文章已下线
dic=resp.json()#用字典的方式拿
srcUrl=dic['videoInfo']['videos']['srcUrl']#看层次结果找我们要的东西
#print(srcUrl)#我们得到链接：https://video.pearvideo.com/mp4/short/20220130/1703401049518-15822443-hd.mp4
#             #视频真实链接：https://video.pearvideo.com/mp4/short/20220130/cont-1748691-15822443-hd.mp4
systemTime=dic['systemTime']#systemTime里面也有我们要的东西
#开始修改
srcUrl=srcUrl.replace(systemTime,f"cont-{conId}")#replace(这部分要换的东西，换成的东西)#f"a{换成}"
# print(srcUrl)
#下载视频
with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)


