# -*- coding:utf-8 -*-

from config import settings
import wsgi

import tornado.web
import tornado.wsgi
import tornado.ioloop

app = tornado.web.Application(
    **settings
)

if __name__ == '__main__':
     app.listen(8000)
     tornado.ioloop.IOLoop.instance().start()