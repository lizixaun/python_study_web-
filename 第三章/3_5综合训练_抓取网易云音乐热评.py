#页面源代码与框架源代码，就是两套代码，框架加进去的
#看不到页面源代码，与框架源代码里面有我们需要的东西，直接f12，抓包network的xhr里面的前端preview找评论comment单词评论的意思
#1.找到未加密的参数（post才有加密）
#2.想办法把参数进行加密（必须参考网易的逻辑），params，encSecKey
#3.请求到网易，拿到评论信息
# url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token=ce24f899914b2aa549183800105e8bfdhttps://music.163.com/weapi/comment/resource/comments/get?csrf_token=ce24f899914b2aa549183800105e8bfd"
url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="#模拟未登录状态
#请求方式post
#====================================================================================
#详细过程
#1.点击在前端旁边lnitiator（由用于查看执行请求的过程），call stack的一个栈里面写了js脚本的执行过程（从下往上）
#2.点击最上面链接，也就是最后一次执行的链接，然后点框框。（改成正常我们看的舒服的）
#3.找send(data)【这样的：this.tt3x.send(gA0x.data)】做一个断点，断点设置就是在本行的最左边点击一下跟c语言一样
#4.再次刷新，由于断点过，代码会在断点前停下来，断点前的信息将会显示在右边框的scope里面的local里面，看request在哪里就点开哪一个
#5.这里的url是（/weapi/cdns?csrf_token=ce24f899914b2aa549183800105e8bfd）不是我们想要的，我们想要get的东西也就是上面的那个
#get的东西（url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token=），
#6.就是点击播放建，放开我们进行下次拦截，直到我们得到我们想要的get结尾的url
#就是这玩意(https://music.163.com/weapi/comment/resource/comments/get?csrf_token=ce24f899914b2aa549183800105e8bfd"）
#我们的data此时已经被加密（data "params=4iPRPLg4P7NEQqKhAbR5yH1U%2Bd1wX2cq5m2M940N2bnyaRlEqIO0H5GnmzQVSfhWrEqrg2a50pjRtIfkCh68KDsIdcdxpLQxMBohqlJZnzBvvkc%2BI82h8ZWPVx3G9g8l2HnwBCRSWKoZ8eFSV%2B3VLTSBiA8qRhAf53%2B1EKy45sVt9M3aLhB1ze4RwF49k5a%2Bsza4%2FEk0YYj9zjpjUSaW8Dv7ah3vyqezfYJKBgQdZPJ%2FzPL5BD9W2uadsrvTDhWsuErpbMvRyvUgIAndQx14FTzgIz5ioyCDhSvu2btLY%2FGdvRVqG3hxfPH%2FrC9vf%2Bw9PmNpDAKfXyqwNBzfy2p55h5pYM8A4AvYUadJrDD1w7g%3D&encSecKey=124ff0929ac238e0511fe2b605039fc02acac780a75c6ce2f5403d5f0a46b658a949dca4cf80d4eed62b824296b22de44b5e9ab09cd86d546fffd003efbbe6ce6e5a0b7996a25e7bd1de1a053582f7853229faff05585d05ae0d3a22ec985851953612ceccfb3308032f2972ef11950c1939c2b779d4b71bf1a98fbc881e0f1b"）
#7.看local下面我们的名字:ef9,看左边的代码找上一个data是怎么被加密的
#看右边的call stall里面是js脚本倒数第二部，我们看一下是不是这个时候被加密的，用上面方法看一下程序有没有还被加密，直到找到未加密的，就是data比较短
#也就是说程序在anonymous后面开始被加密，然后回到被加密的那一步，此时我们已经找到被加密的这一步了
#8.在这个函数这个，设置断点，然后将之前的断点给去掉，breakpoint那里，重新点播放键，再刷新页面，然后看请求里面的东西类似这样的（X9O: "/api/cdns"）
#跟我们没关系，然后点击播放键，找一个get在最后的（X9O: "https://music.163.com/api/comment/resource/comments/get"）这个是获取评论的url看data有没有问题，然后点击播放旁边的那个
#将断点往下拉，我们看data是哪一步开始变的，直到（ var bVi8a = window.asrsea(JSON.stringify(i9b), bsu7n(["流泪", "强"]), bsu7n(Xo2x.md), bsu7n(["爱心",）这一行我们发现data变了
#

