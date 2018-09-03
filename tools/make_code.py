import hashlib
import random
import sys

def getcode():
    rnd = str(random.random())
    return hashlib.md5(rnd).hexdigest()

APP_ID = '9RLabat5zEzNkYtwQW1Rn5sK-gzGzoHsz'

APP_KEY = 'M38DE3wMfrPA4HHeRaUkyoIR'

MASTER_KEY = 'EFNMBnGv5KazPMgzTNokpj6e'

import leancloud

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(False)

number = int(sys.argv[1])

for _ in range(number):
    code = getcode()
    Invite = leancloud.Object.extend('mInvite')
    inviteInfo = Invite()
    inviteInfo.set('code', code)
    inviteInfo.save()
    print code