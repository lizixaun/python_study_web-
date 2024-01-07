#我们要干的事情参考（图片：初始对象）
# 1. 设计一个类（类比生活中: 设计一张登记表)
class Student:
    name=None
    gender=None
    nation=None
#2.创建一个对象(类比生活中:打印一张登记表)
stu_1=Student()
#3.对象属性进行赋值(类比生活中:填表单)
stu_1.name="lizixuan"
stu_1.nation="中国"
stu_1.gender="帅哥"
#4.获取对象中记录的信息（看表格）
print(stu_1.nation)
print(stu_1.gender)
print(stu_1.name)

