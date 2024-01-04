from selenium.webdriver import Edge
import time
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains#事件链
#初始化超级鹰，直接复制
chaojiying = Chaojiying_Client('3105489241', '047973lzx', '914467')#第一行超级鹰
#如果你的程序被识别到怎么办？（在控制台输入window.navigator.webdriver图片：识别情况）结果为true，自动台为true,普通为flase
#1.chrome的版本号如果小于88     ：在你启动浏览器的时候（此时没有加载如何网页内容），向页面嵌入jS代码，去掉webdriver
# from selenium import webdriver
#
# # 创建 Chrome WebDriver
# web = webdriver.Chrome()
#
# # 执行 Chrome DevTools Protocol 命令
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": """
#     window.navigator.webdriver = undefined
#         Object.defineProperty(navigator, 'webdriver', {
#             get: () => undefined
#         })
#     """
# })
#2.chrome的版本号大于88#加上之后拖过去就很简单了
"""from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled') 

web = webdriver.Edge(options=options)
"""
web=Edge()
web.get('https://kyfw.12306.cn/otn/resources/login.html')
input('enter')
#下面的代码，我们是处理图片识别的，但是现在版本的12306没有图片识别

verify_img_element=web.find_element(By.XPATH,"图片位置")
#用超级鹰去识别验证码
dic=chaojiying.PostPic(verify_img_element.screenshot_as_png, 9004)#第二行超级鹰
result=dic['pic_str']#x1,y1|x2,y2|x3y3(返回这样的坐标)
# print(result)
rs_list=result.split("|")#比如说得到49,73|184,142，我们按照|来切开
for rs in rs_list:#x1,y1
    p_temp=rs.split(',')#再根据,号切割
    x=int(p_temp[0])    #我们这边拿到的是字符串，也就是这样的“49”,我们要将数据处理为49数字，加上int,就变为数据了
    y=int(p_temp[1])
    #我们接下来需要将鼠标移动到某个位置,然后进行点击（所以也是一个事件链）
    #醒来 -->掀开被子 --->坐起来-->穿鞋子(前面可以认为是晚上 睡觉前定义好怎么起床)---->开始执行(.perfrom)
    # ActionChains(web)事件链捆绑在web身上，          #路径                        #.perfrom提交
    ActionChains(web).move_to_element_with_offset(verify_img_element,x,y).click().perform()#move_to_element_with_offset移动到某一个节点，这个节点带着偏移量去移动（就是移动到这个节点，之后在当前节点上做顶点坐标，这个就叫偏移量）
#输入用户名或者密码                                                                  #perform：演出，表演；执行，履行（尤指复杂的任务或行动）；运行
"""
太简单了，就不写了
"""
time.sleep(5)
#滑块处理（图片：滑块处理）----系统检测出来是自动检测控制。（解决方法，让系统认为我们不是自动工具）
#接下来就拖拽问题了（图片：识别情况）#现在12306已经取消拖拽了接下来的代码为跟课程演示
btn=web.find_element(By.XPATH,'//*[@id="nc_1_nlz"]')#按钮位置
ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()#drag抓起来，drop放下,（得到坐标位置截图在：位置截图处理）.#横坐标300，纵坐标，不移动（因为是从坐边拖到右边去）