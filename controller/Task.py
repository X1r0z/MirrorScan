# -*- coding:utf-8 -*-

from lib.utils import *
from lib.warpper import *

import tornado.web
import leancloud

class TaskHandler(tornado.web.RequestHandler):
    @authentication
    def get(self, act, tid):
        user = self.get_secure_cookie('user')
        uhash = self.get_secure_cookie('hash')
        if act == 'Info':
            taskQuery = leancloud.Query('mTask')
            taskQuery.equal_to('uhash', uhash)
            taskQuery.equal_to('tid', tid)
            taskInfo = taskQuery.find()
            if taskInfo:
                target = taskQuery.first().get('target')
                reportQuery = leancloud.Query('mReport')
                reportQuery.equal_to('uhash', uhash)
                reportQuery.equal_to('tid', tid)
                reportQuery.limit(1000)
                reportInfo = reportQuery.find()
                if reportInfo:
                    report = reportformat(reportInfo)
                    self.render('taskinfo.tpl', user=user, target=target, report=report)
                else:
                    taskQuery = leancloud.Query('mTask')
                    taskQuery.equal_to('uhash', uhash)
                    taskInfo = taskQuery.find()
                    self.render('task.tpl', user=user, info=taskInfo, err='该扫描节点还没有发送报告')
            else:
                taskQuery = leancloud.Query('mTask')
                taskQuery.equal_to('uhash', uhash)
                taskInfo = taskQuery.find()
                self.render('task.tpl', user=user, info=taskInfo, err='错误的任务哈希')
        elif act == 'Add':
            publicPluginQuery = leancloud.Query('mPlugin')
            publicPluginQuery.equal_to('private', False)
            myPluginQuery = leancloud.Query('mPlugin')
            myPluginQuery.equal_to('uhash', uhash)
            publicPluginList = publicPluginQuery.find()
            serviceList = set()
            for item in publicPluginList:
                serviceList.add(item.get('service'))
            serviceList.add('my plugins')
            self.render('taskadd.tpl', user=user, service=serviceList)
        elif act == 'Del':
            taskQuery = leancloud.Query('mTask')
            taskQuery.equal_to('uhash', uhash)
            taskQuery.equal_to('tid', tid)
            if taskQuery.find():
                reportQuery = leancloud.Query('mReport')
                reportQuery.equal_to('uhash', uhash)
                reportQuery.equal_to('tid', tid)
                reportQuery.limit(1000)
                leancloud.Object.destroy_all(taskQuery.find())
                leancloud.Object.destroy_all(reportQuery.find())
                taskQuery = leancloud.Query('mTask')
                taskQuery.equal_to('uhash', uhash)
                taskInfo = taskQuery.find()
                self.render('task.tpl', user=user, info=taskInfo, suc='成功删除任务')
            else:
                taskQuery = leancloud.Query('mTask')
                taskQuery.equal_to('uhash', uhash)
                taskInfo = taskQuery.find()
                self.render('task.tpl', user=user, info=taskInfo, err='错误的任务哈希')
        else:
            taskQuery = leancloud.Query('mTask')
            taskQuery.equal_to('uhash', uhash)
            taskInfo = taskQuery.find()
            self.render('task.tpl', user=user, info=taskInfo)

    @authentication
    def post(self, act, tid):
        user = self.get_secure_cookie('user')
        uhash = self.get_secure_cookie('hash')
        if act == 'Add':
            speed = self.get_argument('speed', '')
            target = self.get_argument('target', '')
            cookie = self.get_argument('cookie', '')
            method = self.get_arguments('method')
            plugins = self.get_arguments('plugins')
            timeout = self.get_argument('timeout', '')
            maxpage = self.get_argument('maxpage', '')
            exclude = self.get_argument('exclude', '')
            comments = self.get_argument('comments', '')
            useragent = self.get_argument('useragent', '')
            subdomain = True if 'subdomain' in method else False
            scanport = True if 'scanport' in method else False
            if speed and target and timeout and maxpage and plugins:
                publicPluginQuery = leancloud.Query('mPlugin')
                publicPluginQuery.equal_to('private', False)
                myPluginQuery = leancloud.Query('mPlugin')
                myPluginQuery.equal_to('uhash', uhash)
                myPluginList = myPluginQuery.find()
                hashList = set()
                if 'my plugins' in plugins:
                    plugins.remove('my plugins')
                    for item in myPluginList:
                        hashList.add(item.get('phash'))
                publicPluginQuery.contained_in('service', plugins)
                pluginList = publicPluginQuery.find()
                for item in pluginList:
                    hashList.add(item.get('phash'))
                Task = leancloud.Object.extend('mTask')
                taskInfo = Task()
                taskInfo.set('tid', gethash())
                taskInfo.set('uhash', uhash)
                taskInfo.set('target', target)
                taskInfo.set('stime', gettime())
                taskInfo.set('plugins', list(hashList))
                taskInfo.set('status', 'wait')
                taskInfo.set('speed', int(speed))
                taskInfo.set('timeout', int(timeout))
                taskInfo.set('maxpage', int(maxpage))
                taskInfo.set('exclude', exclude)
                taskInfo.set('cookie', cookie)
                taskInfo.set('useragent', useragent)
                taskInfo.set('subdomain', subdomain)
                taskInfo.set('scanport', scanport)
                taskInfo.set('comments', comments)
                taskInfo.save()
                taskQuery = leancloud.Query('mTask')
                taskQuery.equal_to('uhash', uhash)
                taskInfo = taskQuery.find()
                self.render('task.tpl', user=user, info=taskInfo, suc='成功添加任务')