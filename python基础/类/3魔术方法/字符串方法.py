#快速得到结果
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Student{self.name}{self.age}"
stu=Student("周杰伦",31)
print(stu)