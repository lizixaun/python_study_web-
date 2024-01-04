"""#递归：函数自己调用自己
def func():
    print("1")
    func()
#函数一个功能，就像下面，这个约会功能
def yue():
    print("1.登录陌陌")
    print("2.找人")
    print("3.出来约")
#sys模块：存放一些python解释器里面的一些常量

"""
"""import sys
print(sys.getrecursionlimit())#1000
sys.setrecursionlimit(5000)#设置
#global将全局变量拽到局部变量里面去,可以改结果，如果不拽进来的话，直接改会报错
i=0"""
"""def func():
    global i    #global全球的，全世界的；全面的，整体的；（计算机）全局的；球形的
    print(i)
    i+=1
    func()"""
#递归的应用
#数的遍历 -> 从根节点找到子节点，把每一个子节点当成根节点继续寻找
#我们操作系统的文件夹系统就是一个树形结构
#使用递归来遍历a这个文件夹 ->拿到a中的每一个文件和文件夹的名字（文件夹样子）

#病毒
#使用代码查看每一个文件的名字：思路1：循环外面一层2.循环时加上地址查看是不是文件。如果是那么就直接递归，不是直接打印
#注意路径拼接
import os #我们需要使用os模块来打开
#函数接收一个参数，把文件夹的地址给它
def func(path,layer):#路径          #但是不好看，所以我们需要在递归前面加上一个层，显示出不同文件夹之间的缩进
    #1.打开文件夹 ——>拿里面的文件名字
    lst=os.listdir(path)
    # print(lst)
    for name in lst:#拿到每一个名字    #a/c
        #2.判断name对位的文件是文件夹还是文件
        #获取到文件所在的路径，（拼起来就可以了）
        real_path=os.path.join(path,name)
        if os.path.isdir(real_path):#判断是否是文件夹，需要把文件路径扔进去
            #发现是文件夹了，直接递归，再来一次
            print("|--"*layer+name)
            func(real_path,layer+1)#递归的路口   #改变层
        else:
            print("|--"*layer+name)
            # open(real_path,mode="w").write("1")#不要跑，这个是病毒，跑完这个东西就没了
func("a",1)

