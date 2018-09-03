# -*- coding:utf-8 -*-

from lib.warpper import *

import tornado.web

class LogoutHandler(tornado.web.RequestHandler):
    @authentication
    def get(self):
        self.clear_cookie('user')
        self.clear_cookie('hash')
        self.redirect('/login')