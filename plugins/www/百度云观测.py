import socket
import json

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    if not _G['subdomain']:
        return
    socket.setdefaulttimeout(5)
    domain = util.get_domain_root(arg)
    target = 'http://ce.baidu.com/index/getRelatedSites?site_address=' + domain
    code, head, res, err, _ = curl.curl(target)
    data = json.loads(res)
    if data.get('data'):
        for item in data['data']:
            try:
                hostname = item['domain']
                if not hostname.startswith('www.'):
                    security_info('subdomain discover: %s' % hostname)
                    task_push('www', 'http://%s/' % hostname, target=hostname)
                    task_push('ip', socket.gethostbyname(hostname), target=hostname)
            except Exception:
                pass