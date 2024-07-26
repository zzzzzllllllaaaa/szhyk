[[rss]]

[rsshub](https://docs.rsshub.app/)
[教程](https://b23.tv/N4gvzXL)

### vercel(墙)
部署过程与[[在线大声朗读部署]]类似。(电脑+梯子)
1. 打开github和vercel
2. 打开([rsshub](https://docs.rsshub.app/)打不开用别人部署的文档:https://rsshub-doc.vercel.app/dist)，直接部署那里点vercel按钮一键部署。
3. 成功。

成功部署地址:https://rss-sigma-two.vercel.app/

### 宝塔面板docker(安全)
[教程](https://cry33.com/archives/489.html)，后面部分搞时光机域名解析验证部署ssl，因为西部数码里面域名解析类型不含有caa类型，所以没办法进行下去。

没有部署ssl，telegram频道订阅无法加载。
#### 安装Docker和PM2管理器

在宝塔的软件商店里搜索 `管理器`，找到 `Docker管理器`和 `PM2管理器`，并安装

![](https://img-blog.csdnimg.cn/img_convert/4af8834c064acd7dbe3151a33ffd16f1.png)

安装完成后，设置为首页显示

![](https://img-blog.csdnimg.cn/img_convert/efccc71ce4d77667877f742ebc652ab3.png)

这样我们就能直接从首页打开并设置了。

#### 配置Docker

##### 获取镜像

打开Docker管理器，点击 `镜像管理` - `获取镜像` ，输入`diygod/rsshub` 获取rsshub镜像

![](https://img-blog.csdnimg.cn/img_convert/c225ed5e9ac6613ada3a87b7ca0dc028.png)

出现如图所示，则获取成功

![](https://img-blog.csdnimg.cn/img_convert/54de1ddcec348755c744f0ee42d36a53.png)

#### 创建Docker容器

打开 `容器列表` - `创建容器`，具体配置如图所示：

![](https://img-blog.csdnimg.cn/img_convert/87ba20e65aa9a86a285800125f86598f.png)

> 1.  端口映射为1200
> 2.  将目录 `/www/wwwroot/rsshub/` 映射到目录 `/usr/src/app/`
> 3.  CPU权重 30

配置完成后，点击提交。稍等片刻，容器就创建成功了

![](https://img-blog.csdnimg.cn/img_convert/39074ebc7d66c7418fb84376781afbe4.png)

#### 新建网站并反代

##### 宝塔新建站点

域名填写服务器IP或者域名地址，php版本为纯静态

![](https://img-blog.csdnimg.cn/img_convert/e669f7bcbe66f43e246d93366db17fe5.png)

##### 设置反向代理

1.先进入网站设置

![](https://img-blog.csdnimg.cn/img_convert/76fc1d83a70dc34c4d8748438c02d5ca.png)

2.找到反向代理，并进行如下设置

![](https://img-blog.csdnimg.cn/img_convert/e5418596af2e317157d9c5dd5a6a0f8a.png)

> 目标URL：`http://127.0.0.1:1200`

3.提交后，访问之前设置好的域名或者ip地址

![](https://img-blog.csdnimg.cn/img_convert/16ff3c6cee8cebb465fdaaf0da727fde.png)

出现如图所示，即代表成功部署了rsshub服务。此时，我们就可以使用rsshub的订阅规则，订阅我们想订阅的内容了。比如我想订阅bing的每日壁纸，这时使用 `https://rsshub.cry33.com/bing` 这个链接就可以在rss阅读器里订阅了。
