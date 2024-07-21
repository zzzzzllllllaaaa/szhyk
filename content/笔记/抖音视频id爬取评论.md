[[抖音]]，[[有意思]]

抖音视频链接可以分享视频链接在浏览器打开，最前面的那一长串数字就是视频id。

[视频评论查询 (zhzhzh.cloudns.ch)](http://a.zhzhzh.cloudns.ch/%E5%B0%8F%E7%8E%A9%E6%84%8F/%E7%88%AC%E5%8F%96%E6%8A%96%E9%9F%B3%E8%A7%86%E9%A2%91%E8%AF%84%E8%AE%BA.html)，ps:手机端好像导出不了，算了，管它呢，就这样吧！
## 简化（最终版本）
- 只保留评论内容和获赞数
- 评论内容只保留具体内容，去除掉“评论内容”这个前缀

### HTML 和 JavaScript 代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>视频评论查询</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        input, button {
            padding: 10px;
            margin: 5px;
        }
        .comments {
            margin-top: 20px;
        }
        .comment {
            border-bottom: 1px solid #ccc;
            padding: 10px 0;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>视频评论查询</h1>
    <label for="videoId">视频ID:</label>
    <input type="text" id="videoId" placeholder="输入视频ID">
    <label for="pn">开始条数:</label>
    <input type="number" id="pn" placeholder="输入开始条数" value="0">
    <label for="ps">数量:</label>
    <input type="number" id="ps" placeholder="输入查询数量" value="300">
    <button onclick="fetchComments()">查询评论</button>
    <button onclick="exportToTXT()">导出为TXT文件</button>
    <button onclick="exportToExcel()">导出为Excel文件</button>
    <div class="comments" id="comments"></div>

    <script>
        let allComments = [];

        async function fetchComments() {
            const videoId = document.getElementById('videoId').value.trim();
            const ps = parseInt(document.getElementById('ps').value) || 300;
            const pn = parseInt(document.getElementById('pn').value) || 0;

            if (!videoId) {
                alert("请输入视频ID");
                return;
            }

            allComments = [];
            let currentPn = pn;
            const pageSize = 50; // Assuming the API supports a maximum of 50 comments per request

            while (allComments.length < ps) {
                const url = `https://bzapi.bzweb.xyz/api/public/dy/video/comment?id=${videoId}&pn=${currentPn}&ps=${pageSize}`;
                try {
                    const response = await fetch(url);
                    const result = await response.json();

                    if (result.code === 200 && result.status) {
                        allComments = allComments.concat(result.data.comments);
                        if (result.data.comments.length < pageSize) {
                            // No more comments to fetch
                            break;
                        }
                        currentPn += pageSize;
                    } else {
                        alert("请求失败，状态码：" + result.code);
                        break;
                    }
                } catch (error) {
                    console.error("请求出错：", error);
                    alert("请求出错，请检查控制台日志");
                    break;
                }
            }

            displayComments(allComments.slice(0, ps));
        }

        function displayComments(comments) {
            const commentsContainer = document.getElementById('comments');
            commentsContainer.innerHTML = '';

            if (comments.length === 0) {
                commentsContainer.innerHTML = '<p>没有评论</p>';
                return;
            }

            comments.forEach(comment => {
                const commentElement = document.createElement('div');
                commentElement.className = 'comment';
                commentElement.innerHTML = `
                    <p>${comment.text}</p>
                    <p><strong>获赞数:</strong> ${comment.digg_count}</p>
                `;
                commentsContainer.appendChild(commentElement);
            });
        }

        function exportToTXT() {
            const commentTexts = allComments.map(comment => `
${comment.text}
获赞数: ${comment.digg_count}
            `).join('\n\n');

            const blob = new Blob([commentTexts], { type: 'text/plain' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'comments.txt';
            link.click();
        }

        function exportToExcel() {
            const headers = ['评论内容', '获赞数'];
            const rows = allComments.map(comment => [
                comment.text,
                comment.digg_count
            ]);

            const csvContent = [headers, ...rows].map(e => e.join(",")).join("\n");
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'comments.csv';
            link.click();
        }
    </script>
</body>
</html>
```



## 优化抓取数目，增加导出功能
好的，这里是一个增强版的HTML和JavaScript代码，它包含分页请求、从指定条数开始、以及导出评论到TXT和Excel文件的功能。

### 代码功能概述

1. **输入选项**：用户可以输入视频ID、开始条数和查询数量。
2. **获取评论**：通过分页请求获取评论数据，最多获取到用户指定的数量。
3. **显示评论**：将获取到的评论数据显示在页面上。
4. **导出功能**：用户可以选择将评论导出为TXT文件或Excel文件（CSV格式）。

### 注意事项

- **分页请求限制**：API一次最多支持获取50条评论，代码会根据需要多次请求以获取到用户指定数量的评论。
- **导出文件格式**：TXT文件导出为纯文本格式，Excel文件导出为CSV格式，可以用Excel打开并查看。
- **浏览器支持**：确保用户使用的浏览器支持Blob和URL.createObjectURL等API。

### HTML 和 JavaScript 代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>视频评论查询</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        input, button {
            padding: 10px;
            margin: 5px;
        }
        .comments {
            margin-top: 20px;
        }
        .comment {
            border-bottom: 1px solid #ccc;
            padding: 10px 0;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>视频评论查询</h1>
    <label for="videoId">视频ID:</label>
    <input type="text" id="videoId" placeholder="输入视频ID">
    <label for="pn">开始条数:</label>
    <input type="number" id="pn" placeholder="输入开始条数" value="0">
    <label for="ps">数量:</label>
    <input type="number" id="ps" placeholder="输入查询数量" value="300">
    <button onclick="fetchComments()">查询评论</button>
    <button onclick="exportToTXT()">导出为TXT文件</button>
    <button onclick="exportToExcel()">导出为Excel文件</button>
    <div class="comments" id="comments"></div>

    <script>
        let allComments = [];

        async function fetchComments() {
            const videoId = document.getElementById('videoId').value.trim();
            const ps = parseInt(document.getElementById('ps').value) || 300;
            const pn = parseInt(document.getElementById('pn').value) || 0;

            if (!videoId) {
                alert("请输入视频ID");
                return;
            }

            allComments = [];
            let currentPn = pn;
            const pageSize = 50; // Assuming the API supports a maximum of 50 comments per request

            while (allComments.length < ps) {
                const url = `https://bzapi.bzweb.xyz/api/public/dy/video/comment?id=${videoId}&pn=${currentPn}&ps=${pageSize}`;
                try {
                    const response = await fetch(url);
                    const result = await response.json();

                    if (result.code === 200 && result.status) {
                        allComments = allComments.concat(result.data.comments);
                        if (result.data.comments.length < pageSize) {
                            // No more comments to fetch
                            break;
                        }
                        currentPn += pageSize;
                    } else {
                        alert("请求失败，状态码：" + result.code);
                        break;
                    }
                } catch (error) {
                    console.error("请求出错：", error);
                    alert("请求出错，请检查控制台日志");
                    break;
                }
            }

            displayComments(allComments.slice(0, ps));
        }

        function displayComments(comments) {
            const commentsContainer = document.getElementById('comments');
            commentsContainer.innerHTML = '';

            if (comments.length === 0) {
                commentsContainer.innerHTML = '<p>没有评论</p>';
                return;
            }

            comments.forEach(comment => {
                const commentElement = document.createElement('div');
                commentElement.className = 'comment';
                commentElement.innerHTML = `
                    <p><strong>评论者用户ID:</strong> ${comment.uid}</p>
                    <p><strong>评论时间:</strong> ${new Date(comment.create_time * 1000).toLocaleString()}</p>
                    <p><strong>评论内容:</strong> ${comment.text}</p>
                    <p><strong>获赞数:</strong> ${comment.digg_count}</p>
                `;
                commentsContainer.appendChild(commentElement);
            });
        }

        function exportToTXT() {
            const commentTexts = allComments.map(comment => `
评论者用户ID: ${comment.uid}
评论时间: ${new Date(comment.create_time * 1000).toLocaleString()}
评论内容: ${comment.text}
获赞数: ${comment.digg_count}
            `).join('\n\n');

            const blob = new Blob([commentTexts], { type: 'text/plain' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'comments.txt';
            link.click();
        }

        function exportToExcel() {
            const headers = ['评论者用户ID', '评论时间', '评论内容', '获赞数'];
            const rows = allComments.map(comment => [
                comment.uid,
                new Date(comment.create_time * 1000).toLocaleString(),
                comment.text,
                comment.digg_count
            ]);

            const csvContent = [headers, ...rows].map(e => e.join(",")).join("\n");
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'comments.csv';
            link.click();
        }
    </script>
</body>
</html>
```

## 最初版本最多抓取50条

[抖音视频图文根据ID获得评论信息单页源码 _ 酷库博客 (zxki.cn)](https://www.zxki.cn/9991.html)

### 代码功能概述

1. **页面布局**：包含输入框、按钮和显示评论的区域。
2. **用户输入**：用户可以输入视频ID、开始条数和查询数量。
3. **获取评论**：点击按钮后，通过JavaScript的`fetch` API请求评论数据。
4. **显示评论**：将获取到的评论数据显示在页面上。

### 改进建议

1. **输入验证**：增加更详细的输入验证，确保视频ID格式正确，开始条数和查询数量为正整数。
2. **错误处理**：增加更多的错误处理，比如处理网络错误或API返回的不同错误状态码。
3. **UI改进**：改进样式，使页面更美观和用户友好。
4. **分页功能**：如果评论很多，可以增加分页功能，方便用户浏览更多评论。

### 示例改进

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>视频评论查询</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        input, button {
            padding: 10px;
            margin: 5px;
        }
        .comments {
            margin-top: 20px;
        }
        .comment {
            border-bottom: 1px solid #ccc;
            padding: 10px 0;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>视频评论查询</h1>
    <label for="videoId">视频ID:</label>
    <input type="text" id="videoId" placeholder="输入视频ID">
    <label for="pn">开始条数:</label>
    <input type="number" id="pn" placeholder="输入开始条数" value="0">
    <label for="ps">数量:</label>
    <input type="number" id="ps" placeholder="输入查询数量" value="20">
    <button onclick="fetchComments()">查询评论</button>
    <div class="comments" id="comments"></div>

    <script>
        async function fetchComments() {
            const videoId = document.getElementById('videoId').value.trim();
            const pn = parseInt(document.getElementById('pn').value) || 0;
            const ps = parseInt(document.getElementById('ps').value) || 20;

            if (!videoId) {
                alert("请输入视频ID");
                return;
            }

            const url = `https://bzapi.bzweb.xyz/api/public/dy/video/comment?id=${videoId}&pn=${pn}&ps=${ps}`;

            try {
                const response = await fetch(url);
                const result = await response.json();

                if (result.code === 200 && result.status) {
                    displayComments(result.data.comments);
                } else {
                    alert("请求失败，状态码：" + result.code);
                }
            } catch (error) {
                console.error("请求出错：", error);
                alert("请求出错，请检查控制台日志");
            }
        }

        function displayComments(comments) {
            const commentsContainer = document.getElementById('comments');
            commentsContainer.innerHTML = '';

            if (comments.length === 0) {
                commentsContainer.innerHTML = '<p>没有评论</p>';
                return;
            }

            comments.forEach(comment => {
                const commentElement = document.createElement('div');
                commentElement.className = 'comment';
                commentElement.innerHTML = `
                    <p><strong>评论者用户ID:</strong> ${comment.uid}</p>
                    <p><strong>评论时间:</strong> ${new Date(comment.create_time * 1000).toLocaleString()}</p>
                    <p><strong>评论内容:</strong> ${comment.text}</p>
                    <p><strong>获赞数:</strong> ${comment.digg_count}</p>
                `;
                commentsContainer.appendChild(commentElement);
            });
        }
    </script>
</body>
</html>
```

