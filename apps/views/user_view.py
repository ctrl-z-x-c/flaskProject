from flask import Blueprint, request, render_template, session, make_response

import models

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/')
def user_index():
    if request.cookies.get('user_pwd') == '':
        return render_template('login.html')
    elif request.cookies.get('user_pwd') == session['user_pwd']:
        return render_template('index.html', name=session['name'], psw=session['psw'])


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = dict(request.form)
        # print(data)
        print(request.cookies.get('user_pwd'))
        print(session)
        try:
            if request.cookies.get('user_pwd') == session['user_pwd']:
                return '免登录'
        except:
            pass
        if models.compare(data['name'], data['psw']):
            # 设置cookie
            resp = make_response(render_template('index.html', name=data['name'], psw=data['psw']))
            resp.set_cookie('user_pwd', data['name'] + data['psw'], max_age=300)
            # resp.set_cookie('user_pwd', 'iamcookie', max_age=300)
            print(resp)
            print(request.cookies.get('user_pwd'))
            session.permanent = True
            session['user_pwd'] = data['name'] + data['psw']
            session['name'] = data['name']
            session['psw'] = data['psw']
            print(session)
            print(session['user_pwd'])
            return resp
            # return render_template('index.html', name=data['name'], psw=data['psw'])
        else:
            return {'错误': '账号或密码错误'}
    else:
        return render_template('login.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = dict(request.form)
        models.add(data['name'], data['psw'])
        return '注册成功'
    else:
        return render_template('register.html')
