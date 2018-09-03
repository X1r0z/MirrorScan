import socket
import time

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    if _G['subdomain']:
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
                    l = socket.gethostbyname_ex(hostname)
                    security_info('subdomain discover: %s %s' %(hostname,str(l[2])))
                    time.sleep(0.01)
                except Exception:
                    pass
        else:
            security_info('Universal parsing discover: *.' + domain)
