from flask import Blueprint

# 创建蓝图对象
api = Blueprint("api_1_0", __name__)


# 导入蓝图视图函数
from . import demo

# 导入Test视图函数
from . import test

# 导入登陆视图函数
from . import login_register