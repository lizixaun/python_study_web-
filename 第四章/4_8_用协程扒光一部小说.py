#具体步骤1.xrh找得到的headers
#——————————————————————————————————————————————————————————————————————————————————————————————
#1.第一个链接同步操作2.下面链接异步操作
# Request URL:
#http://dushu.baiducom/api/pc/getCatalog?data=["book id":"4306063500")=> 所有章节的内容(名称，cid)
#章节内部的内容
# http://dushu,baidu, com/api/pc/gethapter(ontent?data=("book_id":"4306063500","cid":"4306063500|11348571","r
import requests
