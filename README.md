# MirrorScan

云镜 (MirrorScan) 是一款模仿 BugScan 分布式节点架构的插件化 Web 漏洞扫描器

节点代码基于 BugScan 二次开发

项目基于 Tornado LeanCloud Redis

## Features

插件化

分布式节点扫描

## Usage

使用前请自行注册 LeanCloud 并配置相关服务 (含 Redis), 在 config.py 中填写相关信息

## SDK

代码兼容 BugScan 的插件编写规范

目前内置 minicurl hackhttp 模块

```python
def assign(service, arg):
    if service == 'www':
        return True, arg

def audit(arg):
    target = arg + '/phpinfo.php'
    code, head, res, err, _ = curl.curl2(target)
    if code == 200 and 'allow_url_include' in res:
        security_hole('phpinfo [allow_url_include] discover: ' + target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://127.0.0.1/'))
``` 
