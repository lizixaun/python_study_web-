url = "https://example.com/sample.ts"

with open("output.mp3", mode="wb") as f:
    url_bytes = url.encode('utf-8')  # 将字符串转换为字节类型
    f.write(url_bytes)  # 将字节数据写入文件
