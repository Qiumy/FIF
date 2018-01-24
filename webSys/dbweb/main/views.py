#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template
from . import main
from flask_babel import gettext
from ..models import Article, Stock, News, Follow_Stock
import tushare as ts, json
import datetime
from ..util.get_yahoo_news import getLatestNews
from flask_login import login_required, current_user


@main.route('/')
def index():
    whole_indicators = json.loads(ts.get_index()[:4].to_json(orient='records'))

    getLatestNews()
    whole_news = News.query.order_by(News.time.desc()).limit(7)
    # 站点公告
    notice = Article.query.order_by(Article.updated_time.desc()).limit(7)

    dates = datetime.datetime.now()
    week = datetime.datetime.now().weekday()
    if week in [5, 6]:
        days = 4 - week
        dates = dates + datetime.timedelta(days=days)
    dates = dates.strftime('%Y-%m-%d')

    recommend_stocks = Stock.query.filter(Stock.code != 'ALL').limit(8).all()
    if current_user.is_authenticated:
        for i in range(len(recommend_stocks)):
            if Follow_Stock.query.filter_by(user_id=current_user.id,
                                            stock_id=recommend_stocks[i].code).first() is not None:
                recommend_stocks[i].flag = True
            else:
                recommend_stocks[i].flag = False

    return render_template('main/index.html',
                           whole_indicators=whole_indicators,
                           news=whole_news,
                           notices=notice,
                           dates=dates,
                           stocks=recommend_stocks)


@main.app_errorhandler(404)
def page_404(err):
    return render_template('404.html', title='404'), 404


@main.app_errorhandler(403)
def page_403(err):
    return render_template('403.html', title='403'), 403


@main.app_errorhandler(500)
def page_500(err):
    return render_template('500.html', title='500'), 500
