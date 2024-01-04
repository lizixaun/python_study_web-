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