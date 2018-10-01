import hashlib

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    for appname, fingers in cmsdata.data.items():
        for item in fingers:
            path, value = item
            target = arg + path
            code, head, res, err, _ = curl.curl2(target)
            if code == 200:
                if value in res or hashlib.md5(res).hexdigest() == value:
                    security_info('CMS version discover: %s' % appname)
                    return