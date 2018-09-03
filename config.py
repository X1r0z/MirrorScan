# -*- coding:utf-8 -*-

from urls import urls

import marshal
import os

SCHEME = 'http'

HOST = 'mirrorscan.leanapp.cn'

INIT_FILE = 'init.py'

NODE_FILE = 'node.py'

DEBUG = False

BASE_DIR = os.path.dirname(__file__)

TEMPLATE_PATH = 'templates'

STATIC_PATH = 'static'

settings = {
    'handlers': urls,
    'cookie_secret': '5_pdecg&#s1g=ka_rrohm)v1-zyecoqxzmga9%abm7quvs6y^5',
    'template_path': os.path.join(BASE_DIR,TEMPLATE_PATH),
    'static_path': os.path.join(BASE_DIR,STATIC_PATH),
    'debug': DEBUG,
}


def render(text, context):
    if context:
        for k,v in context.items():
            name = '{{ %s }}' % k
            text = text.replace(name,v)
    return text

def compiles(name, context=None):
    with open('templates/bin/' + name, 'r') as f:
        text = f.read()
    with open('templates/bin/' + name + '.tpl', 'w+b') as f:
        content = render(text,context)
        marshal.dump(compile(content, 'templates/bin/' + name + 'c', 'exec'), f)
    return 'templates/bin/' + name + '.tpl'

INIT_FILE = compiles(INIT_FILE, {'host': HOST, 'scheme': SCHEME})
NODE_FILE = compiles(NODE_FILE)