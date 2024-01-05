#pip install flask
from flask import Flask,render_template#通过它，返回一个html页面
from flask import request#通过请求拿到数据
#hello world
#创建应用程序
#web应用程序
app=Flask(__name__)
#现在进入网站，404
# #写一个函数来处理浏览器发送过来的请求
# @app.route("/")#当访问到127.0.1：5000/（http://127.0.0.1:5000）就会触发下面这个函数
# def 随便名字():
#     #这里来处理业务逻辑的
#     return "hello world"    #返回的数据->相应
# @app.route("/lizixuan")
# def shoudehao():
#     return "李子煊，大帅哥"


#模板->html
# @app.route("/")
# def index():
#     return render_template("hello.html")#此时会自动找templates文件夹里面的hello.html

# #把一个变量发送到页面
# @app.route("/")
# def index():
#     #字符串
#     s="你好啊"
#     lst=["帅哥煊","学霸煊"]#列表的
#     return render_template("hello.html",jay=s,lst=lst)#动态jay(接收数据)
#----------------------------------------------------------------------------------------------------
#通过一个页面来学习，如何从页面来接收数据
#登录验证
@app.route("/")
def index():
    return render_template("login.html")
@app.route("/longin",methods=["POST"])#默认是get我们需要改为post
def longin():
    #接收到用户名和密码
    #{username:你写的内容 pwd:你写的内容}
    username=request.form.get("username")
    password=request.form.get("pwd")
    if username=="alex" and password=="123":
        return "成功"
    else:
        return render_template("login.html",msg="登入失败")#随便接收一下


if __name__ == '__main__':
    app.run()#启动应用程序->启动一个Flask项目#如果app.run(debug=true)那么就不用重启
