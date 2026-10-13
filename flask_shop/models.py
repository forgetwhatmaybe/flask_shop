from flask_shop import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True
    
    create_time = db.Column(db.DateTime,nullable=False,default=datetime.now)
    update_time = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)


class User(BaseModel):
    __tablename__ = 't_users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32),unique=True ,nullable=False)
    pwd = db.Column(db.String(255),nullable=False)
    nick_name = db.Column(db.String(32))
    phone = db.Column(db.String(11),unique=True)
    email = db.Column(db.String(64),unique=True)


    @property
    def password(self):
        return self.pwd
    
    @password.setter
    def password(self, pwd):
        self.pwd = generate_password_hash(pwd)
        
    def check_password(self, pwd):
        return check_password_hash(self.pwd, pwd)