from selenium import webdriver

# 创建 Chrome WebDriver
web = webdriver.Chrome()

# 执行 Chrome DevTools Protocol 命令
web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    window.navigator.webdriver = undefined
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
})

# 在这里使用 web.get() 加载你要访问的网页
web.get("https://example.com")  # 将网址替换为你要访问的实际网址
