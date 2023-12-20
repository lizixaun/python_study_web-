from urllib.request import urlopen

url = "https://home.firefoxchina.cn/?from=extra_start"

# 打开 URL
resp = urlopen(url)
content = resp.read().decode("utf-8")
print(content)  # 打印内容

# 将内容写入文件
with open("firefox1.html", mode="w", encoding="utf-8") as f:
    f.write(content)

print("完成")

