# -*- coding:utf-8 -*-

from lib.utils import *

import tornado.web
import leancloud

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        email = self.get_argument('email', '')
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        code = self.get_argument('code', '')
        if email and username and password and code:
            userQuery = leancloud.Query('mUser')
            userQuery.equal_to('username',username)
            if userQuery.find():
                self.render('login.tpl', err='该用户名已经被注册')
            else:
                codeQuery = leancloud.Query('mInvite')
                codeQuery.equal_to('code', code)
                if codeQuery.find():
                    codeQuery.destroy()
                    User = leancloud.Object.extend('mUser')
                    userInfo = User()
                    userInfo.set('email', email)
                    userInfo.set('username', username)
                    userInfo.set('password', encodepass(password))
                    userInfo.set('uhash', gethash())
                    userInfo.set('group', '注册用户')
                    userInfo.set('block', False)
                    userInfo.save()
                    self.render('login.tpl', suc='注册成功')
                else:
                    self.render('login.tpl', err='错误的邀请码')