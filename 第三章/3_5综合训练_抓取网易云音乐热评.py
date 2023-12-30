#页面源代码与框架源代码，就是两套代码，框架加进去的
#看不到页面源代码，与框架源代码里面有我们需要的东西，直接f12，抓包network的xhr里面的前端preview找评论comment单词评论的意思
#1.找到未加密的参数（post才有加密）       #都是window.asrsea（参数，xxx,xxx,xxx）
#2.想办法把参数进行加密（必须参考网易的逻辑），params->encText，encSecKey->encSeckey
#3.请求到网易，拿到评论信息
# url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token=ce24f899914b2aa549183800105e8bfdhttps://music.163.com/weapi/comment/resource/comments/get?csrf_token=ce24f899914b2aa549183800105e8bfd"
import json

import requests

url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="#模拟未登录状态
#安装pycrypto,或者安装pip install pycryptodome两个库效果差不多
from Crypto.Cipher import AES
from base64 import b64encode#得到字节序列对象，加密之后，得到的东西计算机看不懂，所以改成字节序列对象

#请求方式post
#====================================================================================
#详细过程
#1.点击在前端旁边lnitiator（由用于查看执行请求的过程），call stack的一个栈里面写了js脚本的执行过程（从下往上）
#2.点击最上面链接，也就是最后一次执行的链接，然后点框框。（改成正常我们看的舒服的）
#3.找send(data)【这样的：this.tt3x.send(gA0x.data)】做一个断点，断点设置就是在本行的最左边点击一下跟c语言一样
#4.再次刷新，由于断点过，代码会在断点前停下来，断点前的信息将会显示在右边框的scope里面的local里面，看request在哪里就点开哪一个
#5.这里的url是（/weapi/cdns?csrf_token=ce24f899914b2aa549183800105e8bfd）不是我们想要的，我们想要get的东西也就是上面的那个
#get的东西（url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token=），
#6.就是点击播放建，放开我们进行下次拦截，直到我们得到我们想要的get结尾的url
#就是这玩意(https://music.163.com/weapi/comment/resource/comments/get?csrf_token=ce24f899914b2aa549183800105e8bfd"）
#我们的data此时已经被加密（data "params=4iPRPLg4P7NEQqKhAbR5yH1U%2Bd1wX2cq5m2M940N2bnyaRlEqIO0H5GnmzQVSfhWrEqrg2a50pjRtIfkCh68KDsIdcdxpLQxMBohqlJZnzBvvkc%2BI82h8ZWPVx3G9g8l2HnwBCRSWKoZ8eFSV%2B3VLTSBiA8qRhAf53%2B1EKy45sVt9M3aLhB1ze4RwF49k5a%2Bsza4%2FEk0YYj9zjpjUSaW8Dv7ah3vyqezfYJKBgQdZPJ%2FzPL5BD9W2uadsrvTDhWsuErpbMvRyvUgIAndQx14FTzgIz5ioyCDhSvu2btLY%2FGdvRVqG3hxfPH%2FrC9vf%2Bw9PmNpDAKfXyqwNBzfy2p55h5pYM8A4AvYUadJrDD1w7g%3D&encSecKey=124ff0929ac238e0511fe2b605039fc02acac780a75c6ce2f5403d5f0a46b658a949dca4cf80d4eed62b824296b22de44b5e9ab09cd86d546fffd003efbbe6ce6e5a0b7996a25e7bd1de1a053582f7853229faff05585d05ae0d3a22ec985851953612ceccfb3308032f2972ef11950c1939c2b779d4b71bf1a98fbc881e0f1b"）
#7.因为url是一样的，所以是得到同一个东西也就是评论。看local下面我们的名字:ef9,看左边的代码找上一个data是怎么被加密的
#看右边的call stall里面是js脚本倒数第二部，我们看一下是不是这个时候被加密的，用上面方法看一下程序有没有还被加密，直到找到未加密的，就是data比较短
#也就是说程序在anonymous后面开始被加密，然后回到被加密的那一步，此时我们已经找到被加密的这一步了
#8.在这个函数这个，设置断点，然后将之前的断点给去掉，breakpoint那里，重新点播放键，再刷新页面，然后看请求里面的东西类似这样的（X9O: "/api/cdns"）
#跟我们没关系，然后点击播放键，找一个get在最后的（X9O: "https://music.163.com/api/comment/resource/comments/get"）这个是获取评论的url看data有没有问题，然后点击播放旁边的那个
#将断点往下拉，我们看data是哪一步开始变的，直到（ var bVi8a = window.asrsea(JSON.stringify(i9b), bsu7n(["流泪", "强"]), bsu7n(Xo2x.md), bsu7n(["爱心",）这一行我们发现data变了。
#快走的方法：上面的断点不去掉，不然还得重新断点，（今天就是没看清楚断的我命快没了），下面再段一个，播放完，再把上面那个断点去掉。
#找加密的那一步，我们这边加密这一步是将。
#怎么加密的我们讲一下（下面是html的样子）：i9b是参数，参数给（）里面传进去，跑出来一个叫bvi8a的东西。bvi8a有两个东西分别是encSeckey,和encText，e9f被赋值成bVi8a.encText， bVi8a.encSecKey，也就是说bvi8a把两个东西塞给了data用于加密。(data里面是有params与encSeckey的)
# 所以我们要找的params实际上就是encText,要找的encSeckey实际上就是encSeckey,我们现在就可以回到开头了
#-------------------------------------------------------------------------------------------------------------------------------
#var bVi8a = window.asrsea(JSON.stringify(i9b), bsu7n(["流泪", "强"]), bsu7n(Xo2x.md), bsu7n(["爱心", "女孩", "惊恐", "大笑"]));
#             e9f.data = j9a.cr9i({
#                 params: bVi8a.encText,
#                 encSecKey: bVi8a.encSecKey
#-------------------------------------------------------------------------------------------------------------------------------------------------
#我们将我们知道的参数复制出来,请求方式post，真实参数
data={
"csrf_token": "ce24f899914b2aa549183800105e8bfd",
"cursor": "-1",
"offset": "0",
"orderType": "1",
"pageNo": "1",
"pageSize": "20",
"rid": "R_SO_4_2096798000",
"threadId": "R_SO_4_2096798000"
}
#2加密过程。解决方法就是将加密的那个前头，复制查找一下（window.asrsea），然后找到另外一个也就是 window.asrsea = d,找前头看一下这个d是怎么操作的(图在E:\study_web\第三章\综合训练\第二次断点\查找编码过程需要的部分.png)
'''
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {                                
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
'''
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"
e="010001"
#                                                      function d(d, e, f, g)d：数据   e:010001    f:很长，我们起一个变量为f， g:'0CoJUm6Qyw8W8jud'
#现在返回去看我们需要什么参数            var bVi8a = window.asrsea(JSON.stringify(i9b), bsu7n(["流泪", "强"]), bsu7n(Xo2x.md), bsu7n(["爱心", "女孩", "惊恐", "大笑"]));
#第一个参数是                                                        这个i9b也就是我们上面1的实参data（看82行）
#第二个参数我们将他复制 bsu7n(["流泪", "强"])到console(控制台)得到一个数字可以看图我们得到这个e的值是个固定的010001
#第三个参数重复上面的步骤bsu7n(Xo2x.md)得到（'00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'）
#第四个参数也是定值，我们bsu7n(["爱心", "女孩", "惊恐", "大笑"])得到：'0CoJUm6Qyw8W8jud'
#所以我们得知除了d以外其他玩样是定死的（f,g,e）
#现在我们可以开始看函数function d(d, e, f, g)的内部了
#《函数每一行过程理解》
# function d(d, e, f, g) {
#         var h = {}                    #空对象
#           , i = a(16);                #我们这边可以看到这个a其实是上面这个东西，我们来到第100行，也就是（function a(a)，下面为我们再次复制一次用以，讲解代码 #a函数结束之后我们得到一个结果这个i就是等于16位随机值
#         h.encText = b(d, g),   #后面四行修改写法#接下来，讲解一下这个代码，执行b函数，得到encText
#         h.encText = b(h.encText, i),#然后将得到的params，和前面这个随机码丢到这个函数里面，然后再返回这个h（return h）
#         h.encSecKey = c(i, e, f), #得到的就是encSecKey  《def get_encSeckey():》                       #e,f是定死的i是随机的，c会产生变化只会在i身上，如果把i固定，那么c也会得到一个固定的值（前提是我们这个c里面不产生随机数，我们可以看c干了什么有没有
#         产生随机数），所以我们把i设置为固定的，方法就是设置断点得到i。

#         下面是我们要怎么得到encSecKey的具体过程function C（下面）

#         return h
#     }
# function a(a) {                                   #a=16                               #a函数就是产生16个随机的字符串
#         var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
#         for (d = 0; a > d; d += 1)                #也就是让d从0数到15，循环16次  #举个例子----#
#             e = Math.random() * b.length,         #随机数                             ----#随机数为1.23
#             e = Math.floor(e),                    #取整                              -----#取整为1
#             c += b.charAt(e);                     #取字符串中的xxx位置                  ----#所以取字符串中的位置为1的数，也就是b,因为循环16次所以最后会出现16个随机的数字
#         return c                                                                          #返回到c里面去，所以这个a函数就是产生16个随机的字符串，为了方便我们放到最上面去100行的位置
#     }
#————————————————————————————————————————————————————————————————————————————————————
 # function c(a, b, c) {        #c太复杂了，直接给他定死
 #        var d, e;
 #        return setMaxDigits(131),
 #        d = new RSAKeyPair(b,"",c),
 #        e = encryptedString(d, a)
 #    }
#我们将断点设置到i后面，最后一个函数前面也就是（图片"E:\study_web\第三章\综合训练\图片理解\得到随机数的断点设置.jpg"）然后得到i数据图片（E:\study_web\第三章\综合训练\图片理解\得到i图片.png）,
i="n1r9sfgIOmxV6ykF"
#然后我们再次设置函数后面再次设置断点（此时fuction已经跑完），前面的断点不要放全部不要放。断点全部留，保证是get不然失效了，又得下一个轮回。视频讲解断点断点要怎么不会跑掉（）
def get_encSeckey():
    return "7fed8e963fc540092cb0d6a6ac89dfeb12cbc0f0e80e098509b61dcc62f35c7b83c8dc230ca220cdfe0201e199d3661a48c19be2b0c81dca548cc9368c141f41c230f2302490a903e37516bdd3da6ed6f2621f408e9bb77350a55f541873cab7577357bbada92dd0d66be54c665f1d88db56dad40efe94090d2138ec90e219b4"
#——————————————————————————————————————————————————————————-----
#接下来就只有剩下两行了，
#         h.encText = b(d, g),
#         h.encText = b(h.encText, i),
#两次加密：
#数据+g(丢给) =>b =>第一次加密结果 +i =>b =params
#我们看一下b干了什么事
#-----------------------------------------------------------------
"""
function b(a, b) {  #a是要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b)  #c跟b是一回事，但是我们不知道c是什么
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")#偏移量
          , e = CryptoJS.enc.Utf8.parse(a)  #e是a的数据
          , f = CryptoJS.AES.encrypt(e, c, {    #AES加密：里面丢了一个e,c,{}.这个三个东西 #c是加密的密钥，往回推b就是加密的密钥
            iv: d,          #偏移量
            mode: CryptoJS.mode.CBC #模式：cbc
        });
        return f.toString()
"""
#         h.encText = b(d, g),   #g是密钥，因为g是b，我们知道g的值
#         h.encText = b(h.encText, i),#i也是密钥
def get_params(data):#因为就这个data是会变的，所以我们就把这个data设置为定值
    first=enc_params(data,g)
    second=enc_params(first,i)
    return second   #返回的就是params,因为得到e,e就是a，a就是要加密的nr
#下面这个代码 需要 搞定function b
def to_16(data):
    pad=16-len(data) %16
    data +=chr(pad)*pad
    return data
def enc_params(data,key):#加密过程
    iv="0102030405060708"
    data=to_16(data)
    #先造一个可以加密的工具arg,也就是argument（自变量）
    aes=AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC)#创建加密器#ctrl+单击#因为本来是字符串但是要字节，所以要.encode("utf-8")，字节就是utf-8
    bs=aes.encrypt(data.encode("utf-8"))#加密，加密内容长度必须是16的倍数
    #加密之后我们需要return f.toString()转化成字符串，但是我们直接bs.decode是不行的，因为decode必须要有“utf-8",但是结果无法被utf-8识别，
    #所以我们需要模块from base64 import b64encode
    return str(b64encode(bs),"utf-8")#再变成字符串
resp=requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSeckey":get_encSeckey()
})
print(resp.text)