#python里面前两个下划线，后面两个下划线都可以被叫做魔术方法，所以构造方法也可以叫魔术方法-----快速传参（构造方法），快速得结果字符串方法
#一次需要传入很多参数，
#stu_1=Stundet()这一步，就是生活中的打印纸张，我们直接全部填写完身份信息，后面的括号，长的很像我们的函数参数，其实也是可以传参的。需要在类里面，制作一个构造方法
#构造方法的特性1.是会自动执行2.会将参数带到构造方法里面，可以理解为构造方法是类的本体
class Student:

    # name=None
    # age=None          #下面有写，，上面其实可以不写，因为python，定义+赋值可以一步完成，java不行
    def __init__(self,name,age):#当然是方法就得写self
        self.name=name
        self.age=age
stu_1=Student("fananqi","刚满18岁")
print(stu_1.name+stu_1.age)