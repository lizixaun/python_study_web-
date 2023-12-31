# 1.找到未加密的参数（post才有加密）       #都是window.asrsea（参数，xxx,xxx,xxx）
# 2.想办法把参数进行加密(必须参考网易的逻辑)， paramsencText，encSecKey=> encSecKey
#3， 请求到网易。 拿到评论信息
# 需要安装pycrypto:from Crypto.Cipher import AES
#pip install pycrypto
from base64 import b64encode
import requests
import json
from Crypto.Cipher import AES
url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token=ce24f899914b2aa549183800105e8bfd"
# 请求方式是POST
data={
"csrf_token": "ce24f899914b2aa549183800105e8bfd",
"cursor": "-1",
"offset": "0",
"orderType": "1",
"pageNo": "1",
"pageSize": "20",
"rid": "R_SO_4_2111993259",
"threadId": "R_SO_4_2111993259"
}
#服务于d的
f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g="0CoJUm6Qyw8W8jud"
e="010001"
i="1QMLVDkXuLIq28hR"#手动固定的->人家函数中是随机的
def get_encSeckey():#由于i是固定的，那么encSeckey就是固定的，c()函数的结果就是固定的
    return "8d4de59ff4bfbd2d805e0ef83670c2c3c27a4f87f5072c98db8550fd723a2f94d958b4ca8bd97a688c5bb1ff150d0f27f9ea79c46c64201b35746bea0b11b24acda60c9fa896c81bd718c67075ce725325caa2306b75641e4c387420cdd5cb6f79ff7a3e7aaf9fea4d8a713c2877cef52b204e02ed6fb9639bae34a4ec467fc0"
def get_params(data):#默认这里接收到的就是字符串
    first=enc_params(data,g)
    second=enc_params(first,i)
    return second   #返回的就是params,因为得到e,e就是a，a就是要加密的nr
def to_16(data):
    pad=16-len(data) %16
    data +=chr(pad)*pad
    return data
def enc_params(data,key):#加密过程
    iv="0102030405060708"
    data=to_16(data)
    aes=AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC)#创建加密器
    bs=aes.encrypt(data.encode("utf-8"))#加密，加密的内容的长度必须是16的倍数
    return str(b64encode(bs),"utf-8")#转化为字符串返回
#处理加密过程
"""
function a(a = 16) { // 随机的16位字符串
    var d, e, b = "abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1) { // 循环16次
        e = Math.random() * b.length; // 随机数 1.234
        e = Math.floor(e); // 取整 1
        c += b.charAt(e); // 去字符串中的xxx位置 b
    }
    return c;
}

function b(a, b) {              // a是要加密的内容，b是秘钥
    var c = CryptoJS.enc.Utf8.parse(b)  //b是秘钥
    , d = CryptoJS.enc.Utf8.parse("0102030405060708"),
        e = CryptoJS.enc.Utf8.parse(a); // e是数据
    var f = CryptoJS.AES.encrypt(e, c, { // c 加密的秘钥
        iv: d, // 偏移量
        mode: CryptoJS.mode.CBC // 模式: cbc
    });
    return f.toString();
}

function c(a, b, c) { // c里面不产生随机数
    var d, e;
    setMaxDigits(131);
    d = new RSAKeyPair(b,"",c);
    e = encryptedString(d, a);
}

function d(d, e, f, g) { // d:数据，e: 010001，f: 很长，g: 0CoJUm6Qyw8W8jud
    var h = {}  //空对象
    , i = a(16); // i就是一个16位的随机值，把i设置成定值
    h.encText = b(d, g); // g秘钥
    h.encText = b(h.encText, i); // 返回的就是params，i也是秘钥   
    h.encSecKey = c(i, e, f), //得到的就是encSecKey，e和f是定死的，如果此时我们把i固定，得到的key一定是固定的
    // 两次加密: 数据+g => b => 第一次加密+i => b = params
}

"""
#发送请求，得到评论结果
resp=requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSeckey()
})
print(resp.text)