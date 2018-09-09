# -*- coding:utf-8 -*-

import binascii
import hashlib
import random
import base64
import zlib
import json
import time
import re

def gethash():
	cur = str(random.random())
	return hashlib.sha1(cur).hexdigest()

def sha1(string):
	return hashlib.sha1(string).hexdigest()

def md5(string):
    return hashlib.md5(string).hexdigest()

def gettime():
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

def encodestr(raw):
	return base64.encodestring(zlib.compress(json.dumps(raw)))

def decodestr(raw):
	return json.loads(zlib.decompress(base64.decodestring(raw)))

def encodeplugin(raw):
    return binascii.b2a_hex(zlib.compress(raw))

def encodepass(raw):
    return md5(base64.encodestring(binascii.b2a_hex(md5(sha1(base64.encodestring(zlib.compress(raw)))))))

def gethost(url):
    if url.startswith('http'):
        url = url.strip('http://')
        url = url.strip('https://')
    if url.endswith('/'):
        url = url.strip('/')
    return url