from flask import Flask, jsonify, request, render_template
import pandas as pd
import random

app = Flask(__name__)

# 读取Excel文件
df = pd.read_excel('真心话大冒险.xlsx')

# 初始化卡片
cards = list(range(1, 25))
random.shuffle(cards)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw_card', methods=['POST'])
def draw_card():
    if len(cards) == 0:
        return jsonify({'message': '游戏结束，所有卡片已抽完！'}), 200

    card_number = cards.pop()
    card_type = random.choice(['truth', 'dare'])
    if card_type == 'truth':
        content = df.iloc[card_number - 1, 0]
    else:
        content = df.iloc[card_number - 1, 1]

    return jsonify({'card_number': card_number, 'type': card_type, 'content': content}), 200

@app.route('/reset_game', methods=['POST'])
def reset_game():
    global cards
    cards = list(range(1, 25))
    random.shuffle(cards)
    return jsonify({'message': '游戏已重置'}), 200

if __name__ == '__main__':
    app.run(debug=True)
