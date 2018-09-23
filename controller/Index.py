# -*- coding:utf-8 -*-

from lib.core import *

import tornado.web

import leancloud

class IndexHandler(tornado.web.RequestHandler):
    @authentication
    def get(self):
        user = self.get_secure_cookie('user')
        uhash = self.get_secure_cookie('hash')
        top = leancloud.Query('mPlugin').equal_to('private', False).add_descending('count').limit(5).find()
        hole = leancloud.Query('mReport').equal_to('uhash', uhash).equal_to('level', 'hole').count()
        warn = leancloud.Query('mReport').equal_to('uhash', uhash).equal_to('level', 'warn').count()
        info = leancloud.Query('mReport').equal_to('uhash', uhash).equal_to('level', 'info').count()
        note = leancloud.Query('mReport').equal_to('uhash', uhash).equal_to('level', 'note').count()
        wait = leancloud.Query('mTask').equal_to('uhash', uhash).equal_to('status', 'wait').count()
        running = leancloud.Query('mTask').equal_to('uhash', uhash).equal_to('status', 'running').count()
        completed = leancloud.Query('mTask').equal_to('uhash', uhash).equal_to('status', 'completed').count()
        + leancloud.Query('mTask').equal_to('uhash', uhash).equal_to('status', 'stop').count()
        self.render('index.tpl',
            user=user,
            running=running,
            wait=wait,
            completed=completed,
            hole=hole,
            warn=warn,
            info=info,
            note=note,
            top=top)
