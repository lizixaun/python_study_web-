#源代码没有结果，我们需要network，很麻烦（要解密什么的），所以最好就是我们直接连接到浏览器，让浏览器帮我们完成各种复杂的操作，我们只接收结果
#selenium:自动化测试工具
#可以：打开浏览器像人一样去操作浏览器
#程序员可以从selenium中直接提取网页上的各种信息
#环境搭建：
#   pip install selenium -i 清华源
#   下载浏览器驱动：https://npm.taobao.org/mirrors/chromedriver
#我们大部分都是用eage所以，特别讲一下eage的驱动下载方式，我放在OneNote里面
#       把解压缩的浏览器驱动chromedriver放在python解释器所在的文件夹（图片：下载到解释器的位置）或者直接代码（python解释器文件夹位置.py）
#让selenium启动浏览器
from selenium.webdriver import Edge
#1.创建浏览器对象
web = Edge()
#2.打开一个网站
web.get("http://www.baidu.com")
# input("按下 Enter 键以关闭程序...")  # 程序将在按下 Enter 后继续执行并关闭,加一个input，可以让软件不自动关闭
print(web.title)

