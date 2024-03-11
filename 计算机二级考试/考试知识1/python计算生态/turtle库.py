#--------------------基本海龟画图----------
import turtle as t
t.setup(600,600,10,20)#窗口宽度，窗口高度，距离屏幕左边距离，距离屏幕顶部像素

#前进 forward()
#后退 backward()
t.forward(100)
#t.right()#右转
#t.left()#左转
for i in range(4):
    t.forward(100)
    t.left(90)
#-------------画笔状态函数---------------------------------------------------------------------
import turtle as t
t.setup(600,600,10,20)#窗口宽度，窗口高度，距离屏幕左边距离，距离屏幕顶部像素

#设置画笔条的粗细为指定大小
t.pensize(2)
#设置画笔的颜色 t.pencolor((r,g,b))0~1
#t.pencolor("blue")
#t.pencolor((0,0,1))#也是一样的效果，同样是blue

#设置颜色（可以设置画笔和填充颜色）
#t.color(,)#两个参数，第一个参数画笔颜色，第二个填充颜色
t.color("red","blue")

#填充前
#t.begin_fill()

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)

#填充后
t.end_fill()

#箭头隐藏
t.hideturtle()

#箭头展示
t.showturtle()

#在图上写文字
t.write("在画图")
#画笔抬起来
t.penup()
#画笔放下去
t.pendown()
#--------------------------画圆---------------------------
import turtle as t
t.setup(600,600,10,10)

#画图速度
t.speed(2)

#画圆
t.circle(60)#画一个半径为60的圆，第二个参数默认为360.第三个参数steps意思为在圆里面画几步，也就是几边形，3就是三角形
t.circle(60,180)#画一个半径为60，但是只画180的部分（一个圆360度）
t.circle(60,180,steps=6)







