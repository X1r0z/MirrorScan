import hashlib
import random
import os

def gethash():
    cur = str(random.random())
    return hashlib.sha1(cur).hexdigest()

BASE_DIR = os.path.abspath('..')

PLUGIN_DIR = 'plugins'

AUTHOR = 'X1r0z'

USERNAME = 'exp10it'

PRIVATE = False

COUNT = 0

APP_ID = '9RLabat5zEzNkYtwQW1Rn5sK-gzGzoHsz'

APP_KEY = 'M38DE3wMfrPA4HHeRaUkyoIR'

MASTER_KEY = 'EFNMBnGv5KazPMgzTNokpj6e'

import leancloud

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(False)

userQuery = leancloud.Query('mUser')
userQuery.equal_to('username', USERNAME)
userInfo = userQuery.first()
uhash = userInfo.get('uhash')

pluginQuery = leancloud.Query('mPlugin')
leancloud.Object.destroy_all(pluginQuery.find())

for folder in os.listdir(os.path.join(BASE_DIR,PLUGIN_DIR)):
    for file in os.listdir(os.path.join(BASE_DIR,PLUGIN_DIR,folder)):
        path = os.path.join(BASE_DIR,PLUGIN_DIR,folder,file)
        name = file.split('.')[0]
        service = folder
        with open(path,'r') as f:
            body = f.read()
        Plugin = leancloud.Object.extend('mPlugin')
        pluginInfo = Plugin()
        pluginInfo.set('name', name)
        pluginInfo.set('info', name)
        pluginInfo.set('body', body)
        pluginInfo.set('author', AUTHOR)
        pluginInfo.set('service', service)
        pluginInfo.set('uhash', uhash)
        pluginInfo.set('phash', gethash())
        pluginInfo.set('private', PRIVATE)
        pluginInfo.set('count', COUNT)
        pluginInfo.save()
        print 'Load Plugin', name, 'successfully'

print len(os.listdir(os.path.join(BASE_DIR,PLUGIN_DIR,folder))), 'Plugins loaded'