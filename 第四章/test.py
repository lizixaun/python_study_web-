from http import cookies
from http import client
from urllib import request

# 你提供的 Accept-Encoding 和 Accept-Language 信息
accept_encoding = 'gzip, deflate, br'
accept_language = 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'

# 解析 Accept-Encoding 头信息
parsed_encoding = [encoding.strip() for encoding in accept_encoding.split(',')]
print("Accept-Encoding翻译成中文为：")
for encoding in parsed_encoding:
    if encoding == 'gzip':
        print("gzip（gzip压缩）")
    elif encoding == 'deflate':
        print("deflate（deflate压缩）")
    elif encoding == 'br':
        print("br（Brotli压缩）")

# 解析 Accept-Language 头信息
parsed_languages = [lang.strip() for lang in accept_language.split(',')]
print("\nAccept-Language翻译成中文为：")
for lang in parsed_languages:
    language, _, priority = lang.partition(';')
    print(f"{language} 的优先级为 {priority if priority else '1'}")
