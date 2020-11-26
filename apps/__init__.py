from flask import Flask

from apps.views.cookies import cookie
from apps.views.sessions import sess
from settings import Config
from apps.views.user_view import user_bp
# from flask_script import Manager


def create_app():
    app=Flask(__name__)
    #加载配置
    app.config.from_object(Config)
    app.config['SECRET_KEY']='123456'
    app.config['PERMANENT_SESSION_LIFETIME']=7*24*60


    #注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(cookie)
    app.register_blueprint(sess)
    #app=Manager(app)
    return app