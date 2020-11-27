from flask import Blueprint, request, render_template, \
    session, make_response, redirect

import models

user_bp = Blueprint('user', __name__, url_prefix='/user')


# 进入页面，如果有session信息则进入主页，没有则跳转登录界面
@user_bp.route('/')
def user_index():
    #  没有 session
    if not request.cookies.get('session'):
        return render_template('login.html')
    # 有session，并返回session信息
    elif session:
        return render_template('index.html', name=session['data']['name'], pw=session['data']['pwd'])
    return '跳转错误'


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    # 接收登录信息
    if request.method == 'POST':
        data = dict(request.form)
        # 如果有session信息则跳到主页
        if session:
            if data['name'] in session:
                # 免登录
                return redirect('/user')
        else:
            # 验证账号密码是否正确
            if models.User.compare(data['name'], data['pwd']):
                # 设置session，并返回主页
                resp = make_response(render_template('index.html', name=data['name'], pwd=data['pwd']))
                session.permanent = True
                session[data['name']] = {}
                # 账号其他信息
                session['data'] = {'name': data['name'], 'pwd': data['pwd']}
                return resp

            else:
                # 账号密码不在库
                return {'错误': '账号或密码错误'}
    else:
        # get请求返回的登录界面
        return render_template('login.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = dict(request.form)
        if not models.User.compare(data['name'], data['pwd']):
            models.User.add(data['name'], data['pwd'])
        else:
            return '账号已存在'
        return '注册成功'
    else:
        return render_template('register.html')
