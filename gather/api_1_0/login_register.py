# 使用相对路径导入api
from . import api
from flask import Flask, jsonify, request, render_template, session
from gather.utils.exts import db
from gather.utils.models import Users

@api.route('/login', methods=['GET', 'POST'])
def login():

    # 如果请求是GET请求，则跳转页面到login.html
    if request.method == 'GET':
        return jsonify({
            'status': 1,
            'message': '登陆成功'
        })
    # 如果请求时POST请求，则跳转页面到登陆判断逻辑
    elif request.method == 'POST':
        return jsonify({
            'status': 0,
            'message': '成功'
        })
        # # 获取前端发送来的用户名和密码
        # userid = request.form.get('username')
        # password = request.form.get('password')
        # # 在数据库进行username和password匹配
        # user_login = Users.query.filter(Users.username == userid, Users.password == password).first()
        # # 如果都匹配正确
        # if user_login:
        #     # 生成session
        #     # session['session_username'] = userid
        #     # 给前端返回json数据
        #     return jsonify({
        #         'status': 1,
        #         'message': '登陆成功'
        #     })
        # else:
        #     # 给前端返回json数据
        #     return jsonify({
        #         'status': 0,
        #         'message': '登陆失败'
        #     })