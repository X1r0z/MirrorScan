# -*- coding:utf-8 -*-

from lib.warpper import *

import tornado.web
import leancloud
import config

class UHandler(tornado.web.RequestHandler):
    @protect
    def get(self, uhash, act):
        userQuery = leancloud.Query('mUser')
        userQuery.equal_to('uhash', uhash)
        userInfo = userQuery.find()
        if userInfo:
            if act == 'node':
                data = open(config.NODE_FILE, 'rb').read()
                self.set_header('Content-Type', 'application/octet-stream')
                self.set_header('Content-Disposition', 'attachment;filename=node.py')
                self.write(data)
            else:
                data = open(config.INIT_FILE, 'rb').read()
                self.set_header('Content-Type', 'application/octet-stream')
                self.set_header('Content-Disposition', 'attachment;filename=init.py')
                self.write(data)
        else:
            self.write('Access Denied')