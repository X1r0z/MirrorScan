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

    HOST = 'mirrorscan.leanapp.cn'

    DEBUG = False
else:

    HOST = 'mirrorscan:8000'

    DEBUG = True

INIT_FILE = 'init.pyc'

NODE_FILE = 'node.pyc'

APP_ID = '9RLabat5zEzNkYtwQW1Rn5sK-gzGzoHsz'

APP_KEY = 'M38DE3wMfrPA4HHeRaUkyoIR'

MASTER_KEY = 'EFNMBnGv5KazPMgzTNokpj6e'

REDIS_HOST = 'redis-13572.c1.asia-northeast1-1.gce.cloud.redislabs.com'

REDIS_PORT = 13572

REDIS_PASS = 'mmqrfPVXIYYmhB7rlykmA6wHV09p54xY'

REDIS_EXPIRE = 300

SECRET = '5_pdecg&#s1g=ka_rrohm)v1-zyecoqxzmga9%abm7quvs6y^5'

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