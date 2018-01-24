#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import current_app
import pickle as pkl
import numpy as np


def get_max_dd_ddd(xs):
    index = xs.index
    xs = xs.values
    ans = {}

    max_dd_end = np.argmax(np.maximum.accumulate(xs) / xs)
    if max_dd_end == 0:
        max_dd_end = len(xs) -1
    max_dd_start = np.argmax(xs[:max_dd_end]) if max_dd_end > 0 else 0

    al_cum = np.maximum.accumulate(xs)
    a = np.unique(al_cum, return_counts=True)
    start_idx = np.argmax(a[1])
    m = a[0][start_idx]
    al_cum_array = np.where(al_cum == m)
    max_ddd_start_day = al_cum_array[0][0]
    max_ddd_end_day = al_cum_array[0][-1]

    ans = {'max_dd_end':index[max_dd_end], 'max_dd_start':index[max_dd_start], 'max_ddd_start_day':index[max_ddd_start_day], 'max_ddd_end_day':index[max_ddd_end_day]}
    return ans

def get_backtest_result(filepath):
    result = {}
    with open(filepath, 'rb') as f:
        data = pkl.load(f)
        result['summary'] = data['summary']
        result['benchmark'] = data['benchmark_portfolio']['unit_net_value'].to_json()
        result['portfolio'] = data['portfolio']['unit_net_value'].to_json()
        xs = data['portfolio']['unit_net_value'] * data['portfolio']['units']
        max_dd_ddd_day = get_max_dd_ddd(xs)
        result['max_dd_ddd_day'] = max_dd_ddd_day
    return result
