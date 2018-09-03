# -*- coding:utf-8 -*-

import leancloud

def authentication(controller):
    def warpper(self, *args, **kwargs):
        user = self.get_secure_cookie('user')
        uhash = self.get_secure_cookie('hash')
        if user and uhash:
            return controller(self, *args, **kwargs)
        else:
            self.redirect('/login')
    return warpper

def protect(controller):
    def warpper(self, *args, **kwargs):
        if self.request.headers.get('User-Agent') == 'Python-urllib/2.7':
            return controller(self, *args, **kwargs)
        else:
            userQuery = leancloud.Query('mUser')
            userQuery.equal_to('uhash', args[0])
            if userQuery.find():
                userInfo = userQuery.first()
                userInfo.set('block', True)
                userInfo.set('group', '黑名单用户')
                userInfo.save()
                self.write('您已经被封禁')
            else:
                self.write('拒绝访问')
    return warpper