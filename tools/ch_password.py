import binascii
import hashlib
import random
import base64
import zlib
import sys

def sha1(string):
    return hashlib.sha1(string).hexdigest()

def md5(string):
    return hashlib.md5(string).hexdigest()

def encodepass(raw):
    return md5(base64.encodestring(binascii.b2a_hex(md5(sha1(base64.encodestring(zlib.compress(raw)))))))

APP_ID = '9RLabat5zEzNkYtwQW1Rn5sK-gzGzoHsz'

APP_KEY = 'M38DE3wMfrPA4HHeRaUkyoIR'

MASTER_KEY = 'EFNMBnGv5KazPMgzTNokpj6e'

import leancloud

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(False)

username = sys.argv[1]

password = sys.argv[2]

userQuery = leancloud.Query('mUser')
userQuery.equal_to('username', username)
userInfo = userQuery.first()
userInfo.set('password', encodepass(password))
userInfo.save()

print 'User:', username, 'Password:', password