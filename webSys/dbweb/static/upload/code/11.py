# -*- coding:utf-8 -*-
import numpy as np

start = '2015-01-01'  # �ز���ʼʱ��
end = '2015-12-31'  # �ز����ʱ��
universe = ['600000']  # ֤ȯ��
capital_base = 1000000  # ��ʼ�ʽ�
freq = 'd'  # �������� 'd'��ʾʹ�����߻ز� 'm'��ʾ���ڲ���ʹ�÷���
refresh_rate = 5  # ����Ƶ��, ��ʾhandle_data��ʱ����


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