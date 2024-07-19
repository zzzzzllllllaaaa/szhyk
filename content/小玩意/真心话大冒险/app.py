from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

# 读取Excel文件
df = pd.read_excel('真心话大冒险.xlsx')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw_card')
def draw_card():
    # 抽取一张卡片
    card = random.choice(df['卡片内容'].tolist())  # 确保替换 '卡片内容' 为你Excel文件中的实际列名
    return render_template('index.html', card=card)

if __name__ == '__main__':
    app.run(debug=True)
