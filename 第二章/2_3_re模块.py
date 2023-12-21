import re
#findall：匹配字符串里面所以的符合正则的内容
#lst=re.findall(r"\d+","我的电话号码是：100，你的电话号码10086")
#print(lst)
#finditer:匹配字符串里面所以的内容返回迭代器，拿到内容.group
#it=re.finditer(r"\d+","我的电话号码是：100，你的电话号码10065")
#for i in  it:
    #print(i)
#<re.Match object; span=(8, 11), match='100'>
#<re.Match object; span=(18, 23), match='10065'>
#    print(i.group())
#search返回的结果是match对象，拿数据需要.group
#search,找到一个结果就返回
##print(s.group())
#从头开始匹配默认跟加个^
#s=re.match(r"\d+","我的电话号码是：100，你的电话号码10065")
#print(s.group())
##预加载正则表达式
##提起放那边方便
#obj=re.compile(r"\d+")
#ret=obj.finditer()
#for it  in ret:
#    print()
s = """
<div class='西游记'><span id='10010'>中国联通</span></div>
<div class='西游'><span id='0010'>中国联</span></div>
"""
#re.S:让.*?可以 匹配换行符，不会断掉
#obj=re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>",re.S)
#result=ret=obj.finditer(s)
#for it in result:
#    print(it.group())
#匹配内容里面的我们要的
#前面加上（?P<随便取个名字>正则表达式）

obj=re.compile(r"<div class='(?P<wahaha>.*?)'><span id='\d+'>.*?</span></div>",re.S)
result=obj.finditer(s)
for it in result:
    print(it.group("wahaha"))