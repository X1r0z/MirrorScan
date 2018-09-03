def assign(service, arg):
    if service == 'www':
        return True,arg

def audit(arg):
    target = arg + '/.git/config'
    code, head, res, err, _ = curl.curl2(target)
    if '[remote "origin"]' in res:
        security_hole('Git repo discover: ' + target)
