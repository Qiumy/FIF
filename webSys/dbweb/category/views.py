#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, abort, request, redirect, url_for, jsonify
from flask_login import current_user, login_required
from flask_babel import gettext
from datetime import datetime
from . import category
from ..models import Topic, Post
from ..util.text_process import add_user_links_in_content
from .. import db

# 社区首页
@category.route('/all/')
def all():
    all_topic = Topic.query.all()
    return render_template('category/all.html',
                           title=gettext('All'),
                           all_topic=all_topic,
                           cate='all')

@category.route('/research/')
def research():
    all_topic = Topic.query.filter_by(cat_type=1).all()
    return render_template('category/research.html',
                           title=gettext('Research'),
                           all_topic=all_topic)

@category.route('/study/')
def study():
    all_topic = Topic.query.filter_by(cat_type=2).all()
    return render_template('category/study.html',
                           title=gettext('Study'),
                           all_topic=all_topic)

@category.route('/question/')
def question():
    all_topic = Topic.query.filter_by(cat_type=3).all()
    return render_template('category/question.html',
                           title=gettext('Question'),
                           all_topic=all_topic)

# 话题的详细页面
@category.route('/topic/<int:tid>/')
def topic_view(tid):
    cur_topic = Topic.query.filter_by(id=tid).first_or_404()
    cur_topic.visit_num += 1
    db.session.commit()
    return render_template('category/topic_detail.html',
                           title=cur_topic.title,
                           topic=cur_topic)

@category.route('/topic/new/', methods=['GET', 'POST'])
@login_required
def topic_new():
    if request.method == 'GET':
        print("GET+++++++++++++++++++++")
        return render_template('category/topic_new.html',
                               title='New Topic')
    elif request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cate_type = request.form['cate-type']
        new_topic = Topic(current_user.id, title, content, cate_type)
        db.session.commit()

        # 更新用户和专栏对应的话题
        current_user.topics.append(new_topic)
        current_user.topic_num += 1
        db.session.commit()
        return redirect(url_for('category.topic_view', tid=new_topic.id))

# 话题编辑页面
@category.route('/topic/edit/<int:tid>')
@login_required
def topic_edit(tid):
    cur_topic = Topic.query.filter_by(id=tid).first_or_404()
    if current_user.id != cur_topic.user_id:
        abort(403)
    else:
        return render_template('category/topic_edit.html',
                               title=cur_topic.title,
                               topic=cur_topic)

# 更新话题
@category.route('/topic/update/<int:tid>/', methods=['POST'])
@login_required
def topic_update(tid):
    cur_topic = Topic.query.filter_by(id=tid).first_or_404()
    if current_user.id != cur_topic.user_id:
        abort(403)
    else:
        content = request.form['content']
        title = request.form['title']
        cur_topic.title = title
        cur_topic.content = content
        cur_topic.updatedTime = datetime.now()
        db.session.commit()

        return redirect(url_for('category.topic_view', tid=cur_topic.id))

# 在话题下发表评论
@category.route('/topic/<int:tid>/comment/create/', methods=['POST'])
@login_required
def create_post(tid):
    cur_topic = Topic.query.filter_by(id=tid).first_or_404()
    post_content = request.form['content']
    post_content = add_user_links_in_content(post_content)

    new_post = Post(current_user.id, content=post_content)
    cur_topic.posts.append(new_post)
    cur_topic.post_num += 1

    current_user.post_num += 1
    db.session.add(new_post)
    db.session.commit()

    new_post_html = render_template('category/widget_post_detail.html',
                                    p=new_post,
                                    index=cur_topic.post_num)

    return jsonify(post_html=new_post_html,
                   post_cnt=cur_topic.post_num)