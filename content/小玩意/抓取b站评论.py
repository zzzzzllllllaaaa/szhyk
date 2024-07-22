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
