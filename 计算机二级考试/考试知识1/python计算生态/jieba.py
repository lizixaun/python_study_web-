import jieba#中文分词
ls=jieba.lcut("国家计算机二级python学科")#['国家', '计算机', '二级', 'python', '学科']#精确模式，返回一个列表类型
print(ls)
jieba.add_word("python学科")#向结巴字典再加上新词（因为结巴有字典来分词，加上之后就可以划分更好了）
ls=jieba.lcut("国家计算机二级python学科")
print(ls)#['国家', '计算机', '二级', 'python学科']
