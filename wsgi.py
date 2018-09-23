# -*- coding:utf-8 -*-

import leancloud

from config import settings

import tornado.wsgi

app = tornado.wsgi.WSGIApplication(
    **settings
)

application = leancloud.Engine(app)