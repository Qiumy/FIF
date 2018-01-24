#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
search = Blueprint('search', __name__)
from . import views

