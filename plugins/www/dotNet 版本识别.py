import re

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    target = arg + '/~.aspx'
    code, head, res, err, _ = curl.curl(target)
    if code == 404:
        regex = re.search(r'Microsoft .NET Framework [^:\n]+:[\d\.]+;[^\r\n<]+', res, re.M | re.I)
        if regex:
            security_note('.Net Version discover: ' + regex.group(0))
