# -*- coding:utf-8 -*-

from urls import urls

import tornado.log

import leancloud
import logging
import marshal
import time
import os

SCHEME = 'http'

if os.environ.get('LEANCLOUD_APP_ID'):

    HOST = 'HOST'

    DEBUG = False
else:

    HOST = 'mirrorscan:8000'

    DEBUG = True

INIT_FILE = 'init.pyc'

NODE_FILE = 'node.pyc'

APP_ID = 'APP_ID'

APP_KEY = 'APP_KEY'

MASTER_KEY = 'MASTER_KEY'

REDIS_HOST = 'REDIS_HOST'

REDIS_PORT = 6379

REDIS_PASS = 'REDIS_PASS'

REDIS_EXPIRE = 300

SECRET = 'SECRET'

BASE_DIR = os.path.dirname(__file__)

TEMPLATE_PATH = 'templates'

STATIC_PATH = 'static'

logging.getLogger().setLevel(logging.INFO)

def logger(handler):
    if handler.get_status() < 400:
        func = tornado.log.access_log.info
    elif handler.get_status() < 500:
        func = tornado.log.access_log.warning
    else:
        func = tornado.log.access_log.error
    func("%d %s %s (%s) %.2fms",
            handler.get_status(), handler.request.method,
            handler.request.uri, handler.request.remote_ip,
            1000.0 * handler.request.request_time())

settings = {
    'handlers': urls,
    'cookie_secret': SECRET,
    'template_path': os.path.join(BASE_DIR,TEMPLATE_PATH),
    'static_path': os.path.join(BASE_DIR,STATIC_PATH),
    'log_function': logger,
    'debug': DEBUG,
}

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(False)

marshal.dump(compile(open('templates/bin/init.py', 'r').read().replace('HOST', HOST).replace('SCHEME', SCHEME), 'templates/bin/init.pyc', 'exec'), open('templates/bin/init.pyc', 'w+b'))
marshal.dump(compile(open('templates/bin/node.py', 'r').read(), 'templates/bin/init.pyc', 'exec'), open('templates/bin/node.pyc', 'w+b'))
