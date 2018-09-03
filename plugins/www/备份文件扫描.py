import urlparse

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
        url = urlparse.urlparse(arg).netloc
        a = ('bak','backup','www','web','wwwroot','beifen','ftp','website','back','backupdata','temp','htdocs','database','data','user','admin','test','conf','config','db','sql','install','bf')
        b = (url,url.replace('.',''),url.split('.',1)[1],url.split('.',1)[0],url.split('.')[1],url.split('.')[-1])
        c = ('.rar','.zip','.tar','.tar.gz','.tar.bz2','.tar.xz','.gz','.bz2','.xz','.tgz','.7z','.z')
        backup_list = [x + y for x in a for y in c] + [x + y for x in b for y in c]
        for backup in backup_list:
            target = arg + backup
            code, head, res, err, _ = curl.curl2(target)
            if code == 200 and 'Content-Type: application' in head:
                security_warning('Web Backup File discover: ' + target)