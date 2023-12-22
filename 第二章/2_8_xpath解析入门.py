#1.后代写法2.xpath的正则表达式
#xpath 是在xml文档中搜索内容的一门语言
#html是xml的一个子集
#谁抱着谁谁就是谁的父节点,xpath通过节点之间的关系来找的，有点像文件夹
#/book/price
'''
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
    </author>
<book>
'''
#安装lxml模块
#pip install lxml
#pip install lxml -i xxxx如果你需要国内的镜像
#xpath解析
from lxml import etree

xml='''
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>惹了1</nick>
        </div>
        <span>
            <nick>惹了2</nick>
        </span>
    </author>
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
'''

#将内容加载成xml对象
tree=etree.XML(xml)
#tree.xpath()#ok，告诉电脑我要开始使用xpath的功能
#result=tree.xpath("/book")#表示层级关系，第一个/是根节点。结果：[<Element book at 0x1b8a0f754c0>]
#result=tree.xpath("/book/name")#[<Element name at 0x14e8914fbc0>]
#result=tree.xpath("/book/name/text()")#text()拿文本内容，如果不加括号的话就变成，找子节点了，我们要找内容
#result=tree.xpath("/book/author/nick/text()")
#result=tree.xpath("/book/author/div/nick/text()")想要一个文件夹下面的子节点跟子子节点全部出来
result=tree.xpath("/book/author//nick/text()")#['周大强', '周芷若', '周杰伦', '蔡依林', '惹了', '惹了']#后代全部出来，一个路径给例子
#author/div/nick
#author/spn/nick除了中间的位置全部一样的，有点像正则表达式里面的一个点
result=tree.xpath("book/author/*/nick")#*任意节点



print(result)