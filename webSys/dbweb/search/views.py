#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, current_app
from . import search
from flask_babel import gettext
import tushare as ts, json
import datetime

@search.route('/')
def index():
    stockcode = request.args.get('q')
    with current_app.open_resource('stock.json') as f:
        stock_dic = json.loads(f.read())

    if stockcode in stock_dic:
        return redirect(url_for('stock.stock_view', code=stockcode))
    else:
        return render_template('404.html', title='404'), 404

@search.app_errorhandler(404)
def page_404(err):
    return render_template('404.html', title='404'), 404


@search.app_errorhandler(403)
def page_403(err):
    return render_template('403.html', title='403'), 403


@search.app_errorhandler(500)
def page_500(err):
    return render_template('500.html', title='500'), 500
