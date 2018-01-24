#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask_babel import gettext
from flask import current_app
from PIL import Image
import os


def upload_img(file_src, des_height, des_width, des_path):
    """ 保存 form 表单获取的上传图片到目标地址 des_path

    图片大小为 des_height * des_width,
    成功返回 True 和 图片携带的特征戳
    失败返回 False, 同时 message 里面携带失败信息.
    """
    if file_src.filename == '':
        message = gettext('No selected file')
        return False, message

    allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']
    file_appendix = file_src.filename.rsplit('.', 1)[1]

    if file_src and '.' in file_src.filename and file_appendix in allowed_extensions:
        im = Image.open(file_src)
        # im.thumbnail((des_height, des_width), Image.ANTIALIAS)
        im.resize((des_height, des_width))
        im.save(des_path, 'PNG')

        unique_uri = os.stat(des_path).st_mtime
        return True, unique_uri
    else:
        message = gettext("Invalid file")
        return False, message

