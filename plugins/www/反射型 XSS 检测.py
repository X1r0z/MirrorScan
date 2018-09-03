import urllib
import urlparse

def check_xss_get(url,payloads):
    data,payload = payloads
    code, head, res, err, _ = curl.curl2(url + '?' + data)
    if payload in res:
        return True
    else:
        return False

def check_xss_post(url,payloads):
    data,payload = payloads
    code, head, res, err, _ = curl.curl2(url,post=data)
    if payload in res:
        return True
    else:
        return False

def check_xss_cookie(url,payloads):
    data,payload = payloads
    code, head, res, err, _ = curl.curl2(url,cookie=data)
    if payload in res:
        return True
    else:
        return False

def splitparams(params):
    query = dict()
    if '&' in params:
        for arg in params.split('&'):
            if '=' in arg:
                name,value = arg.split('=',1)
                query[name] = value
    else:
        if '=' in params:
            name,value = params.split('=',1)
            query[name] = value
    return query

def joinparams(query,name,value):
    temp = query.copy()
    temp[name] = urllib.quote(value)
    params = '&'.join([k + '=' + v for k,v in temp.items()])
    return params

def assign(service,arg):
    if service == 'spider':
        return True,arg

def audit(arg):
    payloads = ["<script>alert(1)</script>",
                "<svg/onload=alert(1)>",
                '\" onmouseover=alert(0)']
    target,_ = arg
    params = urlparse.urlparse(target).query
    if params:
        url = target.split('?',1)[0]
        query = splitparams(params)
        for name in query:
            for payload in payloads:
                data = joinparams(query,name,payload)
                if check_xss_get(url,(data,payload)):
                    security_hole('Ref XSS GET [%s => %s] %s' %(name,payload,url))
                    break
                elif check_xss_post(url,(data,payload)):
                    security_hole('Ref XSS POST [%s => %s] %s' %(name,payload,url))
                    break
                elif check_xss_cookie(url,(data,payload)):
                    security_hole('Ref XSS COOKIE [%s => %s] %s' %(name,payload,url))
                    break
                else:
                    pass
