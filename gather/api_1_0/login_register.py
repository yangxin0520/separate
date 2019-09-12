# 使用相对路径导入api
from . import api
from flask import Flask, jsonify, request, session
from gather.utils.exts import db
from gather.utils.models import Users



@api.route('/login', methods=['POST'])
def login():
    userid = request.form.get('username')
    password = request.form.get('password')
    # 在数据库进行username和password匹配
    user_login = Users.query.filter(Users.username == userid, Users.password == password).first()
    # 如果都匹配正确
    if user_login:
        # 生成session
        session['session_username'] = userid
        # 给前端返回json数据
        return jsonify({
            'status': 1,
            'message': '登陆成功'
        })
    else:
        # 给前端返回json数据
        return jsonify({
            'status': 0,
            'message': '登陆失败'
        })


@api.route('/register', methods=['POST'])
def register():
    userid = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    # 将邮箱与数据库已知邮箱数据对比
    user_register = Users.query.filter(Users.email == email).first()
    # 如果已存在该邮箱
    if user_register:
        # 返回json数据
        return jsonify({
            'status': 1,
            'message': '该邮箱已注册'
        })
    # 如果邮箱没有重复，那么继续往下判断两次输入密码
    else:
        if password != password2:
            # 返回json数据
            return jsonify({
                'status': 2,
                'message': '两次输入密码不一致'
            })
        else:
            # 如果两次密码输入一致，开始像数据库中插入数据
            user = Users(username=userid, email=email, password=password)
            # 插入命令
            db.session.add(user)
            # 确认插入命令
            db.session.commit()
            # 返回json数据
            return jsonify({
                'status': 3,
                'message': '注册成功'
            })