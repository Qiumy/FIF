#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
group = Blueprint('group', __name__)
from . import views