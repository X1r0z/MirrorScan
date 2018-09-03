import re

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    target = arg + '/robots.txt'
    code, head, res, err, _ = curl.curl(target)
    if code == 200:
        if re.search(r'Content\-Type:\s+[^\n]*text[^\n]+', head):
            security_note('robots.txt discover: ' + target)
