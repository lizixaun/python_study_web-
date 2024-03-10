#————————————————————————————————————————————————————-一维数据读写——————————————————————————————————————————————————————
#写
ls=["b","a"]
f=open("a.csv",mode="w",encoding="UTF-8")
s=",".join(ls)
f.write(s)
f.close()
#读
f=open("a.csv",mode="r",encoding="UTF-8")
info=f.read()
f.close()
print(info)#直接读取是字符串##b,a
#如果将文件以，拆开系统自动放到列表中
a=info.split(",")
print(a)#['b', 'a']
#—————————————————————————————————————————————————————————二维数据读写—————————————————————————————————————————————————————————————————
#写
student=[
        ["学号","姓名","性别"],
        ["1","2","3"]
        ]
f=open("a.csv","w")
for i in student:
    f.write(",".join(i)+"\n")
f.close()
#读
f=open("a.csv","r")#打开文件，以读取的方式
#用s=f.read()读取文件内容时，它会将整个文件作为一个字符串返回。因此，在接下来的for循环中，您实际上是在遍历字符串的每个字符，而不是按行遍历文件的内容。
ls=[]
for line in f:
    line=line.strip("\n")
    temp=line.split(",")
    ls.append(temp)
f.close()
print(ls)
