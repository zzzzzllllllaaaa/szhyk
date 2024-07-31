[[在表格上检索数据]]

在原来的基础上用网站来查询数据可能要更快一些，我在想如果再加入语音输入输出会不好更快呢？

### 需求
- 帮我编写一个html，可以上传exccel，我上传的excel表格只包含两列数据，一列是顾客id，一列是箱号，我需要这个网站提供一个输入顾客id后四尾数输出对应箱号的功能。
- 修改一下，我会把对应的excel文件命名为查询表.xlsx，然后放在同一文件夹里面，这样直接查询这个文件就可以了，不需要选择文件。
- 我觉得重复删除输入很烦，可以改成输出箱号后清空框内的内容，保留5条最近查询过的数据
- 增加了回车键直接输入功能
- 保留10条记录，并增加删除记录按钮。
- 给记录前面增加序号
- 自适应页面大小
- 出现代理域名无法读取数据问题（尝试将xlsx数据源转换成json数据源，[[xlsx文件转json文件网站]]，[[从json查询数据版本]]，结果还是不行）（尝试使用api查询呢？）



### 代码

```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>顾客ID与箱号查询</title>
    <script src="https://cdn.jsdelivr.net/npm/xlsx/dist/xlsx.full.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            margin: 0;
            box-sizing: border-box;
        }
        input, button {
            margin: 10px 0;
            display: block;
            width: 100%;
            max-width: 300px;
            padding: 10px;
            box-sizing: border-box;
        }
        .history {
            margin-top: 20px;
        }
        .history-item {
            margin-bottom: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .delete-btn {
            margin-left: 10px;
            cursor: pointer;
            color: red;
        }
        @media (min-width: 600px) {
            input, button {
                width: auto;
                display: inline-block;
            }
            button {
                margin-left: 10px;
            }
        }
        @media (min-width: 800px) {
            .history-item {
                justify-content: flex-start;
            }
            .delete-btn {
                margin-left: auto;
            }
        }
    </style>
</head>
<body>

<h1>顾客ID与箱号查询</h1>
<input type="text" id="customerId" placeholder="输入顾客ID后四位" />
<button onclick="findBoxNumber()">查询箱号</button>
<br>
<h3 id="result"></h3>
<div class="history">
    <h3>最近查询</h3>
    <button onclick="deleteAllHistory()">删除所有记录</button>
    <div id="historyList"></div>
</div>

<script>
    let data = {};
    let history = [];

    // 假设'查询表.xlsx'在同一目录下
    function readExcelFile() {
        fetch('查询表.xlsx')
            .then(res => res.arrayBuffer())
            .then(ab => {
                const workbook = XLSX.read(ab, { type: 'array' });
                const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
                const json = XLSX.utils.sheet_to_json(firstSheet, { header: 1 });
                json.forEach(row => {
                    const customerId = row[0].toString();
                    const boxNumber = row[1];
                    if (customerId && boxNumber) {
                        data[customerId.slice(-4)] = boxNumber;
                    }
                });
            })
            .catch(error => console.error('Error reading the Excel file:', error));
    }

    function findBoxNumber() {
        const inputId = document.getElementById('customerId').value;
        const boxNumber = data[inputId];
        const result = boxNumber ? `箱号: ${boxNumber}` : '未找到对应的箱号';
        document.getElementById('result').innerText = result;

        // 清空输入框内容
        document.getElementById('customerId').value = '';

        // 更新查询历史
        if (inputId) {
            if (history.length === 10) {
                history.shift(); // 删除最旧的一条记录
            }
            history.push({ id: inputId, box: result });
            updateHistoryList();
        }
    }

    function updateHistoryList() {
        const historyList = document.getElementById('historyList');
        historyList.innerHTML = '';
        history.forEach((item, index) => {
            const div = document.createElement('div');
            div.className = 'history-item';
            div.innerHTML = `${index + 1}. 顾客ID: ${item.id}, ${item.box} <span class="delete-btn" onclick="deleteHistoryItem(${index})">删除</span>`;
            historyList.appendChild(div);
        });
    }

    function deleteHistoryItem(index) {
        history.splice(index, 1);
        updateHistoryList();
    }

    function deleteAllHistory() {
        history = [];
        updateHistoryList();
    }

    // 读取Excel文件
    readExcelFile();

    // 添加回车键查询功能
    document.getElementById('customerId').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            findBoxNumber();
        }
    });
</script>

</body>
</html>
```


