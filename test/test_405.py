# -*- coding: utf-8 -*-
"""
验证 /user/test/ 的请求方法限制（只读测试，不改动源代码）

现象：Postman 请求 http://localhost:5000/user/test/ 返回 405 METHOD NOT ALLOWED
假设：路由 @user_bp.route('/test/', methods=['GET']) 只允许 GET，而 Postman 选的是 POST
"""
import os
import sys

# 把项目根目录加入 sys.path，才能 import flask_shop
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_shop import create_app
from flask_shop.utils.token import generate_token

app = create_app('development')
client = app.test_client()

# 用户截图/消息里提供的 token（由用户正在运行的服务进程签发）
USER_TOKEN = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJpZCI6MiwiZXhwIjoxNzkyMzgwNDgyLjA2Mzg3MjN9."
    "g51lez5RjulpGT3tibtDNJjwR8VtoHQXbhYZWsMevVk"
)


def show(method, path, headers=None):
    resp = client.open(path, method=method, headers=headers or {})
    body = resp.get_data(as_text=True)
    if len(body) > 120:
        body = body[:120] + "..."
    print(f"{method:4} {path:14} -> {resp.status_code}  {body}")


print("=" * 70)
print("1. 复现 Postman 的请求：POST + token header")
show("POST", "/user/test/", {"token": USER_TOKEN})

print()
print("2. 同样参数但换成 GET")
show("GET", "/user/test/", {"token": USER_TOKEN})

print()
print("3. GET 且不带 token")
show("GET", "/user/test/")

print()
print("4. GET + 本进程刚签发的 token")
with app.app_context():
    fresh_token = generate_token({"id": 2})
show("GET", "/user/test/", {"token": fresh_token})

print()
print("5. 对照：登录接口（只允许 POST）")
show("GET", "/user/login/")
show("POST", "/user/login/", {})
