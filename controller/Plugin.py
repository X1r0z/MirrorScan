# -*- coding:utf-8 -*-

from lib.utils import *
from lib.warpper import *

import tornado.web
import leancloud

class PluginHandler(tornado.web.RequestHandler):
    @authentication
    def get(self, act, phash):
        user = self.get_secure_cookie('user')
        uhash = self.get_secure_cookie('hash')
        if act == 'Edit':
            myPluginQuery = leancloud.Query('mPlugin')
            myPluginQuery.equal_to('uhash', uhash)
            myPluginQuery.equal_to('phash', phash)
            if myPluginQuery.find():
                pluginInfo = myPluginQuery.first()
                self.render('pluginedit.tpl', user=user, info=pluginInfo)
            else:
                self.render('pluginedit.tpl', user=user)
        elif act == 'Del':
            myPluginQuery = leancloud.Query('mPlugin')
            myPluginQuery.equal_to('uhash', uhash)
            myPluginQuery.equal_to('phash', phash)
            if myPluginQuery.find():
                leancloud.Object.destroy_all(myPluginQuery.find())
                myPluginQuery = leancloud.Query('mPlugin')
                myPluginQuery.equal_to('uhash', uhash)
                myPluginList = myPluginQuery.find()
                self.render('plugin.tpl', user=user, myplugins=myPluginList, suc='成功删除插件')
            else:
                myPluginQuery = leancloud.Query('mPlugin')
                myPluginQuery.equal_to('uhash', uhash)
                myPluginList = myPluginQuery.find()
                self.render('plugin.tpl', user=user, myplugins=myPluginList, err='错误的插件哈希')
        else:
            myPluginQuery = leancloud.Query('mPlugin')
            myPluginQuery.equal_to('uhash', uhash)
            myPluginList = myPluginQuery.find()
            self.render('plugin.tpl', user=user, myplugins=myPluginList)

    @authentication
    def post(self, act, phash):
        user = self.get_secure_cookie('user')
        uhash = self.get_secure_cookie('hash')
        if act == 'Edit':
            name = self.get_argument('name')
            info = self.get_argument('info')
            body = self.get_argument('body')
            author = self.get_argument('author')
            service = self.get_argument('service')
            if name and info and body and author and service:
                if phash:
                    myPluginQuery = leancloud.Query('mPlugin')
                    myPluginQuery.equal_to('uhash', uhash)
                    myPluginQuery.equal_to('phash', phash)
                    pluginInfo =  myPluginQuery.find()
                    if pluginInfo:
                        pluginInfo.set('name', name)
                        pluginInfo.set('info', info)
                        pluginInfo.set('body', body)
                        pluginInfo.set('author', author)
                        pluginInfo.set('service', service)
                        pluginInfo.save()
                        myPluginQuery = leancloud.Query('mPlugin')
                        myPluginQuery.equal_to('uhash', uhash)
                        myPluginList = myPluginQuery.find()
                        self.render('plugin.tpl', user=user, myplugins=myPluginList, suc='成功编辑插件')
                    else:
                        self.render('plugin.tpl', user=user, myplugins=myPluginList, err='错误的插件哈希')
                else:
                    Plugin = leancloud.Object.extend('mPlugin')
                    pluginInfo = Plugin()
                    pluginInfo.set('name', name)
                    pluginInfo.set('info', info)
                    pluginInfo.set('body', body)
                    pluginInfo.set('author', author)
                    pluginInfo.set('service', service)
                    pluginInfo.set('uhash', uhash)
                    pluginInfo.set('phash', gethash())
                    pluginInfo.set('private', True)
                    pluginInfo.save()
                    myPluginQuery = leancloud.Query('mPlugin')
                    myPluginQuery.equal_to('uhash', uhash)
                    myPluginList = myPluginQuery.find()
                    self.render('plugin.tpl', user=user, myplugins=myPluginList, suc='成功添加插件')