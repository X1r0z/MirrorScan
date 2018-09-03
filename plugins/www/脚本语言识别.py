import re

def getScript(url):
    app_suffix = []
    signature_buff = ['php','asp.net']
    session_buff = ['aspsessionid-asp','jsessionid-jsp','phpsessid-php','asp.net_sessionid-aspx']
    web_suffix = ['php','asp','aspx','jsp']
    code, head, res, err, _ = curl.curl(url)
    if code == 200:
        m = re.search('X-Powered-By: (.*?)[\r|\n]+', head,flags=re.S)
        if m:
            buff = m.group(1).lower()
            for index in signature_buff:
                if index in buff:
                    app_suffix.append(index)
                    
        m = re.search('Set-Cookie: (.*?)=', head,flags=re.S)
        if m:
            buff = m.group(1).lower()
            for index in session_buff:
                if (index[:index.find('-')] in buff) and (index[index.find('-')+1:] not in app_suffix):
                    app_suffix.append(index[index.find('-')+1:])

        m = re.findall(r'href=(?:"|\'|\s)*[/\w]*\.(jsp|php|aspx|asp)',res,re.I)
        if m:
            max_buff = 'asp'
            for index in web_suffix:
                if m.count(index) > m.count(max_buff):
                    max_buff = index
            if max_buff not in app_suffix:
                app_suffix.append(max_buff)


        if 'asp' in app_suffix or 'aspx' in app_suffix :
            if 'asp.net' in app_suffix:app_suffix.remove('asp.net')
        if len(app_suffix) == 0:app_suffix.append('html')
    return app_suffix

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    app_suffix = getScript(arg)
    if len(app_suffix) != 0:
        security_note('Web Script suffix discover: ' + str(app_suffix))