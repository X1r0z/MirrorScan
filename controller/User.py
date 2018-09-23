# -*- coding:utf-8 -*-

from lib.core import *

import tornado.web

import leancloud

class UserHandler(tornado.web.RequestHandler):
    @authentication
    def get(self):
        user = self.get_secure_cookie('user')
        uhash = self.get_secure_cookie('hash')
        userQuery = leancloud.Query('mUser')
        userQuery.equal_to('uhash', uhash)
        userInfo = userQuery.first()
        self.render('user.tpl', user=user, info=userInfo)

    @authentication
    def post(self):
        user = self.get_secure_cookie('user')
        uhash = self.get_secure_cookie('hash')
        email = self.get_argument('email', '')
        website = self.get_argument('website', '')
        info = self.get_argument('info', '')
        qq = self.get_argument('qq', '')
        password = self.get_argument('password', '')
        userQuery = leancloud.Query('mUser')
        userQuery.equal_to('uhash', uhash)
        userInfo = userQuery.first()
        if password:
            if userInfo.get('password') == password:
                userInfo.set('email', email)
                userInfo.set('website', website)
                userInfo.set('info', info)
                userInfo.set('qq', qq)
                userInfo.save()
                self.render('user.tpl', user=user, info=userInfo, suc='成功更新个人信息')
            else:
                self.render('user.tpl', user=user, info=userInfo, err='错误的密码')