#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, abort, request, redirect, url_for
from . import article
from ..models import Article
from flask_babel import gettext
from .. import db


@article.route('/')
def index():
    article_list = Article.query.all()
    return render_template('article/index.html', title="Notices", article_list=article_list)


@article.route('/<int:article_id>')
def detail(article_id):
    detail_article = Article.query.filter_by(id=article_id).first()
    detail_article.visit_num += 1
    db.session.commit()
    return render_template('article/detail.html',
                           title=detail_article.title[:10],
                           article=detail_article)
