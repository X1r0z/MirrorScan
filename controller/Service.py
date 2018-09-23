# -*- coding:utf-8 -*-

from lib.common import *
from lib.utils import *

import tornado.web
import tornado.gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

import leancloud
import config
import redis

nodeID = 0

class ServiceHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(10)
    
    @run_on_executor
    def deleteCache(self, handler, chash):
        handler.delete(chash)

    def get(self):
        self.write('Access Denied')
    
    @tornado.gen.coroutine
    def post(self):
        global nodeID
        redisCache = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PASS)
        if self.request.body:
            data = decodestr(self.request.body[33:])
            uuid = data['uuid']
            uhash = data['uhash']
            values = data['values']
            act = data['intention']
            userQuery = leancloud.Query('mUser')
            userQuery.equal_to('uhash', uhash)
            userQuery.equal_to('block', False)
            if userQuery.find():
                if act == 'login':
                    nodeID += 1
                    platform, version = values
                    Node = leancloud.Object.extend('mNode')
                    nodeInfo = Node()
                    nodeInfo.set('uhash', uhash)
                    nodeInfo.set('nodeid', nodeID)
                    nodeInfo.set('platform', platform)
                    nodeInfo.set('version', version)
                    nodeInfo.set('ip', self.request.remote_ip)
                    nodeInfo.save()
                    resp = {
                    'uuid': uuid,
                    'error': None,
                    'result': nodeID
                    }
                    self.write(md5(json.dumps(resp)) + '|' + encodestr(resp))
                elif act == 'get_task_list':
                    taskList = list()
                    stopList = list()
                    perPage, _ = getpage(leancloud.Query('mTask').equal_to('uhash', uhash).equal_to('status', 'wait'))
                    queueTaskList = getdata('mTask', perPage, uhash=uhash, status='wait')
                    perPage, _ = getpage(leancloud.Query('mTask').equal_to('uhash', uhash).equal_to('status', 'cancel'))
                    stopTaskList = getdata('mTask', perPage, uhash=uhash, status='cancel')
                    for item in queueTaskList:
                        policy = {
                        'entry': item.get('target'),
                        'plugins': item.get('plugins'),
                        'subdomain': item.get('subdomain'),
                        'scanport': item.get('scanport'),
                        'speed': item.get('speed'),
                        'timeout': item.get('timeout'),
                        'maxtask': item.get('maxpage'),
                        'disallow': item.get('exclude'),
                        'useragent': item.get('useragent'),
                        'cookie': item.get('cookie')
                        }
                        task = {
                        'id': item.get('tid'),
                        'target': gethost(item.get('target')),
                        'policy': base64.encodestring(json.dumps(policy))
                        }
                        taskList.append(task)
                    for item in stopTaskList:
                        stopList.append(item.get('tid'))
                    resp = {
                    'uuid': uuid,
                    'error': None,
                    'result': {
                        'nodever': 1.01,
                        'tasks': taskList,
                        'stops': stopList
                        }
                    }
                    self.write(md5(json.dumps(resp)) + '|' + encodestr(resp))
                elif act == 'get_plugin_list':
                    hashList = values[0]
                    pluginList = dict()
                    perPage, _ = getpage(leancloud.Query('mPlugin').contained_in('phash', hashList))
                    taskPluginList = getdata('mPlugin', perPage, phash=hashList)
                    for item in taskPluginList:
                        pluginList[item.get('phash')] = (item.get('phash'), encodeplugin(item.get('body')))
                    resp = {
                    'uuid': uuid,
                    'error': None,
                    'result': pluginList
                    }
                    self.write(md5(json.dumps(resp)) + '|' + encodestr(resp))
                elif act == 'set_task_status':
                    levels = {2: 'wait', 3: 'running', 5: 'completed', 6: 'stop', 7: 'cancel'}
                    tid, status = values
                    taskQuery = leancloud.Query('mTask')
                    taskQuery.equal_to('tid', tid)
                    taskInfo = taskQuery.first()
                    taskInfo.set('status', levels[status])
                    taskInfo.save()
                    resp = {
                    'uuid': uuid,
                    'error': None,
                    'result': {}
                    }
                    self.write(md5(json.dumps(resp)) + '|' + encodestr(resp))
                elif act == 'add_log':
                    tid, level, target, phash, body = values
                    levels = {0: 'note', 1: 'info', 2: 'warning', 3: 'hole'}
                    pluginQuery = leancloud.Query('mPlugin')
                    pluginQuery.equal_to('phash', phash)
                    pluginInfo = pluginQuery.first()
                    name = pluginInfo.get('name')
                    pluginInfo.increment('count')
                    pluginInfo.save()
                    Report = leancloud.Object.extend('mReport')
                    reportInfo = Report()
                    reportInfo.set('uhash', uhash)
                    reportInfo.set('tid', tid)
                    reportInfo.set('target', target)
                    reportInfo.set('level', levels[level])
                    reportInfo.set('name', name)
                    reportInfo.set('body', body)
                    reportInfo.save()
                    chash = sha1(uhash + tid)
                    self.deleteCache(redisCache, chash)
                    resp = {
                    'uuid': uuid,
                    'error': None,
                    'result': {}
                    }
                    self.write(md5(json.dumps(resp)) + '|' + encodestr(resp))
                elif act == 'set_task_progress':
                    resp = {
                    'uuid': uuid,
                    'error': None,
                    'result': {}
                    }
                    self.write(md5(json.dumps(resp)) + '|' + encodestr(resp))
                elif act == 'logout':
                    nodeQuery = leancloud.Query('mNode')
                    nodeQuery.equal_to('uhash', uhash)
                    nodeQuery.equal_to('nodeid', values[0])
                    leancloud.Object.destroy_all(nodeQuery.find())
                    resp = {
                    'uuid': uuid,
                    'error': None,
                    'result': {}
                    }
                    self.write(md5(json.dumps(resp)) + '|' + encodestr(resp))
                else:
                    resp = {
                    'uuid': uuid,
                    'error': 'Invalid intention',
                    'result': {}
                    }
                    self.write(md5(json.dumps(resp)) + '|' + encodestr(resp))
            else:
                self.write('This user has been blocked')