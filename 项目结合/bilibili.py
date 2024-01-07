#第二种找到视频的方式，不需要解密1.由于加密后的视频出现的里面数字的mp4前面的数字是一样的，直接在all里面搜索，找到其中一个最特别的这个里面有详细的mp4,与audiio就是视频加载的url
#audio音频，mp4视频bilibili的音频视频分开的
#video视频，分开的
#高清就是hight=1080
import requests
url="https://s1.hdslb.com/bfs/seed/jinkela/short/cols/iframe.html"
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
"Cookie":"buvid3=E1EF725A-1D01-7FE1-79D4-64BCCF4779A733917infoc; b_nut=1697533933; _uuid=4E857B98-23D8-7597-4B10F-86C932CD936534022infoc; buvid4=CCE92061-B325-3030-F02E-F90FE69F645735630-023101717-psRAQT9gZx5e%2BJI6L%2FWwuA%3D%3D; CURRENT_FNVAL=4048; rpdid=|(J|)YYkmkll0J'uYmm~kuRkY; PVID=1; enable_web_push=DISABLE; home_feed_column=4; header_theme_version=CLOSE; b_lsid=1A3DC7108_18CDECB7F7E; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; browser_resolution=1369-664; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDQ4MDQxMzIsImlhdCI6MTcwNDU0NDg3MiwicGx0IjotMX0.RKGG3ZsC9nUS5iK-MieEA6t5mMTZ7_3cXQ82MfmLN44; bili_ticket_expires=1704804072; fingerprint=053b70f5d4d5546a6b72214f584916b1; buvid_fp_plain=undefined; SESSDATA=ede3fd51%2C1720097257%2C5e74f%2A12CjDVFogBi6loRofMBavBQSKbOxA5Z032MU9PVVQ6mXcEYa07LcNI5oHVfh15X2vTqn0SVm5FcERTQU1mZ0oxaW9vQm84aFBTd2VnUGVWWUFlNHpmYTgxRDgwWlZWODU1X09rbXVyMU1jTVRkeDhfVzczeWRKdnNaM0dYbjVLbVpvUUlwbHh2WHVBIIEC; bili_jct=9dafec0332f390a626905accf1615629; DedeUserID=3493127048399714; DedeUserID__ckMd5=579232b61cb5f0d1;"}
rep=requests.get(url=url,headers=headers)
bilibili_content=rep.text
print(bilibili_content)



