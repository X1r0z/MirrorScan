import re

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    target = arg + 'testvulsbsbsbxzxzxz'
    code, head, body, err, _ = curl.curl(target)
    m=re.search(r'</th><td>[(&nbsp;)]*(.+)\\testvulsbsbsbxzxzxz', body)
    if m:
        security_info('WebRoot path discover: ' + m.group(1))