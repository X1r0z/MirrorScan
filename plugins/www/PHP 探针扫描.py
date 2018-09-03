import re

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    phpinfo_list = [
    '/phpinfo.php',
    '/PhpInfo.php',
    '/PHPinfo.php',
    '/PHPINFO.php',
    '/phpInfo.php'
    '/info.php',
    '/Info.php',
    '/INFO.php',
    '/test.php?mode=phpinfo',
    '/index.php?view=phpinfo',
    '/index.php?mode=phpinfo',
    '/TEST.php?mode=phpinfo',
    '/?mode=phpinfo',
    '/?view=phpinfo',
    '/install.php?mode=phpinfo',
    '/INSTALL.php?mode=phpinfo',
    '/admin.php?mode=phpinfo',
    '/phpversion.php',
    '/phpVersion.php',
    '/test.php',
    '/test1.php',
    '/test2.php',
    '/phpinfo1.php',
    '/info1.php',
    '/PHPversion.php',
    '/version.php',
    '/x.php',
    '/xx.php',
    '/xxx.php',
    '/l.php'
    ]
    for path in phpinfo_list:
        target = arg + path
        code, head, res, err, _ = curl.curl(target)
        if code == 200:
            if 'allow_url_fopen' in res:
                security_note('phpinfo probe discover: ' + target)
