# -*- coding:utf-8 -*-

from lib.utils import *

import tornado.web

import leancloud

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.tpl')

    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        userQuery = leancloud.Query('mUser')
        userQuery.equal_to('username', username)
        userQuery.equal_to('password', encodepass(password))
        if userQuery.find():
            userInfo = userQuery.first()
            self.set_secure_cookie('user', userInfo.get('username'), expires_days=None, httponly=True)
            self.set_secure_cookie('hash', userInfo.get('uhash'), expires_days=None, httponly=True)
            self.redirect('/')
        else:
            self.render('login.tpl', err='登录失败')