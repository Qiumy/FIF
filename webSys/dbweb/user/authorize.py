#! /usr/bin/env python
# -*- coding: utf-8 -*-


from flask import redirect, request, url_for
from flask_login import current_user
from functools import wraps


def admin_login(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if current_user.is_authenticated and (current_user.permissions == 0):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.auth', next=request.url))
    return wrap

def system_login(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if current_user.is_authenticated and current_user.permissions == 0:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.auth', next=request.url))
    return wrap

