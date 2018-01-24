#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
algo = Blueprint('algo', __name__)
from . import views
