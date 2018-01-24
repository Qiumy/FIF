# -*- coding:utf-8 -*-
import numpy as np

start = '2016-06-01'  # 回测起始时间
end = '2016-12-01'  # 回测结束时间
stock_starting_cash = 100000 # 初始持有资金
benchmark = '000300.XSHG'


def init(context):
    logger.info("init")
    context.s1 = "000001.XSHE"
    update_universe(context.s1)
    context.fired = False


def before_trading(context):
    pass


def handle_bar(context, bar_dict):
    if not context.fired:
        # order_percent并且传入1代表买入该股票并且使其占有投资组合的100%
        order_percent(context.s1, 1)
        context.fired = True