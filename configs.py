#!/usr/bin/python
#coding:utf-8


import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/win/chromedriver.exe")

# 浏览器路径
CHROME_DRIVER_PATH = DRIVER_BIN  # 可以指定绝对路径，如果不指定的话会在$PATH里面查找
# 数据库连接信息
DATABASES = {
    'DRIVER': 'mysql+pymysql',
    'HOST': '127.0.0.1',
    'PORT': 3306,
    'NAME': 'gp',
    'USER': 'root',
    'PASSWORD': 'root',
}
