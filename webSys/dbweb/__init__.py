#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'user.signin'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Register all the filter.
    from .util import filter_blueprint
    app.register_blueprint(filter_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    # from .group import group as group_blueprint
    # app.register_blueprint(group_blueprint, url_prefix='/group')
    from .category import category as category_blueprint
    app.register_blueprint(category_blueprint, url_prefix='/category')
    from .article import article as article_blueprint
    app.register_blueprint(article_blueprint, url_prefix='/article')
    from .stock import stock as stock_blueprint
    app.register_blueprint(stock_blueprint, url_prefix='/stock')
    from .search import search as search_blueprint
    app.register_blueprint(search_blueprint, url_prefix='/search')
    from .algo import algo as algo_blueprint
    app.register_blueprint(algo_blueprint, url_prefix='/algo')

    return app
