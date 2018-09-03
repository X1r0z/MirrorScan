def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    payload = '/.svn/entries'
    target = arg + payload
    code, head, res, err, _ = curl.curl(target)
    if r'dir' in res or r'file' in res and code == 200:
        security_hole('SVN Repo discover: ' + target)
