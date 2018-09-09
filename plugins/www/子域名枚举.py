import socket
import time

def assign(service, arg):
    if service == 'dns':
        return True, arg

def audit(arg):
    if not _G['subdomain']:
        return
    socket.setdefaulttimeout(5)
    domain = util.get_domain_root(arg)
    tlds = util.list_from_file("database/sub_domain.txt")
    unable_pro = "stackoverflowsb"
    hostname = unable_pro + "." + domain
    try:
        socket.gethostbyname_ex(hostname)
    except Exception:
        for pro in tlds:
            hostname = pro + "." + domain
            try:
                ip = socket.gethostbyname(hostname)
                security_info('subdomain discover: %s %s' %(hostname, ip))
                if hostname != arg and pro != 'www':
                    task_push('ip', ip, target=hostname)
                    task_push('www', 'http://%s/' % hostname, target=hostname)
            except Exception:
                pass
    else:
        security_info('Universal parsing discover: *.' + domain)