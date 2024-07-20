const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const WebSocket = require('ws');
const { v4: uuidv4 } = require('uuid');

const app = express();
app.use(bodyParser.json());

// 读取 JSON 文件
const dataFilePath = './data.json';
let data = {};

function loadData() {
    try {
        const fileData = fs.readFileSync(dataFilePath, 'utf8');
        data = JSON.parse(fileData);
    } catch (error) {
        console.error('Error loading data:', error);
        data = {
            "真心话": [],
            "大冒险": [],
            "回复表": []
        };
    }
}

function saveData() {
    fs.writeFileSync(dataFilePath, JSON.stringify(data, null, 2), 'utf8');
}

loadData();

// 存储用户和对应的 WebSocket 连接
const userConnections = {};

// 存储每个用户的记录
const userRecords = {};

// WebSocket server
const wss = new WebSocket.Server({ noServer: true });

wss.on('connection', (ws, req) => {
    const userId = req.url.split('/').pop();
    userConnections[userId] = ws;

    ws.on('message', (message) => {
        const data = JSON.parse(message);
        if (!userRecords[userId]) {
            userRecords[userId] = [];
        }
        userRecords[userId].push(data);

        if (userRecords[userId].length > 10) {
            userRecords[userId].shift();
        }

        if (data.partnerId && userConnections[data.partnerId]) {
            userConnections[data.partnerId].send(JSON.stringify({
                event: 'update',
                records: userRecords[userId]
            }));
        }
    });

    ws.on('close', () => {
        delete userConnections[userId];
    });

    ws.send(JSON.stringify({
        event: 'connected',
        userId: userId,
        records: userRecords[userId] || []
    }));
});

const server = app.listen(3000, () => {
    console.log('Server is running on port 3000');
});

server.on('upgrade', (request, socket, head) => {
    wss.handleUpgrade(request, socket, head, (ws) => {
        wss.emit('connection', ws, request);
    });
});

app.get('/data', (req, res) => {
    res.json(data);
});

app.post('/submit-reply', (req, res) => {
    const reply = req.body.reply;
    if (!reply) {
        return res.status(400).send('回复内容不能为空');
    }

    if (!data['回复表']) {
        data['回复表'] = [];
    }

    data['回复表'].push({ 回复: reply });
    saveData();
    res.sendStatus(200);
});

app.post('/connect', (req, res) => {
    const userId = uuidv4().slice(0, 5);
    res.json({ userId });
});
