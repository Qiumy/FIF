#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, abort, jsonify, current_app
from flask_login import login_user, logout_user, current_user, login_required
from flask_babel import gettext
from datetime import datetime
import os

from ..util.run_backtest import run_strategy
from ..util.text_process import python
from ..util.get_backtest_result import get_backtest_result
from . import algo
from ..models import Strategy
from .. import db


@algo.route('/')
@login_required
def index():
    strategy = current_user.strategy
    return render_template('algo/index.html',
                           title=gettext('Algorithm'),
                           strategy=strategy)


# 创建策略
@algo.route('/new/', methods=['POST', 'GET'])
@login_required
def strategy_new():
    if request.method == 'GET':
        return render_template('algo/edit.html',
                               title=gettext('Algorithm'))
    if request.method == 'POST':
        name = request.form['name']
        # code = request.form['content']
        codePath = os.path.join(current_app.config['UPLOAD_FOLDER'], 'code', 'stTemplate.py')
        code = open(codePath, 'rb').read()
        new_strategy = Strategy(name=name, code=code, user_id=current_user.id)
        db.session.commit()

        # 更新用户对应的策略
        current_user.strategy.append(new_strategy)
        current_user.strategy_num += 1
        db.session.commit()
        return redirect(url_for('algo.strategy_edit',
                                sid=new_strategy.id,
                                strategy=new_strategy))


# 策略编辑
@algo.route('/edit/<int:sid>/')
@login_required
def strategy_edit(sid):
    cur_strategy = Strategy.query.filter_by(id=sid).first_or_404()
    if current_user.id != cur_strategy.user_id:
        abort(403)
    else:
        return render_template('algo/edit.html',
                               title=cur_strategy.name,
                               strategy=cur_strategy)


# 策略更新
@algo.route('/update/<int:sid>', methods=['POST', 'GET'])
@login_required
def strategy_update(sid):
    cur_strategy = Strategy.query.filter_by(id=sid).first_or_404()
    if current_user.id != cur_strategy.user_id:
        abort(403)
    else:
        name = request.form["name"]
        code = request.form['code']
        cur_strategy.name = name
        cur_strategy.code = code

        cur_strategy.modified_time = datetime.now()
        db.session.commit()

        return jsonify(name=name, code=code)


# 策略删除
@algo.route('/del/', methods=['POST', 'GET'])
@login_required
def strategy_delete():
    cur_strategy = Strategy.query.filter_by(id=request.form['id']).first_or_404()
    db.session.delete(cur_strategy)
    db.session.commit()
    return jsonify(status="success", del_strategy_id=cur_strategy.id)


# 策略批量删除
@algo.route('/batchDel/', methods=['POST', 'GET'])
@login_required
def strategy_batch_delete():
    idx = request.form.getlist('id[]')
    for x in idx:
        curr_strategy = Strategy.query.filter_by(id=x).first_or_404()
        db.session.delete(curr_strategy)
    db.session.commit()
    return jsonify(status='success')


# 策略运行
@algo.route('/run/<int:sid>/', methods=['POST', 'GET'])
@login_required
def strategy_run(sid):
    start_date = request.form['start-date']
    end_date = request.form['end-date']
    print("&&&&&&&:", start_date, "::", end_date)
    cur_strategy = Strategy.query.filter_by(id=sid).first_or_404()
    ## save as tmp .py file
    code_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], 'code')
    code_path = os.path.join(code_dir, "%d.py" % cur_strategy.id)
    print(code_path)

    with open(code_path, "w") as f:
        f.write(cur_strategy.code)

    result = run_strategy(start_date, end_date)

    print(result, "DONE!")

    picklePath = os.path.join(current_app.config['UPLOAD_FOLDER'], 'pickle')
    data_result = get_backtest_result(picklePath)

    senddata = {"data_result": data_result}
    return jsonify(senddata)

