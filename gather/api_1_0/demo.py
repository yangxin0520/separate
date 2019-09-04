# 使用相对路径导入api
from . import api


@api.route('/index')
def index():
    return 'index page'
