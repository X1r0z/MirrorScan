# -*- coding:utf-8 -*-

from lib.utils import *

import leancloud
import wsgi
import os

PLUGIN_DIR = 'plugins'

AUTHOR = 'X1r0z'

USERNAME = 'exp10it'

UHASH = '8d4feddaa3c2466449d7570898a8d7619bbfae9e'

PRIVATE = False

COUNT = 0

for rt, dirs, files in os.walk(PLUGIN_DIR):
    for f in files:
        name = f.split('.')[0]
        service = os.path.basename(rt)
        body = open(os.path.join(rt,f),'r').read()
        query = leancloud.Query('mPlugin')
        query.equal_to('name', name)
        if query.find():
            info = query.first()
            if info.get('service') != service or info.get('body') != body:
                info.set('service', service)
                info.set('body', body)
                info.save()
                print 'Update Plugin', name, 'successfully'
        else:
            Plugin = leancloud.Object.extend('mPlugin')
            info = Plugin()
            info.set('name', name)
            info.set('info', info)
            info.set('body', body)
            info.set('author', AUTHOR)
            info.set('service', service)
            info.set('uhash', UHASH)
            info.set('phash', gethash())
            info.set('private', PRIVATE)
            info.set('count', COUNT)
            info.save()
            print 'Load Plugin', name, 'successfully'