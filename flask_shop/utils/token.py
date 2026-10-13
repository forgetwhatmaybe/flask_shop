
import jwt
from flask import current_app
from functools import wraps 
from flask import request, jsonify
import time


#生成token
def generate_token(data):
    
    data.update({"exp": time.time()+current_app.config['JWT_EXPIRATION_DELTA']})  #设置过期时间为7天
    
    
    #数据的加密
    token = jwt.encode(data, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token

#验证token
def verify_token(token):
    try:
        #解密token
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return data
    except Exception as e:
        print(e)
        return None
    
    
def login_required(view_func):
    @wraps(view_func)
    def decorated_function(*args, **kwargs):
        #获取请求头中的token
        token = request.headers.get('token')
        #验证token
        if verify_token(token):
            return view_func(*args, **kwargs)
        else:
            return jsonify({'status': 401, 'msg': '请先登录'})
    return decorated_function