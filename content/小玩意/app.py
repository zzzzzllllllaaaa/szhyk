from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# 读取Excel文件并创建查找表
def load_data():
    df = pd.read_excel('data.xlsx')  # 确保data.xlsx文件在项目根目录
    lookup = {}
    for _, row in df.iterrows():
        customer_id = str(row['顾客ID'])
        box_number = int(row['箱号'])  # 确保箱号是一个标准的Python int类型
        last_four_digits = customer_id[-4:]
        lookup[last_four_digits] = box_number
    return lookup

data = load_data()

@app.route('/api/query', methods=['GET'])
def query():
    customer_id = request.args.get('customer_id')
    app.logger.info(f"Received query for customer_id: {customer_id}")
    if not customer_id:
        app.logger.warning("Missing customer_id parameter")
        return jsonify({"error": "缺少顾客ID参数"}), 400
    
    box_number = data.get(customer_id[-4:])
    if box_number is not None:
        app.logger.info(f"Box number found: {box_number}")
        return jsonify({"箱号": box_number})
    else:
        app.logger.warning("No box number found")
        return jsonify({"error": "未找到对应的箱号"}), 404

if __name__ == '__main__':
    app.run(debug=True)
