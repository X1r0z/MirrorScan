# -*- coding:utf-8 -*-

from lib.utils import *
from lib.common import *
from lib.warpper import *

import tornado.web
import leancloud

class TaskHandler(tornado.web.RequestHandler):
    @authentication
    def get(self, act, arg):
        user = self.get_secure_cookie('user')
        uhash = self.get_secure_cookie('hash')
        if act == 'Info':
            taskQuery = leancloud.Query('mTask')
            taskQuery.equal_to('uhash', uhash)
            taskQuery.equal_to('tid', arg)
            taskInfo = taskQuery.find()
            if taskInfo:
                target = taskQuery.first().get('target')
                perPage, _ = getpage(leancloud.Query('mReport').equal_to('uhash', uhash).equal_to('tid', arg))
                reportInfo = getdata('mReport', perPage, uhash=uhash, tid=arg)
                if reportInfo:
                    report = reportformat(reportInfo)
                    self.render('taskinfo.tpl', user=user, target=target, report=report)
                else:
                    perPage, skipPage = getpage(leancloud.Query('mTask').equal_to('uhash', uhash))
                    taskQuery = leancloud.Query('mTask')
                    taskQuery.equal_to('uhash', uhash)
                    taskQuery.limit(skipPage)
                    taskInfo = taskQuery.find()
                    self.render('task.tpl', user=user, info=taskInfo, per=perPage, cur=1, err='该扫描节点还没有发送报告')
            else:
                perPage, skipPage = getpage(leancloud.Query('mTask').equal_to('uhash', uhash))
                taskQuery = leancloud.Query('mTask')
                taskQuery.equal_to('uhash', uhash)
                taskQuery.limit(skipPage)
                taskInfo = taskQuery.find()
                self.render('task.tpl', user=user, info=taskInfo, per=perPage, cur=1, err='错误的任务哈希')
        elif act == 'Add':
            perPage, _ = getpage(leancloud.Query('mPlugin').equal_to('private', False))
            publicPluginList = getdata('mPlugin', perPage, private=False)
            serviceList = set()
            for item in publicPluginList:
                serviceList.add(item.get('service'))
            serviceList.add('my plugins')
            self.render('taskadd.tpl', user=user, service=serviceList)
        elif act == 'Del':
            taskQuery = leancloud.Query('mTask')
            taskQuery.equal_to('uhash', uhash)
            taskQuery.equal_to('tid', arg)
            if taskQuery.find():
                perPage, _ = getpage(leancloud.Query('mReport').equal_to('uhash', uhash).equal_to('tid', arg))
                reportInfo = getdata('mReport', perPage, uhash=uhash, tid=arg)
                leancloud.Object.destroy_all(taskQuery.find())
                leancloud.Object.destroy_all(reportInfo)
                perPage, skipPage = getpage(leancloud.Query('mTask').equal_to('uhash', uhash))
                taskQuery = leancloud.Query('mTask')
                taskQuery.equal_to('uhash', uhash)
                taskQuery.limit(skipPage)
                taskInfo = taskQuery.find()
                self.render('task.tpl', user=user, info=taskInfo, per=perPage, cur=1, suc='成功删除任务')
            else:
                perPage, skipPage = getpage(leancloud.Query('mTask').equal_to('uhash', uhash))
                taskQuery = leancloud.Query('mTask')
                taskQuery.equal_to('uhash', uhash)
                taskQuery.limit(skipPage)
                taskInfo = taskQuery.find()
                self.render('task.tpl', user=user, info=taskInfo, per=perPage, cur=1, err='错误的任务哈希')
        elif act == 'Page':
            if arg:
                num = int(arg)
                if num == 1:
                    perPage, skipPage = getpage(leancloud.Query('mTask').equal_to('uhash', uhash))
                    taskQuery = leancloud.Query('mTask')
                    taskQuery.equal_to('uhash', uhash)
                    taskQuery.limit(skipPage)
                    taskInfo = taskQuery.find()
                    self.render('task.tpl', user=user, info=taskInfo, per=perPage, cur=1)
                else:
                    perPage, skipPage = getpage(leancloud.Query('mTask').equal_to('uhash', uhash))
                    skip = (num - 1) * skipPage
                    taskQuery = leancloud.Query('mTask')
                    taskQuery.equal_to('uhash', uhash)
                    taskQuery.skip(skip)
                    taskQuery.limit(skipPage)
                    taskInfo = taskQuery.find()
                    self.render('task.tpl', user=user, info=taskInfo, per=perPage, cur=num)
            else:
                perPage, skipPage = getpage(leancloud.Query('mTask').equal_to('uhash', uhash))
                taskQuery = leancloud.Query('mTask')
                taskQuery.equal_to('uhash', uhash)
                taskQuery.limit(skipPage)
                taskInfo = taskQuery.find()
                self.render('task.tpl', user=user, info=taskInfo, per=perPage, cur=1)
        else:
            perPage, skipPage = getpage(leancloud.Query('mTask').equal_to('uhash', uhash))
            taskQuery = leancloud.Query('mTask')
            taskQuery.equal_to('uhash', uhash)
            taskQuery.limit(skipPage)
            taskInfo = taskQuery.find()
            self.render('task.tpl', user=user, per=perPage, cur=1, info=taskInfo)

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
                perPage, _ = getpage(leancloud.Query('mPlugin').equal_to('uhash', uhash))
                myPluginList = getdata('mPlugin', perPage, uhash=uhash)
                perPage, _ = getpage(leancloud.Query('mPlugin').equal_to('private', False))
                pluginList = getdata('mPlugin', perPage, private=False)
                hashList = set()
                if 'my plugins' in plugins:
                    plugins.remove('my plugins')
                    for item in myPluginList:
                        hashList.add(item.get('phash'))
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
                perPage, skipPage = getpage(leancloud.Query('mTask').equal_to('uhash', uhash))
                taskQuery = leancloud.Query('mTask')
                taskQuery.equal_to('uhash', uhash)
                taskQuery.limit(skipPage)
                taskInfo = taskQuery.find()
                self.render('task.tpl', user=user, info=taskInfo, per=perPage, cur=1, suc='成功添加任务')