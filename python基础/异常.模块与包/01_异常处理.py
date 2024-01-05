#基本语法:捕获所有异常一共有2种
"""
第一种
try:
    可能发生错误的代码
except:#除了....之外，把，，，排除在外
    如果出现问题执行代码"""
"""try:
    f=open('a.text',mode="r")
except:
    f=open('a.text',mode="w")
"""
#第二种
"""try:
    
except Exception as e:
    print(e)
"""
#____________________________________________________________________________________________________________________
#捕获指定的异常（异常有很多类型-其实没啥用）
"""try:
    print(name)
except NameError  as e:
    print("出现变量未定义的异常")
    print(e)#name 'name' is not defined
    """
#捕获多个异常
"""try:
    1/0
    print(name)
except (NameError,ZeroDivisionError)as e:
    print("出现了变量未定义，或者除以0的异常处理")"""