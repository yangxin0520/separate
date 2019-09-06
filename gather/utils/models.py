from gather.utils.exts import db


# 创建用户登陆Users模型
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)


class Users2(db.Model):
    """这是一个创建users2表的ORM模型"""
    __tablename__ = 'users2'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
