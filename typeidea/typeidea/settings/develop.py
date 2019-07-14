#!/usr/bin/env python
# -* coding:utf-8 -*-


__author__ = 'xiaoshuting'
from .base import * # NOQA
DEBUG = True

import pymysql         # 一定要添加这两行！
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'blog',  # 数据库名，先前创建的
        'USER': 'root',     # 用户名，可以自己创建用户
        'PASSWORD': '123456',  # 密码
        'HOST': '127.0.0.1',  # mysql服务所在的主机ip
        'PORT': '3306',         # mysql服务端口
    }
}