import re
import socket

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    data = 'testvul'
    target = arg + '/testvul.txt'
    code, head, body, err, _ = curl.curl('-T -d "%s" %s' % (data, target))
    if code == 200 or code == 201:
        for i in range(2):
            code, head, body, err, _ = curl.curl(target)
            if data in body:
                security_hole('IIS WebDav PUT method Allowed: ' + target)