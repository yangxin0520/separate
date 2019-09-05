# 使用相对路径导入api
from . import api
from gather import db


@api.route('/index')
def index():
    return 'index page'
