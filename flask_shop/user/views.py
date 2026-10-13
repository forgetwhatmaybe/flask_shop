from flask_shop.user import user_bp,user_api
from flask_shop import models
from flask import request
from flask_restful import Resource
from flask_shop import db
import re
from flask_shop.utils.token import generate_token, verify_token, login_required

@user_bp.route('/')
def index():
    return "Hello, Flask Shop!"


@user_bp.route('/login/',methods=['POST'])
def login():
    #获取前端传入的用户名和密码
    name = request.get_json().get('name')
    pwd = request.get_json().get('pwd')
    
    #判断参数是否完整
    if not all([name, pwd]):
        return {'status': 400, 'msg': '参数不完整'}
    else:
        #查询数据库中是否存在该用户
        user = models.User.query.filter(models.User.name == name).first()
        #判断用户是否存在
        if user:
            #判断密码是否正确
            if user.check_password(pwd):
                
                token = generate_token({"id": user.id})
                return {'status': 200, 'msg': '登录成功',"data":{"token":token}}
        #用户不存在
        return {'status': 400, 'msg': '用户名或密码错误'}
    
class Users(Resource):
    def get(self):
        pass
    def post(self):
        #获取前端传入的参数
        name = request.get_json().get('name')
        pwd = request.get_json().get('pwd')
        real_pwd = request.get_json().get('real_pwd')
        nick_name = request.get_json().get('nick_name')
        phone = request.get_json().get('phone')
        email = request.get_json().get('email')
        
        if not all([name, pwd, real_pwd]):
            return {'status': 400, 'msg': '参数不完整'}
        
        if pwd != real_pwd:
            return {'status': 400, 'msg': '两次输入的密码不一致'}
        
        if len(name) < 2:
            return {'status': 400, 'msg': '用户名长度不能小于2位'}
        
        if not re.match(r'^1[3-9]\d{9}$', phone):
            return {'status': 400, 'msg': '手机号格式不正确'}
        
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            return {'status': 400, 'msg': '邮箱格式不正确'}
        
        user = models.User.query.filter((models.User.name == name)).first()
        if user:
            return {'status': 400, 'msg': '用户名已存在'}
        
        user = models.User(name=name, password=pwd,  nick_name=nick_name, phone=phone, email=email)
        #保存数据
        db.session.add(user)
        db.session.commit()
        return {'status': 200, 'msg': '注册成功'}
    
user_api.add_resource(Users, '/users/')


@user_bp.route('/test/', methods=['GET'])
@login_required
def test_login_required():
    return {'status': 200, 'msg': '登录成功'}
        
        
