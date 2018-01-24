# -*- coding:utf-8 -*-


import tushare as ts
# from ..util.tmpstrategy import *
import tmpstrategy

class myException(Exception):
    pass


# start = start
# end = end
# universe = universe
# capital_base = capital_base
# freq = freq
# refresh_rate = refresh_rate

start = tmpstrategy.start
end = tmpstrategy.end
universe = tmpstrategy.universe
capital_base = tmpstrategy.capital_base
freq = tmpstrategy.freq
refresh_rate = tmpstrategy.refresh_rate

import numpy as np


class Account:
    def __init__(self):
        self.capital_base = capital_base
        self.universe = universe
        self.history = {}
        self.position = {}
        self.curday = 0

    def getSingleHis(self, code):
        return ts.get_k_data(code=code, start=start, end=end)['close'].astype(np.float64)

    def getUniverseHis(self):
        his = {}
        for stock in self.universe:
            his[stock] = self.getSingleHis(stock)
        return his

    def sell(self, stock, nums):
        # print("+++++sell+++++")
        if self.position.get(stock, 0) > nums and stock in self.universe:
            self.position[stock] = self.position.get(stock, 0) + nums
            self.capital_base += nums * self.getcurPrice()
        else:
            # print("you don't have enough stock num")
            pass
    def buy(self, stock, nums):
        # print("---buy---")
        if self.capital_base > nums * self.getcurPrice()[stock]:
            self.position[stock] = self.position.get(stock, 0) + nums
            self.capital_base -= nums * self.getcurPrice()[stock]
        else:
            # print("you don't have enough stock num")
            pass
    def getHistoryPrice(self, days):
        self.history = self.getUniverseHis()
        daysHis = {}
        for stock in self.universe:
            daysHis[stock] = self.history[stock][self.curday:self.curday + days + 1]
        return daysHis

    def getcurPrice(self):
        dayCurPrice = {}
        for stock in universe:
            dayCurPrice[stock] = self.history[stock][self.curday]
        return dayCurPrice

    def backtest(self):
        import time
        t0 = time.time()
        for stock in self.universe:
            close = len(self.getUniverseHis()[stock])
            break
        print(close)
        for day in range(close):
            # print("=======",day)
            tmpstrategy.handle_data(self)
            # print(self.capital_base)
            self.curday += 1

        t1 = time.time()
        print("loop time:", t1 - t0)


if __name__ == '__main__':
    import time
    t0 = time.time()

    a = Account()
    a.backtest()

    t1 = time.time()
    print(t1-t0)
