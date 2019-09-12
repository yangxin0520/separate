from flask import Blueprint, make_response
from gather.utils.captcha import Captcha
from io import BytesIO
from gather import redis_store
from gather import constants
from . import api




@api.route('/image_codes/<image_code_id>')
def graph_captcha(image_code_id):
    text, image = Captcha.gene_graph_captcha()
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    redis_store.setex("image_code_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    return resp


# 测试用 先注释掉
# @api.route('/test_ses/')
# def test_ses():
#     new_captcha = CaptchaTool()
#     img, code = new_captcha.get_verify_code()
#     print(img, code)
#     return 'ok'
#
#
# @api.route("/set_session")
# def set_session():
#     """设置session"""
#     redis_store.set("user", "xiaomuing")
#     # session["username1"] = "小明"
#     return "ok"