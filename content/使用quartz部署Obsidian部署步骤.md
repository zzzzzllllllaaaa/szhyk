[[index]]

自定义域名需要修改quartz.config.ts里面的baseUrl
页脚在：quartz\quartz.layout.ts里面
```
npx quartz sync
````
### 部署教程
[如何使用 Quartz 4.0 和 GitHub Pages 免费发布 Obsidian 笔记 (insile.github.io)](https://insile.github.io/my-notes/%E7%AC%94%E8%AE%B0/%E5%85%AC%E5%85%B1%E7%AC%94%E8%AE%B0%E5%BA%93/%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8-Quartz-4.0-%E5%92%8C-GitHub-Pages-%E5%85%8D%E8%B4%B9%E5%8F%91%E5%B8%83-Obsidian-%E7%AC%94%E8%AE%B0#:~:text=%E4%B8%8B%E8%BD%BD%E5%B9%B6%E5%AE%89%E8%A3%85%20Quartz%20%E6%89%93%E5%BC%80%E7%BB%88%E7%AB%AF%E5%B9%B6%E8%BF%90%E8%A1%8C%E4%BB%A5%E4%B8%8B%E5%91%BD%E4%BB%A4%20git%20clone%20github.com%2Fjackyzha0%2Fquartz.git%20%23%20%E4%B8%8B%E8%BD%BD,relative%20paths%20%23%20Obsidian%20%E8%B7%AF%E5%BE%84%E8%AE%BE%E7%BD%AE%20You%27re%20all%20set%21),按他教程我没有看见index，最后结果点击主页就出现xml提示，我就按他的方法直接克隆他的库了（[insile/我的笔记 (github.com)](https://github.com/insile/my-notes)），结果一切正常，还不错。（其实也可以自己新建一个ibdex上去）


NodeJS v18.14+ （使用 node -v 检查您的版本）[Node.js — 下载 Node.js® (nodejs.org)](https://nodejs.org/zh-cn/download/prebuilt-installer)
NPM v9.3.1+（使用 npm -v 检查您的版本）（安装node后自带npm）
Git（使用 git --version 检查您的版本）[CNPM Binaries Mirror (npmmirror.com)](https://registry.npmmirror.com/binary.html?path=git-for-windows/)
Obsidian

##### 步骤 1. 下载并安装 Quartz

- 打开终端并运行以下命令（自己创建一个文件夹，在文件夹上右键打开git指令页面）
```
git clone https://github.com/jackyzha0/quartz.git
# 下载 Quartz 存储库的副本，并将其存储在当前文件夹的 quartz 中
 
cd quartz
# 进入 quartz
 
npm i
# 安装 Quartz 依赖项
 
npx quartz create
# 创建一个新的 Quartz 项目
````

##### 步骤 2. 设置 GitHub 存储库

- 在 GitHub.com 上创建一个新存储库。不要使用 README 、许可证或 gitignore 文件初始化新存储库。（就是创建一个空白库）
- 在 GitHub.com 的“快速设置”页面上存储库的顶部，单击剪贴板以复制远程存储库 URL

```
git remote -v
# 列出所有被跟踪的仓库
# origin  https://github.com/jackyzha0/quartz.git (fetch)
# origin  https://github.com/jackyzha0/quartz.git (push)
# upstream        https://github.com/jackyzha0/quartz.git (fetch)
# upstream        https://github.com/jackyzha0/quartz.git (push)
 
git remote set-url origin <URL>
# 此命令删除 origin 远程仓库 并替换为自己的 URL
 
npx quartz sync --no-pull
# 将对本地仓库所做的更改推送到远程仓库上的
# 末尾带有绿色 Done! 
````

注意：自己url替换掉`<URL>`，而不是url。

##### 步骤 3. 创建 Obsidian 库

- 在 Obsidian 中将 quartz 里的 content 文件夹作为 Obsidian 库打开，然后就可以按照以往习惯写文档（最后部署完后url/你的笔记名就能找到你的笔记）
- index.md 是网站首页不要删除（我没看到）

```
npx quartz sync
````

每次更改后记得更新推送到远程仓库上。`

##### 步骤 4. 在线托管您的保管库

- 前往 GitHub 仓库，点击 Settings>Pages>Source 下拉菜单，选择 GitHub Actions
- 选择静态网站，替代原模板输入下面内容。
- `quartz/.github/workflows/deploy.yml`
```
name: Deploy Quartz site to GitHub Pages
 
on:
  push:
    branches:
      - v4
 
permissions:
  contents: read
  pages: write
  id-token: write
 
concurrency:
  group: "pages"
  cancel-in-progress: false
 
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0 # Fetch all history for git info
      - uses: actions/setup-node@v3
        with:
          node-version: 18.14
      - name: Install Dependencies
        run: npm ci
      - name: Build Quartz
        run: npx quartz build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: public
 
  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
````


- 最后提交更改，网站将部署到 `<github-username>.github.io/<repository-name>`，Pages 页面将会有以下提示 `Your site is live at https://insile.github.io/my-notes/`

```
npx quartz sync
````

每次更改后记得更新推送到远程仓库上`

##### 步骤 5. 更多个性化设置

- [https://quartz.jzhao.xyz/](https://quartz.jzhao.xyz/)