[[听评论]]，[[有意思]]

这个用python实现，我都忘记我啥时候装的了。

### 需求

1. 输入视频bv码抓取评论内容
2. 结果生成一个txt
3. 只保留评论人的昵称和评论内容。
4. 将二级评论直接放在对应的一级评论下面，不额外添加标识。
5. 在每条评论后添加分割线，以提高可读性。

这样，生成的TXT文件将只包含评论人的昵称和评论内容，并且如果有回复评论，它们会紧随对应的一级评论之后。分割线用于分隔不同的评论，使内容更易于阅读和理解。

### 使用
直接搞一个.py文件，输入代码，运行文件，输入bv码，结束，找到生成的文件看看。

### 结果
```python
import requests
import json
import re
import time

def get_comments(bv_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    # 获取视频的aid
    url = f'https://www.bilibili.com/video/{bv_id}'
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查HTTP响应状态码
    except requests.RequestException as e:
        print(f"请求视频页面时发生错误: {e}")
        return

    match = re.search(r'"aid":(\d+)', response.text)
    if not match:
        print("无法获取视频的aid")
        return
    aid = match.group(1)

    # 获取评论
    comments = []
    page_num = 1
    while True:
        comment_url = f'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={page_num}&type=1&oid={aid}&sort=2'
        try:
            response = requests.get(comment_url, headers=headers, timeout=10)
            response.raise_for_status()  # 检查HTTP响应状态码
        except requests.RequestException as e:
            print(f"请求评论时发生错误: {e}")
            break

        data = response.json()
        if not data['data']['replies']:
            break

        for reply in data['data']['replies']:
            comments.append({
                'user': reply['member']['uname'],
                'message': reply['content']['message']
            })
            # 获取二级评论
            if reply.get('replies'):
                for sub_reply in reply['replies']:
                    comments.append({
                        'user': sub_reply['member']['uname'],
                        'message': sub_reply['content']['message']
                    })

        page_num += 1
        time.sleep(1)  # 避免频繁请求

    # 保存评论到txt文件
    with open(f'{bv_id}_comments.txt', 'w', encoding='utf-8') as f:
        for comment in comments:
            f.write(f"{comment['user']}: {comment['message']}\n")
            f.write("-" * 80 + "\n")

    print(f"评论已保存到 {bv_id}_comments.txt")

if __name__ == "__main__":
    bv_id = input("请输入视频的BV号: ")
    get_comments(bv_id)
```

