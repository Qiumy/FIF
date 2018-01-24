#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    SECRET_KEY = os.environ.get('SECRET_KEY') or '!@#$%^&*12345678'
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # If use QQ email, please see http://service.mail.qq.com/cgi-bin/help?id=28 firstly.
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'web_stock@126.com'   # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'qwer1234'               # os.environ.get('MAIL_PASSWORD')
    FORUM_MAIL_SUBJECT_PREFIX = 'Fun-in-Fund'
    FORUM_MAIL_SENDER = '<web_stock@126.com>'

    # BABEL_DEFAULT_LOCALE = 'zh'
    BABEL_DEFAULT_TIMEZONE = 'CST'

    PER_PAGE = 10
    # UPLOAD_FOLDER = os.path.join(basedir, 'dbweb/static/upload')
    UPLOAD_FOLDER = os.path.join(basedir, 'dbweb','static','upload')
    # GROUP_UPLOAD_FOLDER = os.path.join(basedir, 'dbweb/static/upload/group_logo')
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    MAX_CONTENT_LENGTH = 512 * 1024

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    def __init__(self):
        pass

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               'mysql://root:@localhost/website')


class ProductionConfig(Config):
    def __init__(self):
        pass

    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               'mysql://root:@localhost/website')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
