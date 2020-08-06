archive 仅作备份

config 中相关信息已作废

# MirrorScan

云镜 (MirrorScan) 是一款模仿 bugscan 的插件化扫描器.

节点代码基于 bugscan

项目基于 tornado leancloud redis

## Features

插件化

节点扫描

## SDK

代码兼容 bugscan 的插件编写规范.

目前内置 minicurl hackhttp 模块.

```
def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    target = arg + '/phpinfo.php'
    code, head, res, err, _ = curl.curl2(target)
    if code == 200 and 'allow_url_include' in res:
        security_hole('phpinfo discover: ' + target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://127.0.0.1/'))
``` 
