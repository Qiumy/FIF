#! /usr/bin/env python
# -*- coding: utf-8 -*-

from . import filter_blueprint
import misaka as m
import re
from ..models import User
from flask import url_for


@filter_blueprint.app_template_filter('markdown')
def markdown(strs):
    """ Render the string into html style.
    """
    return m.html(strs)


@filter_blueprint.app_template_filter('split')
def split(string, c, n):
    return string.split(c)[n]


@filter_blueprint.app_template_filter("python")
def python(strs):
    keys = ['\'', '\"', '\n']
    for key in keys:
        strs = re.sub(key, "\\" + key, strs)
    return strs


def add_user_links_in_content(content):
    """ Replace the @user with the link of the user.
    """
    for at_name in re.findall(r'@(.*?)(?:\s|</\w+>)', content):
        at_u = User.query.filter_by(username=at_name).first()
        # There is no such a uer.
        if not at_u:
            continue

        # Add links to the @user field.
        content = re.sub(
            '@%s' % at_name,
            '@<a href="%s" class="mention">%s</a>' % (url_for('user.view', uid=at_u.id), at_name),
            content)

    return content
