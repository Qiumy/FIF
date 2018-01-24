#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import current_app
from .. import db
from ..models import Stock
import tushare as ts, json
import datetime
from yahoo_finance import Share


def get_stock(code):
    stock = Stock.query.filter_by(code=code).first()
    if stock == None:
        with current_app.open_resource('stock.json') as f:
            stock_dic = json.loads(f.read())
        stock = Stock(code=code, name=stock_dic[code])
        db.session.add(stock)
        db.session.commit()
    return stock


# 制造一个个人页面股票实时价格对比的数据结构
def get_profit_stock_list(user_stock_list):
    profit_stock_list = []
    # 对基本属性赋值
    for user_stock in user_stock_list:
        profit_stock = {}
        profit_stock['code'] = user_stock.stock.code
        profit_stock['name'] = user_stock.stock.name
        profit_stock['average_price'] = user_stock.average_price
        profit_stock['real_price'] = float(Share(user_stock.stock.code).get_price())
        profit_stock['own_num'] = user_stock.own_num
        profit_stock['mark_value'] = profit_stock['own_num'] * profit_stock['real_price']
        profit_stock['cost'] = profit_stock['own_num'] * profit_stock['average_price']
        profit_stock_list.append(profit_stock)
    return profit_stock_list


# 获取总资产、总收益与总收益率
def get_user_profit(profit_stock_list):
    user_profit = {}
    all_mark_value = 0
    all_cost = 0
    for profit_stock in profit_stock_list:
        all_mark_value += profit_stock['mark_value']
        all_cost += profit_stock['cost']
    user_profit['all_mark_value'] = all_mark_value
    user_profit['all_cost'] = all_cost
    user_profit['all_profit'] = user_profit['all_mark_value'] - user_profit['all_cost']
    if all_cost == 0:
        all_profit_ratio = 0
    else:
        all_profit_ratio = user_profit['all_profit'] / user_profit['all_cost']
    user_profit['all_profit_ratio'] = all_profit_ratio
    return user_profit

def check_trade():
    a_time = datetime.datetime.utcnow()+datetime.timedelta(hours=0, minutes=20)
    hour = a_time.hour
    minute = a_time.minute
    if hour==9:
        if minute >= 30:
            return True
        else:
            return False
    if 10 <= hour < 16:
        return True
    else:
        return False
