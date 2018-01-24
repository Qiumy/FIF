#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, url_for, current_app, abort, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from flask_babel import gettext
from flask_paginate import Pagination
from ..util.get_stock import get_profit_stock_list, get_user_profit, get_stock
import re, os
from PIL import Image
from datetime import datetime
from . import user
from ..models import User, Follow_Stock
from ..util.email_util import send_email
from .. import db

alphanumeric = re.compile(r'^[0-9a-zA-Z\_]*$')
email_address = re.compile(r'[a-zA-z0-9]+\@[a-zA-Z0-9]+\.+[a-zA-Z]')


@user.route('/signin/', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(request.args.get('next') or url_for("main.index"))
        return render_template('user/signin.html',
                               title=gettext('Sign in'),
                               form=None)
    elif request.method == 'POST':
        _form = request.form
        u = User.query.filter_by(email=_form['email']).first()
        if u and u.verify_password(_form['password']) and u.is_valid_registered:
            login_user(u)
            u.last_login = datetime.now()
            db.session.commit()
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            message = gettext('Invalid username or password.')
            return render_template('user/signin.html', title='Sign in',
                                   form=_form, message=message)


@user.route('/signout/')
@login_required
def signout():
    logout_user()
    return redirect(request.args.get('next') or request.referrer or url_for('main.index'))


@user.route('/register/', methods=['GET', 'POST'])
def reg():
    if request.method == 'GET':
        return render_template('user/reg.html',
                               title=gettext('Register Account'),
                               form=None)
    elif request.method == 'POST':
        _form = request.form
        username = _form['username']
        email = _form['email']
        password = _form['password']
        password2 = _form['password2']

        message_e, message_u, message_p = "", "", ""
        # Check username is valid or not.
        if not username:
            message_u = gettext('Username can not be empty.')
        elif not alphanumeric.match(username):
            message_u = gettext('Username can only contain letters digits and underscore.')
        elif User.query.filter_by(username=username).first():
            message_u = gettext('Username already exists.')

        # Check email is valid or not.
        if not email:
            message_e = gettext('Email address can not be empty.')
        elif not email_address.match(email):
            message_e = gettext('Email address is invalid.')
        elif User.query.filter_by(email=email).first():
            message_e = gettext('Email already exists.')

        # Check the password is valid or not.
        if password != password2:
            message_p = gettext("Passwords don't match.")
        elif password == "" or password2 == "":
            message_p = gettext("Passwords can not be empty.")

        if message_u or message_p or message_e:
            return render_template("user/reg.html", form=_form,
                                   title=gettext('Register Account'),
                                   message_u=message_u,
                                   message_p=message_p,
                                   message_e=message_e)

        #A valid register info, save the info into db, and wait for mail confirm.
        else:
            reg_user = User(username=username, email=email, password=password)
            db.session.add(reg_user)
            db.session.commit()
            token = reg_user.generate_reset_token()
            send_email(reg_user.email, 'Confirm Your Email',
                       'user/register_email',
                       user=reg_user, token=token)
            return render_template('user/register_sent.html')


@user.route('/register/<token>')
def reg_confirm(token):
    reg_user = User.verify_token(token)
    reg_user.is_valid_registered = True
    db.session.commit()
    login_user(reg_user)
    return redirect(request.args.get('next') or url_for('main.index'))


@user.route('/<int:uid>/')
@login_required
def view(uid):
    cur_user = User.query.filter_by(id=uid).first_or_404()
    profit_stock_list = get_profit_stock_list(cur_user.user_stock_list)
    user_profit = get_user_profit(profit_stock_list)
    codes = Follow_Stock.query.filter_by(user_id=current_user.id).all()
    follow_stock = [get_stock(code.stock_id) for code in codes]

    for i in range(len(follow_stock)):
        if Follow_Stock.query.filter_by(user_id=current_user.id,
                                        stock_id=follow_stock[i].code).first() is not None:
            follow_stock[i].flag = True
        else:
            follow_stock[i].flag = False
    return render_template('user/detail.html',
                           title='Personal Profile',
                           user=cur_user,
                           profit_stock_list=profit_stock_list,
                           user_profit=user_profit,
                           follow_stock=follow_stock)


@user.route('/password/reset/', methods=['GET', 'POST'])
def password_reset_request():
    if request.method == 'GET':
        return render_template('user/passwd_reset.html', form=None)
    elif request.method == 'POST':
        _form = request.form
        email_addr = _form["email"]
        u = User.query.filter_by(email=email_addr).first()
        message_email = ""
        if not email_addr:
            message_email = gettext("Email address can not be empty.")
        elif not email_address.match(email_addr):
            message_email = gettext('Email address is invalid.')
        elif not u:
            message_email = gettext("The email has not be registered")

        if message_email:
            return render_template('user/passwd_reset.html', message_email=message_email)
        else:
            token = u.generate_reset_token()
            # Clear the token status to "True".
            u.is_password_reset_link_valid = True
            db.session.commit()
            send_email(u.email, 'Reset Your Password',
                       'user/passwd_reset_email',
                       user=u, token=token)

            return render_template('user/passwd_reset_sent.html')


@user.route('/password/reset/<token>/', methods=['GET', 'POST'])
def password_reset(token):
    if request.method == "GET":
        u = User.verify_token(token)
        if u and u.is_password_reset_link_valid:
            return render_template('user/passwd_reset_confirm.html', form=None)
        else:
            return render_template('user/passwd_reset_done.html', message='Failed')
    elif request.method == 'POST':
        _form = request.form
        new_password = _form['password']
        new_password_2 = _form['password2']

        message_p = ""
        if new_password != new_password_2:
            message_p = gettext("Passwords don't match.")
        elif new_password_2 == "" or new_password == "":
            message_p = gettext("Passwords can not be empty.")

        if message_p:
            return render_template('user/passwd_reset_confirm.html', message_p=message_p)
        else:
            # Get the token without input the email address.
            u = User.verify_token(token)
            if u and u.is_password_reset_link_valid:
                u.password = new_password
                u.is_password_reset_link_valid = False
                db.session.commit()
                reset_result = "Successful"
            else:
                reset_result = "Failed"

            return render_template('user/passwd_reset_done.html', message=reset_result)



@user.route('/setting/')
@login_required
def setting():
    if request.method == 'GET':
        return render_template('user/setting.html',
                               title=u'Settings',
                               form=None)


@user.route('/setting/info', methods=['GET', 'POST'])
@login_required
def setting_info():
    if request.method == 'GET':
        return jsonify(content=render_template('user/ajax_setting_info.html', form=None))

    elif request.method == 'POST':
        _form = request.form
        email_addr = _form["email"]
        personal_profile = _form["website"]

        message_email = ""
        if not email_addr:
            message_email = gettext('Email address can not be empty.')
        elif not email_address.match(email_addr):
            message_email = gettext('Email address is invalid.')

        # TODO
        # Change the user's email need to verify the old_email addr's ownership
        if message_email:
            return jsonify(content=render_template("user/ajax_setting_info.html",
                                                   message_email=message_email))
        else:
            current_user.personal_profile = personal_profile
            current_user.email = email_addr
            db.session.commit()
            message_success = u'更改成功！'
            return jsonify(content=render_template('user/ajax_setting_info.html',
                                                   message_success=message_success))


@user.route("/setting/avatar/", methods=['GET', 'POST'])
@login_required
def setting_avatar():
    if request.method == 'GET':
        return jsonify(content=render_template('user/ajax_setting_avatar.html', form=None))

    elif request.method == 'POST':
        _file = request.files['file']
        # If user does not select file, browser also submit a empty part without filename
        if _file.filename == '':
            message_fail = gettext('No selected file')
            return jsonify(content=render_template('user/ajax_setting_avatar.html',
                                                   message_fail=message_fail))

        allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']
        # upload_folder = current_app.config['UPLOAD_FOLDER']
        upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], 'avatar')
        file_appendix = _file.filename.rsplit('.', 1)[1]
        if _file and '.' in _file.filename and file_appendix in allowed_extensions:
            im = Image.open(_file)
            im.thumbnail((128, 128), Image.ANTIALIAS)
            im.save("%s/%d.png" % (upload_folder, current_user.id), 'PNG')

            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], "%d.png" % current_user.id)
            unique_mark = os.stat(image_path).st_mtime
            current_user.avatar_url = url_for('static',
                                              filename='upload/avatar/%d.png' % current_user.id, t=unique_mark)
            db.session.commit()
            message_success = gettext('Update avatar done!')
            return jsonify(content=render_template('user/ajax_setting_avatar.html',
                                                   message_success=message_success))
        else:
            message_fail = gettext("Invalid file")
            return jsonify(content=render_template('user/ajax_setting_avatar.html',
                                                   message_fail=message_fail))


@user.route("/setting/password/", methods=['GET', 'POST'])
@login_required
def setting_password():
    if request.method == 'GET':
        return jsonify(content=render_template('user/ajax_setting_passwd.html', form=None))

    elif request.method == 'POST':
        _form = request.form
        cur_password = _form['old_password']
        new_password = _form['password']
        new_password_2 = _form['password2']

        message_cur, message_new = "", ""
        if not cur_password:
            message_cur = "The old password can not be empty."
        elif not current_user.verify_password(cur_password):
            message_cur = "The old password is not correct."

        if new_password != new_password_2:
            message_new = gettext("Passwords don't match.")
        elif new_password_2 == "" or new_password == "":
            message_new = gettext("Passwords can not be empty.")

        if message_cur or message_new:
            return jsonify(content=render_template('user/ajax_setting_passwd.html', form=_form,
                                                   message_cur=message_cur,
                                                   message_new=message_new
                                                   ))
        else:
            current_user.password = new_password
            db.session.commit()
            message_success = u'密码修改成功'
            return jsonify(content=render_template('user/ajax_setting_passwd.html',
                                                   message_success=message_success))
