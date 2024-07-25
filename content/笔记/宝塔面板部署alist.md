[[alist网盘]]

[教程](https://www.dujin.org/19298.html)有部分失效，搭配[官方文档](https://alist.nn.ci/zh/guide/install/script.html#%E8%8E%B7%E5%8F%96%E5%AF%86%E7%A0%81)使用。

部署好宝塔面板之后，创建网站。

数据库无需创建，PHP版本可随意，纯静态也可以。这里我们复制一下`根目录`地址，后面安装 Alist 程序需要用到。根目录地址为：

```
/www/wwwroot/alist.dujin.org
```

## 宝塔安装 Alist 程序

接下来，通过 ssh 连接该服务器，在官方给出的基础上，末尾增加指定目录安装，添加刚刚得到的根目录地址，如下示例。


```
curl -fsSL "https://alist.nn.ci/v3.sh" | bash -s install /www/wwwroot/alist.dujin.org
curl -fsSL "https://alist.nn.ci/v3.sh" | bash -s update /www/wwwroot/alist.dujin.org
curl -fsSL "https://alist.nn.ci/v3.sh" | bash -s uninstall /www/wwwroot/alist.dujin.org
```


install 为安装，update 为升级，uninstall 为卸载。我们执行第一行安装之后，会得到如下内容：

```
Alist 安装成功！

访问地址：http://YOUR_IP:5244/

配置文件：/www/wwwroot/alist.dujin.org/alist/data/config.json
初始管理密码：www.dujin.org

查看状态：systemctl status alist
启动服务：systemctl start alist
重启服务：systemctl restart alist
停止服务：systemctl stop alist

温馨提示：如果端口无法正常访问，请检查 服务器安全组、本机防火墙、Alist状态
```

ps:这一步不是显示这个,还需要自己按照要求再输入两个指令获取密码。

这里我们要记住 Alist 初始管理密码。所以，你如果是使用阿里云、腾讯云、华为云之类的服务器，就要把这个 5244 端口给开一下，同时在`宝塔`→`安全`里面也对 5244 端口放行一下。

![](https://img.dujin.org/uploads/2022/04/20220423201058.png)

## 给 Alist 程序添加反向代理

点击宝塔→`网站`菜单→对应网站`设置`→反向代理→添加反向代理。

![](https://img.dujin.org/uploads/2022/04/20220423201617.png)

点击开启代理，代理名称随意，目标URL设置为：


```
http://127.0.0.1:5244
```

其余保持默认即可，点击`提交`按钮。