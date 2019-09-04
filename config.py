import os
import redis
from flask_session import Session


SECRET_KEY = os.urandom(24)


class config_basic(object):
    """基本配置信息"""

    # 数据库配置
    DIALECT = 'mysql'
    DRIVER = 'mysqlconnector'
    USERNAME = 'root'
    PASSWORD = 'root'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask'
    # SQLALCHEMY_DATABASE_URI--连接数据库制指定变量
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
    # 这行代码防止报错（不影响的报错）
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-Session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 对cookie中的session_id进行隐藏处理
    SESSION_USE_SIGNER = True
    # 设置session的有效期，单位为秒
    PERMANENT_SESSION_LIFETIME = 86400


class config_development(config_basic):
    """开发模式的配置信息"""
    # debug模式
    DEBUG = True


class config_production(config_basic):
    """生产环境配置信息"""
    pass


# 映射类
config_map = {
    "develop": config_development,
    "product": config_production
}












