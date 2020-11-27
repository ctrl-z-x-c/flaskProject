from flask import Flask
from settings import Config
from apps.views.user_view import user_bp


def create_app():
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(Config)

    # 注册蓝图
    app.register_blueprint(user_bp)

    return app
