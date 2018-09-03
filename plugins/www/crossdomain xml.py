def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    payload = '/crossdomain.xml'
    target = arg + payload
    code, head, res, err, _ = curl.curl2(target)
    if 'allow-access-from domain="*"' in res:
        security_note('crossdomain.xml: ' + target)
