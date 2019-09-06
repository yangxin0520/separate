from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from gather.utils.commons import ReConverter
from gather.utils.exts import db
from gather.utils.models import Users
# import redis


# 创建redis连接对象,暂时用不到
redis_store = None


# 工厂模式
def create_app(config_name):
    """
    创建flask应用对象
    :param config_name: str 配置模式的名字 （"develop", "product"）
    :return: flask应用对象
    """

    app = Flask(__name__)
    from os import urandom
    app.config['SECRET_KEY'] = urandom(50)

    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)


    # 初始化redis工具
    # global redis_store
    # redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # # 利用flask-session，将session保存到redis中
    # Session(app)

    # 为flask添加csrf防护
    # CSRFProtect(app)

    # 为flask添加自定义的转换器
    app.url_map.converters["re"] = ReConverter

    # 注册蓝图
    # 使用绝对路径注册api_1_0蓝图
    from gather import api_1_0
    # app.register_blueprint(api_1_0.api, url_prefix="/api/V1.0")
    app.register_blueprint(api_1_0.api)

    # 注册静态文件的蓝图
    from gather.web_html import html
    app.register_blueprint(html)

    return app
