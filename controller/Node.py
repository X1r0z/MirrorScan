# -*- coding:utf-8 -*-

from lib.core import *

import tornado.web

import leancloud
import config

class NodeHandler(tornado.web.RequestHandler):
    @authentication
    def get(self, act, nodeID):
        user = self.get_secure_cookie('user')
        uhash = self.get_secure_cookie('hash')
        if act == 'Exit':
            nodeQuery = leancloud.Query('mNode')
            nodeQuery.equal_to('uhash', uhash)
            nodeQuery.equal_to('nodeid', int(nodeID))
            if nodeQuery.find():
                leancloud.Object.destroy_all(nodeQuery.find())
                nodeQuery = leancloud.Query('mNode')
                nodeQuery.equal_to('uhash', uhash)
                nodeList = nodeQuery.find()
                self.render('node.tpl',
                    scheme=config.SCHEME,
                    host=config.HOST,
                    uhash=uhash,
                    user=user,
                    nodelist=nodeList,
                    suc='成功退出节点'
                    )
            else:
                nodeQuery = leancloud.Query('mNode')
                nodeQuery.equal_to('uhash', uhash)
                nodeList = nodeQuery.find()
                self.render('node.tpl',
                    scheme=config.SCHEME,
                    host=config.HOST,
                    uhash=uhash,
                    user=user,
                    nodelist=nodeList,
                    err='错误的节点标识'
                    )
        else:
            nodeQuery = leancloud.Query('mNode')
            nodeQuery.equal_to('uhash', uhash)
            nodeList = nodeQuery.find()
            self.render('node.tpl',
                scheme=config.SCHEME,
                host=config.HOST,
                uhash=uhash,
                user=user,
                nodelist=nodeList)