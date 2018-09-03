import urllib
import urlparse

def check_sqli_get(url,payloads):
    origin,true,false = payloads
    code, head, res1, err, _ = curl.curl2(url + '?' + origin)
    code, head, res2, err, _ = curl.curl2(url + '?' + true)
    code, head, res3, err, _ = curl.curl2(url + '?' + false)
    set1 = set([i for i in res1.split('\n')])
    set2 = set([i for i in res2.split('\n')])
    set3 = set([i for i in res3.split('\n')])
    diff1 =  set1 - set2
    diff2 = set1 - set3
    diff3 = set2 - set3
    if len(diff1) < len(diff3):
        return True
    else:
        return False

def check_sqli_post(url,payloads):
    origin,true,false = payloads
    code, head, res1, err, _ = curl.curl2(url + '?' + origin)
    code, head, res2, err, _ = curl.curl2(url, post=true)
    code, head, res3, err, _ = curl.curl2(url, post=false)
    set1 = set([i for i in res1.split('\n')])
    set2 = set([i for i in res2.split('\n')])
    set3 = set([i for i in res3.split('\n')])
    diff1 =  set1 - set2
    diff2 = set1 - set3
    diff3 = set2 - set3
    if len(diff1) < len(diff3):
        return True
    else:
        return False

def check_sqli_cookie(url,payloads):
    origin,true,false = payloads
    code, head, res1, err, _ = curl.curl2(url + '?' + origin)
    code, head, res2, err, _ = curl.curl2(url, cookie=true)
    code, head, res3, err, _ = curl.curl2(url, cookie=false)
    set1 = set([i for i in res1.split('\n')])
    set2 = set([i for i in res2.split('\n')])
    set3 = set([i for i in res3.split('\n')])
    diff1 =  set1 - set2
    diff2 = set1 - set3
    diff3 = set2 - set3
    if len(diff1) < len(diff3):
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
    temp[name] += urllib.quote(value)
    params = '&'.join([k + '=' + v for k,v in temp.items()])
    return params

def assign(service,arg):
    if service == 'spider':
        return True,arg

def audit(arg):
    payloads = {" and 1=1": " and 1=2",
                " and (1=1)": " and (1=2)",
                "' and '1'='1": "' and '1'='2"}
    target,_ = arg
    params = urlparse.urlparse(target).query
    if params:
        url = target.split('?',1)[0]
        query = splitparams(params)
        for name in query:
            for ptrue,pfalse in payloads.items():
                true = joinparams(query,name,ptrue)
                false = joinparams(query,name,pfalse)
                if check_sqli_get(url,(params,true,false)):
                    security_hole('SQL Injection GET [%s => %s] %s' %(name,ptrue.strip(),url))
                    break
                elif check_sqli_post(url,(params,true,false)):
                    security_hole('SQL Injection POST [%s => %s] %s' %(name,ptrue.strip(),url))
                    break
                elif check_sqli_cookie(url,(params,true,false)):
                    security_hole('SQL Injection COOKIE [%s => %s] %s' %(name,ptrue.strip(),url))
                    break
                else:
                    pass
