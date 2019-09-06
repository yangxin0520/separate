# 使用相对路径导入api
from . import api
from gather.utils.exts import db
from gather.utils.models import Users

@api.route('/test')
def test():
    db.session.add(Users(username = "yangxin", email = "7979@163.com", password = "123"))
    db.session.commit()
    db.session.close()
    return 'test page'