#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db, login_manager


# 用户持股的多对多中介模型
class User_Stock(db.Model):
    def __init__(self, user, stock, average_price, own_num):
        self.user_id = user.id
        self.stock_id = stock.code
        self.average_price = average_price
        self.own_num = own_num

    __tablename__ = 'user_stock'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    stock_id = db.Column(db.String(16), db.ForeignKey('stocks.code'), primary_key=True)
    average_price = db.Column(db.Float, default=0)
    own_num = db.Column(db.Integer, default=0)


class Follow_Stock(db.Model):
    def __init__(self, user, stock):
        self.user_id = user.id
        self.stock_id = stock.code

    __tablename__ = 'follow_stock'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    stock_id = db.Column(db.String(16), db.ForeignKey('stocks.code'), primary_key=True)


""" 用户管理模块 """

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    balance = db.Column(db.Float, default=200000)

    is_password_reset_link_valid = db.Column(db.Boolean, default=True)
    is_valid_registered = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime(), default=datetime.utcnow)
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)

    # 权限: 0. 管理员, 1. 普通用户
    permissions = db.Column(db.Integer, default=1, nullable=False)
    avatar_url = db.Column(db.String(64),
                           default="/static/images/default_avatar.jpg")

    # 个人信息, 包括电话号码, 身份证号码, 个人座右铭等。
    telephone = db.Column(db.String(32))
    personal_id = db.Column(db.String(32))
    personal_profile = db.Column(db.Text(), nullable=True)

    # 用户创建话题, 回复等, 一对多的关系
    topics = db.relationship('Topic', backref='user', lazy='dynamic')
    topic_num = db.Column(db.Integer, default=0, nullable=False)

    posts = db.relationship('Post', backref='user', lazy='dynamic')
    post_num = db.Column(db.Integer, default=0, nullable=False)

    # 用户创建策略
    strategy = db.relationship('Strategy', backref='user', lazy='dynamic')
    strategy_num = db.Column(db.Integer, default=0, nullable=False)

    # 用户持仓：用户与股票之间是多对多关系
    stocks = db.relationship('Stock',
                             secondary=User_Stock.__table__,
                             backref=db.backref('users'),
                             lazy='dynamic')

    trade_list = db.relationship('Trade',
                                 backref=db.backref('user'),
                                 lazy='dynamic')

    user_stock_list = db.relationship('User_Stock',
                                      backref=db.backref('user'),
                                      lazy='dynamic')

    user_follow_list = db.relationship('Follow_Stock',
                                       backref=db.backref('user'),
                                       lazy='dynamic'
                                       )

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_reset_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        uid = data.get('id')
        if uid:
            return User.query.get(uid)
        return None


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


'''股票交易功能'''

# 股票信息
class Stock(db.Model):
    def __init__(self, code, name):
        self.code = code
        self.name = name

    __tablename__ = 'stocks'
    code = db.Column(db.String(16), primary_key=True)
    name = db.Column(db.String(32))

    user_stock_list = db.relationship('User_Stock',
                                      backref=db.backref('stock'),
                                      lazy='dynamic')

# 模拟交易信息
class Trade(db.Model):
    def __init__(self, user, stock, num, price, is_buy):
        self.user_id = user.id
        self.stock_id = stock.code
        self.num = num
        self.price = price
        self.is_buy = is_buy

    __tablename__ = 'trades'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    stock_id = db.Column(db.String(16), db.ForeignKey('stocks.code'))
    num = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, default=0)
    is_buy = db.Column(db.Boolean, default=True)  # True代表买入，False代表卖出
    trade_time = db.Column(db.DateTime(), default=datetime.utcnow)


# 股票预测信息
class StockPre(db.Model):
    def __init__(self, stock, date, inc, dec):
        self.stock_id = stock.code
        self.date = date
        self.inc = inc
        self.dec = dec

    __tablename__ = 'predicts'
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.String(16), db.ForeignKey('stocks.code'))
    date = db.Column(db.Date, default=datetime.now().date())
    inc = db.Column(db.Float, default=0)
    dec = db.Column(db.Float, default=0)

'''互动社区功能'''

#
# class Group(db.Model):
#     def __init__(self, title, about):
#         self.title = title
#         self.about = about
#         self.created_time = datetime.now()
#
#     __tablename__ = 'groups'
#     id = db.Column(db.Integer, primary_key=True)  # 专栏 ID
#     title = db.Column(db.String(64), nullable=False)  # 专栏名字
#     about = db.Column(db.Text(), nullable=False)  # 专栏介绍
#     logo = db.Column(db.String(128))  # 专栏Logo 的 URL
#     topic_num = db.Column(db.Integer, default=0)  # 专栏话题数目
#     created_time = db.Column(db.DateTime(), default=datetime.utcnow)
#
#     # 专栏内的话题，一对多的关系
#     topics = db.relationship('Topic', backref='group', lazy='dynamic')

'''
@Category
话题的类型
'''

class Category(db.Model):
    def __init__(self, title):
        self.title = title

    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)

class Topic(db.Model):
    def __init__(self, user_id, title, content, cat_type):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.time_created = datetime.now()
        self.updated_time = datetime.now()
        self.cat_type = cat_type
        # self.group_id = group_id

    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)  # 话题 ID
    title = db.Column(db.String(64), nullable=False)  # 话题标题
    content = db.Column(db.Text(), nullable=False)  # 话题内容
    visit_num = db.Column(db.Integer, default=0)  # 话题浏览次数
    post_num = db.Column(db.Integer, default=0)  # 评论次数
    # group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))  # 所属专栏的ID
    cat_type = db.Column(db.Integer, db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 创建用户的ID

    created_time = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_time = db.Column(db.DateTime(), default=datetime.utcnow)

    # 话题的评论，一对多的关系
    posts = db.relationship('Post', backref='topic', lazy='dynamic')


class Post(db.Model):
    def __init__(self, user_id, content):
        self.content = content
        self.user_id = user_id
        self.createdTime = datetime.now()

    __tablename = "posts"
    id = db.Column(db.Integer, primary_key=True)  # 评论的ID
    content = db.Column(db.String(1024), nullable=False)  # 评论内容

    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))  # 所属话题的ID
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 回复用户的ID
    created_time = db.Column(db.DateTime(), default=datetime.utcnow)


"""
@Article: 用来发布站点公告。
"""


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)  # 站点公告 ID
    title = db.Column(db.String(64), nullable=False)  # 站点公告标题
    content = db.Column(db.Text(), nullable=False)  # 站点公告正文
    visit_num = db.Column(db.Integer, default=0)  # 浏览次数

    updated_time = db.Column(db.DateTime(), default=datetime.utcnow)

"""
@News
"""

class News(db.Model):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime())
    tag = db.Column(db.String(50))


'''
@Strategy
ID， 名字， 代码， 修改时间， 用户ID，
'''
class Strategy(db.Model):
    def __int__(self, name, code, user_id):
        self.name = name
        self.code = code
        self.user_id = user_id

    __tablename__="codes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.Text(), nullable=False)
    note = db.Column(db.Text())
    modified_time = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

'''
@RunResult
ID, 开始时间，结束时间，回测时间，代码ID， 收益， 耗时，备注
'''
class RunResult(db.Model):
    __tablename__='run_result'
    id = db.Column(db.Integer, primary_key=True)
    begin_time = db.Column(db.Date(), default=datetime.date(datetime.now()))
    end_time = db.Column(db.Date(), default=datetime.date(datetime.now()))
    run_time = db.Column(db.DateTime(), default=datetime.utcnow)
    code_id = db.Column(db.Integer, db.ForeignKey('codes.id'))
    profit = db.Column(db.Float, default=0.0)
    last_time = db.Column(db.Float, default=0.0)
