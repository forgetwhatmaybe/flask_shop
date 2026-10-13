
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config_map

#创建SQLAlchemy对象
db = SQLAlchemy()

def create_app(config_name):
    #创建Flask对象
    app = Flask(__name__)
    
    #根据传入的配置名称获取对应的配置类，如果没有传入配置名称，则默认使用开发环境配置
    Config = config_map.get(config_name, config_map['development'])
    
    #加载配置文件
    app.config.from_object(Config)
    # 2.3.0以上版本
    # app.json.ensure_ascii = False
    
    #初始化SQLAlchemy对象
    db.init_app(app)
    
    #注册蓝图
    from flask_shop.user import user_bp
    app.register_blueprint(user_bp)
    
    return app





