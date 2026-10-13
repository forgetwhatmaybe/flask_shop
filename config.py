
import os


class Config:
    MYSQL_DIALECT = 'mysql'
    MYSQL_DRIVER = 'pymysql'
    MYSQL_USERNAME = os.getenv('MYSQL_USERNAME', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')
    MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'flask_shop')
    MYSQL_CHARSET = os.getenv('MYSQL_CHARSET', 'utf8mb4')
    
    #设置json数据不实用ASCII编码，保证中文数据正常显示
    JSON_AS_ASCII = False
    RESTFUL_JSON = {'ensure_ascii': False}
    
    
    SQLALCHEMY_DATABASE_URI = f'{MYSQL_DIALECT}+{MYSQL_DRIVER}://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset={MYSQL_CHARSET}'
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-only-change-me')
    DEBUG = True
    #设置token的过期时间，单位为秒
    JWT_EXPIRATION_DELTA = 60*60*24*7
    
    
    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    pass

config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig 
}