# -*- coding:utf-8 -*-

import leancloud
import os

APP_ID = '9RLabat5zEzNkYtwQW1Rn5sK-gzGzoHsz'
APP_KEY = 'M38DE3wMfrPA4HHeRaUkyoIR'
MASTER_KEY = 'EFNMBnGv5KazPMgzTNokpj6e'

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(False)

from config import settings

import tornado.wsgi

app = tornado.wsgi.WSGIApplication(
    **settings
)

application = leancloud.Engine(app)
