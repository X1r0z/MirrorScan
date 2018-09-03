import urlparse

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    code, head, res, err, _ = curl.curl(arg + '%2F*~1.*%2Fx.aspx')
    if code == 404:
        code, head, res, err, _ = curl.curl(arg + '%2Fooxx*~1.*%2Fx.aspx')
        if code == 400:
            security_info('IIS ShortName discover: ' + arg)
