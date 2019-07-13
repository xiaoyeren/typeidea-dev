#!/usr/bin/env python
# -* coding:utf-8 -*-


__author__ = 'xiaoshuting'
from .base import * # NOQA
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}