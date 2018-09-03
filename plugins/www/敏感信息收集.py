import re

def assign(service, arg):
    if service == 'spider':
        return True, arg

def audit(arg):
    _,html = arg
    regexs = {'Email': r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?",
              'Mobilephone': r'^1(?:3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8\d|9\d)\d{8}$',
              'Telephone': r'\d{3}-\d{8}|\d{4}-\{7,8}',
              'ID Card': r'^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$'}
    for k,v in regexs.items():
        result = re.findall(v, html)
        for info in result:
            security_info('Infomation: %s %s' %(k,info))
