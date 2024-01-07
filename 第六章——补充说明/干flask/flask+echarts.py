#web应用程序的；浏览器思路
from flask import Flask,render_template#（计算机文档的）模板；样板，榜样；
import pandas as pd#要使用pandas引入数据
app=Flask(__name__)
@app.route("/")
def show():
    #读取csv文件的内容，发送到页面中就可以了
    #1.需要将数据复制到我们的html文件夹里面
    data=pd.read_csv("数据.csv")
    # print(data)
    data=data.rename(columns={"3":"name","2":"value"})
    #接下来我们需要将数据改为html上面一样的形式    data: [{value: 335, name: 'Direct'},{},{}]
    data=data.to_dict(orient="records")#看to_list文档，里面有写这种格式，需要怎么改#crient朝向，面对，
    print(data)
    return render_template("show.html",data=data)#data数据改完了，丢给前端
if __name__ == '__main__':
    app.run()