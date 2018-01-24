# -*- coding:utf-8 -*-
import numpy as np

start = '2015-01-01'  # 回测起始时间
end = '2015-12-31'  # 回测结束时间
universe = ['600000']  # 证券池
capital_base = 1000000  # 起始资金
freq = 'd'  # 策略类型 'd'表示使用日线回测 'm'表示日内策略使用分钟
refresh_rate = 5  # 调仓频率, 表示handle_data的时间间隔


def handle_data(account):
    closePrice_history = account.getHistoryPrice(5)
    print("*************====**",closePrice_history)
    for stock in account.universe:
        avg_price = sum(closePrice_history[stock]) / 5
        last_price = account.getcurPrice()[stock]
        if last_price > 1.0 * avg_price:
            account.buy(stock, 100)
        else:
            account.sell(stock, 10)