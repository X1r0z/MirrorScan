import urlparse
import socket
import json

def assign(service, arg):
    if service == 'ip':
        return True, arg

def audit(arg):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + arg
    code, head, res, err, _ = curl.curl(url)
    jsondata = json.loads(res)
    if jsondata.get('data'):
        security_info('Region: ' + jsondata['data']['region'])
        security_info('City: ' + jsondata['data']['city'])
        security_info('ISP: ' + jsondata['data']['isp'])
        security_info('IP: ' + jsondata['data']['ip'])
