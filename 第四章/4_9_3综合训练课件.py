#前提无法直接在html里面找到我们需要的东西，需要借助开发者工具，
#1.找到最外面看一下有没有一个叫iframe，网页框架，在一个html中嵌入一个html（"综合训练图片存放\iframe.png"）,
"""
思路：
    1.拿到主页面的页面源代码，找到iframe
    2.从iframe的页面源代码中拿到m3u8文件
    3.下载第一层m3u8文件-->下载第二层m3u8文件（视频顺序1.2）#我们上面拿到的m3u8是第一层
    4.下载视频
    5.第二层，下载密钥进行解密
    6.合并所以ts视频为一个mp4文件
"""
import requests

def get_iframe_src(url):
    resp=requests.get(url)
    print(resp.text)#结果见（ifranme标签）
def main(url):
    #1.拿到主页面的页面源代码，找到iframe对应的url地址
    iframe_src=get_iframe_src(url)
if __name__ == '__main__':
    url="https://www.91kanju.com/vod-play/541-2-1.html"
    main(url)