[[数字花园]]，[[3zh/3zh|3zh]]


[[问题与解决]]

### 教程
- [托管替代方案 (ole.dev)](https://dg-docs.ole.dev/advanced/hosting-alternatives/)
- [利用obsidian构建个人博客 (zytomorrow.top)](https://zytomorrow.top/%E6%8A%80%E6%9C%AF%E6%8A%98%E8%85%BE/%E5%88%A9%E7%94%A8obsidian%E6%9E%84%E5%BB%BA%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2/#github)
- [Hi , Obsidian Digital Garden :: 木木木木木 (immmmm.com)](https://immmmm.com/hi-obsidian-digital-garden/)
### 托管平台
[[cloudfare（被墙了）]]，改用[[vercel]]可惜部署的网站还是有墙，最后改用[[netlify]]，目前依旧是用的netlify，当然因为用的同一个库，cloufare部署的也会同步更新。

ps:cloudfare虽然国内有墙了，可是他的seo实在是猛，我在必应上搜我内容标题可以搜出我自己，我搜东西的时候突然看见自己的内容，有一瞬间的惊喜，虽然netlify排名还更前，可是它只会显示我花园的主页面。
### 开始
#### 部署
1. 打开https://github.com/oleeskild/digitalgarden ，注册/登录。
2. 点击use this template，然后点击crmrate a new repoditory，填写仓库名，之后点击create repository。
3. ~~进入[[cloudfare（被墙了）]]，注册/登录。~~
4. ~~点击workers和pages，创建应用程序，选择pages，连接到git，选择github账号里面刚刚创建的仓库，直接开始设置。~~
5. ~~构建命令填例如“npm run build”，构建输出目录也是填写例如“dist”，保持并部署，等待完成。~~
6. ~~完了他会显示成功（也有邮箱提示），继续处理项目，能看到cloufare给你分配的==子域名==，这时候已经完成了大半。~~
3. 登录[[netlify]]，连接github，找到刚弄的仓库的项目，填入名称，直接部署，最后会给你名称.netlify.com的二级域名。

#### 插件
1. 直接在obsidian插件市场搜“Digital Garden”，下载启用。
2. 在插件设置“github repo name”填入的是github仓库名，"github username"填入的是github账号名，"github token"点击下面注释结尾的“here”跳转到获取页面，“note”下面输入token的备注，“expiration”下面选择的是token的有效时间(no expiration指无限时间)，下面一堆选项里面选一下“workflow”，完了"generate token"。
3. 复制打✓的那段字符，也就是token，回到插件设置填进去。
4. "base url"填前面~~cloudfare~~/netlify分配的域名，=="slugify note url"一定要关掉==，中文博客不关掉会发生错误链接。
5. 点开"manage note settings"，里面的选项可以全选。OK，基本结束了。

#### yaml设置
1. 作为主页的页面头加上
```
---
dg-home: true
dg-publish: true
---
```
2. 要发布的页面头加入
```
---
dg-publish: true
---
```
3. 最后点击侧边栏Digital Garden插件的图标更新就👌啦……使用前面那个域名访问就行了。



