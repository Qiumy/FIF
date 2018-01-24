#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
category = Blueprint('category', __name__)
from . import views
