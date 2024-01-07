#目的就是为了，方便，如果重新写一个class就会很麻烦，在原来的继承上改改就简单（图片：苹果案例）
#格式（图片：继承理解）
#class 类名（父类名）：#多继承，就多写几个参数，不演示了
#    想补充的新内容
class phone:
    IMEI=None   #序列号
    producer="HM"#参商
    def call_by_4g(self):
        print("四G通话")
class phone2022(phone):
    face_id="10001" #面部识别
    IMEI=1#复写，对父类已有的方法在自己这边重新定义
    def call_by_5g(self):
        print("5g通话")
phone=phone2022()
print(phone.producer)#HM