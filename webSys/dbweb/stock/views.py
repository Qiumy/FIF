#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, url_for, current_app, request
from . import stock
from .. import db
from ..util.get_stock import get_stock, check_trade
from ..models import User, Stock, User_Stock, Trade, StockPre, Follow_Stock, News
from flask_login import login_required, current_user
from flask_babel import gettext
import tushare as ts, datetime, json
import datetime
from yahoo_finance import Share
from ..models import Stock
import urllib.request

DELTA_DAYS = 360


# index
@stock.route('/')
def index():
    stocks = Stock.query.filter(Stock.code != 'ALL').limit(8).all()
    if current_user.is_authenticated:
        for i in range(len(stocks)):
            if Follow_Stock.query.filter_by(user_id=current_user.id, stock_id=stocks[i].code).first() is not None:
                stocks[i].flag = True
            else:
                stocks[i].flag = False
    return render_template('stock/index.html',
                           stocks=stocks)


@stock.route('/allstock/')
def allstock():
    dates = datetime.datetime.now()
    week = datetime.datetime.now().weekday()
    if week in [5, 6]:
        days = 4 - week
        dates = dates + datetime.timedelta(days=days)
    dates = dates.strftime('%Y-%m-%d')

    whole_indicators = json.loads(ts.get_index().to_json(orient='records'))
    return render_template('stock/all_stock.html',
                           whole_indicators=whole_indicators,
                           dates=dates)


# single stock <code>
@stock.route('/<code>/')
def stock_view(code):
    DELTA_DAYS = 365
    end = datetime.datetime.now().date()
    start = end - datetime.timedelta(days=DELTA_DAYS)
    stockData = Share(code)
    stockHisData = stockData.get_historical(start_date=str(start), end_date=str(end))
    stock = Stock.query.filter_by(code=code).first()
    preInfo = StockPre.query.filter_by(stock_id=code, date=end).first() or StockPre.query.filter_by(stock_id="ALL",
                                                                                                    date=end).first()
    news = News.query.order_by(News.time.desc()).limit(7)
    return render_template('stock/stock.html',
                           title='stock detail',
                           stockHisData=stockHisData,
                           stock=stock,
                           preInfo=preInfo,
                           news=news)


@stock.route('/buy/<code>/', methods=['GET', 'POST'])
@login_required
def buy(code):
    # 获取股票以及持股关系的实例
    stock = get_stock(code)
    user_stock = User_Stock.query.filter_by(user_id=current_user.id, stock_id=stock.code).first()
    if user_stock == None:
        own_num = 0
    else:
        own_num = user_stock.own_num
    preInfo = StockPre.query.filter_by(stock_id=code,
                                       date=datetime.datetime.now().date()).first() or StockPre.query.filter_by(
        stock_id="ALL", date=datetime.datetime.now().date()).first()
    news = News.query.order_by(News.time.desc()).limit(7)
    is_trade = check_trade()
    if request.method == 'GET':
        return render_template('stock/trade_buy.html',
                               title='Stock Trade-' + stock.name,
                               code=code,
                               name=stock.name,
                               balance=current_user.balance,
                               own_num=own_num,
                               preInfo=preInfo,
                               news=news,
                               is_trade=is_trade)

    if request.method == 'POST':
        buy_num = int(request.form['buy_num'])
        price = float(request.form['price'])
        # 判断交易能否成功
        if current_user.balance - buy_num * price < 0:
            return render_template('stock/trade_buy.html',
                                   title='Stock Trade-' + stock.name,
                                   code=code,
                                   name=stock.name,
                                   balance=current_user.balance,
                                   own_num=own_num,
                                   preInfo=preInfo,
                                   news=news,
                                   message_done=u'Insufficient Balance！')

        # 写入交易记录，并更新用户余额
        trade = Trade(user=current_user, stock=stock, num=buy_num, price=price, is_buy=True)
        db.session.add(trade)
        current_user.balance = current_user.balance - price * buy_num
        db.session.commit()

        # 更新持股关系
        if user_stock == None:
            user_stock = User_Stock(user=current_user, stock=stock, average_price=price, own_num=0)
            db.session.add(user_stock)
        user_stock.average_price = (user_stock.own_num * user_stock.average_price + buy_num * price) / (
            user_stock.own_num + buy_num) if (user_stock.own_num + buy_num) != 0 else 0
        user_stock.own_num = user_stock.own_num + buy_num
        db.session.commit()

        return render_template('stock/trade_buy.html',
                               title='Stock Trade-' + stock.name,
                               code=code,
                               name=stock.name,
                               balance=current_user.balance,
                               own_num=user_stock.own_num,
                               preInfo=preInfo,
                               news=news,
                               message_done=u'Success！')


@stock.route('/sell/<code>/', methods=['GET', 'POST'])
@login_required
def sell(code):
    # 获取股票以及持股关系的实例
    stock = get_stock(code)
    user_stock = User_Stock.query.filter_by(user_id=current_user.id, stock_id=stock.code).first()
    if user_stock == None:
        own_num = 0
    else:
        own_num = user_stock.own_num
    preInfo = StockPre.query.filter_by(stock_id=code,
                                       date=datetime.datetime.now().date()).first() or StockPre.query.filter_by(
        stock_id="ALL", date=datetime.datetime.now().date()).first()
    news = News.query.order_by(News.time.desc()).limit(7)
    is_trade = check_trade()

    if request.method == 'GET':
        return render_template('stock/trade_sell.html',
                               title='Stock Trade--' + stock.name,
                               name=stock.name,
                               code=code,
                               balance=current_user.balance,
                               own_num=own_num,
                               preInfo=preInfo,
                               news=news,
                               is_trade=is_trade)

    if request.method == 'POST':
        sell_num = int(request.form['sell_num'])
        price = float(request.form['price'])

        # 判断交易是否成功
        if user_stock == None or sell_num > user_stock.own_num:
            return render_template('stock/trade_sell.html',
                                   title='Stock Trade--' + stock.name,
                                   name=stock.name,
                                   code=code,
                                   balance=current_user.balance,
                                   own_num=own_num,
                                   preInfo=preInfo,
                                   news=news,
                                   message_done="You do not have enough volume！")

        # 写入交易记录，并更新用户余额
        trade = Trade(user=current_user, stock=stock, num=sell_num, price=price, is_buy=False)
        db.session.add(trade)
        current_user.balance = current_user.balance + price * sell_num
        db.session.commit()

        # 更新持股关系
        if user_stock.own_num == sell_num:
            user_stock.average_price = 0
            user_stock.own_num = 0
            db.session.delete(user_stock)
            db.session.commit()
        else:
            user_stock.average_price = (user_stock.own_num * user_stock.average_price - sell_num * price) / (
                user_stock.own_num - sell_num)
            user_stock.own_num = user_stock.own_num - sell_num
        db.session.commit()

        return render_template('stock/trade_sell.html',
                               title='Stock Trade-' + stock.name,
                               code=code,
                               name=stock.name,
                               balance=current_user.balance,
                               own_num=user_stock.own_num,
                               preInfo=preInfo,
                               news=news,
                               message_done='Success！')


@stock.route('/list/<code>/', methods=['GET', 'POST'])
@login_required
def list(code):
    # 获取股票以及持股关系的实例
    stock = get_stock(code)
    trade_list = current_user.trade_list.filter_by(stock_id=code)
    preInfo = StockPre.query.filter_by(stock_id=code,
                                       date=datetime.datetime.now().date()).first() or StockPre.query.filter_by(
        stock_id="ALL", date=datetime.datetime.now().date()).first()
    news = News.query.order_by(News.time.desc()).limit(7)
    return render_template('stock/trade_list.html',
                           title='Trade List',
                           code=code,
                           name=stock.name,
                           trade_list=trade_list,
                           preInfo=preInfo,
                           news=news)


@stock.route('/real/<code>/')
def real_data(code):
    stockData = Share(code)
    # stockData.refresh()
    # print([stockData.get_trade_datetime(), stockData.get_price()])
    return json.dumps([stockData.get_trade_datetime(), stockData.get_price()])

    # url = "http://finance.yahoo.com/d/quotes.csv?s=" + code + "&f=" + "t1l1d1"
    # req = urllib.request.Request(url)
    # req.add_header('User-Agent',
    #                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    # response = urllib.request.urlopen(req).read().decode()
    #
    # print(json.dumps([response]))
    # return json.dumps([response])


@stock.route('/follow/<code>/', methods=["GET"])
@login_required
def follow(code):
    stock = get_stock(code)
    follow = Follow_Stock(user=current_user, stock=stock)
    db.session.add(follow)
    db.session.commit()
    return "Success!"


@stock.route('/unfollow/<code>/', methods=["GET"])
@login_required
def unfollow(code):
    stock = get_stock(code)
    follow = Follow_Stock.query.filter_by(user_id=current_user.id, stock_id=stock.code).first()
    db.session.delete(follow)
    db.session.commit()
    return "Success!"
