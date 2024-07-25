[[alist网盘]]

[Replit](https://replit.com/)
## 部署alist网盘
[利用 Replit 平台免费搭建 AList 网盘 | Naive Koala](https://www.xalaok.top/post/alist-on-replit/)密码最后没获取到，所以要合着[利用replit搭建Alist | 舒夏博客](https://sxbai.com/2022/11/11/replit-alist/)一起看。
[利用mogenius搭建uptime来监控repl项目防止休眠 | 舒夏博客](https://sxbai.com/2022/11/11/mogenius-uptime-kuma/)，（其实教程1本身就带一个保活，可是并没有软用。）这个网站注册要企业邮箱。

试验效果：[AList](https://9220bb7f-85a4-44e6-aa3a-3432dd2d8e60-00-1h2a5259j87a7.pike.replit.dev/)
保活：[[监控平台]]，试过了没效果。
### 过程

简单来说就是
- 下载文件解压上传到resplit里面的bash项目
- 输入
```
chmod +x alist
./alist server
````
获取密码。
- 再在main.sh窗口输入
```
echo Hello World
URL=${REPL_SLUG}.${REPL_OWNER}.repl.co
while true; do curl -s "https://$URL" >/dev/null 2>&1 && echo "$(date +'%Y%m%d%H%M%S') Keeping online …" && sleep 300; done &
chmod +x ./replit
nohup ./replit server

````
- 运行就OK了。