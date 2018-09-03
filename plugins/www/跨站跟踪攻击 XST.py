import re

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    headers = {'Fuck': 'helloworld'}
    code, head, res, err, _ = curl.curl2(arg,header='Fuck: helloworld')
    if 'Fuck' in head or 'fuck' in head:
        if 'helloworld' in head:
            security_note('Cross Site Tracing (XST) discover: ' + arg)