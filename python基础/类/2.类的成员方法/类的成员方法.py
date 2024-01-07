#类中定义的属性(变量)，我们称之为:成员变量
# 类中定义的行为(函数)，我们称之为:成员方法。也直接叫方法也是一样的
#在方法里面括号里面必须写self，为了我们下面，如果要在方法里面调用函数那么就self.函数。不然直接写个，比如说：我的名字是{name}，计算机无法理解
#调用的时候，不用管他
#定义一个带有方法的类
class Student:
    name=None
    def say_hi(self):
        print(f"大家好,我是{self.name}")
#使用类
stu=Student()
stu.name="lizixuan"
stu.say_hi()