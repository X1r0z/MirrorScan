import urlparse
import re

old_url = set()
new_url = set()
ignore = ['.jpg', '.jpeg', '.gif','.png','.bmp',
          '.doc','.docx','.xsl','.xslx','.csv',
          '.ppt', '.pptx', '.pdf','.rar','.zip',
          '.7z', '.css', '.js', 'swf', '.html']

def crawl(domain):
    while new_url:
        url = new_url.pop()
        code, head, res, err, _ = curl.curl2(url)
        if code == 200:
            task_push('spider',(url, res))
            urls = re.findall(r'<a[^>]+href=["\'](.*?)["\']',res,re.I)
            for murl in urls:
                murl = urlparse.urljoin(url, murl)
                if util.get_url_host(murl) == domain:
                    turl = urlparse.urlparse(murl).path
                    if turl not in old_url and murl not in new_url:
                        if util.get_url_ext(turl) not in ignore:
                            old_url.add(turl)
                            new_url.add(murl)

def assign(service,arg):
    if service == 'www':
        return True, arg

def audit(arg):
    domain = util.get_url_host(arg)
    new_url.add(arg)
    crawl(domain)
