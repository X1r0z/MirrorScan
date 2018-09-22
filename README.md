# MirrorScan

云镜 (MirrorScan) 是一款模仿 bugscan 的插件化扫描器

节点代码基于 bugscan

## Features

节点扫描

## Sdk

代码兼容 bugscan 的插件编写规范

目前仅内置 miniCurl 模块

示例

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

## Changelogs

**v2.2**

目前可在手机挂载节点 (Termux)

增加分页功能, 在任务和插件处可查看

优化前端模板的加载速度, 删除不必要的引用和注释

移除 Dashboard 中的统计信息, 现只含图表和 Top5 插件

修复百度云观测与子域名枚举插件的冲突, 漏报问题, 优化服务发现插件

节点列表现可显示 IP 地址

删除生成邀请码的脚本

**v2.1**

智能插件导入 (create or update)

支持对子域名及 web 服务端口的扫描

优化任务报告页面, 可显示不同子域名的扫描信息

修复在子域名和端口一起使用时重复使用插件扫描的问题

增加停止扫描任务的选项

**v2.0**

项目改名 云镜 (MirrorScan)

后端换为 Tornado LeanCloud

对导入插件脚本的功能进行修改

添加生成邀请码的脚本

**v1.4**

增加插件调用次数, 可在 Dashboard 查看 Top5 插件

Dashboard 现可显示注册人数 扫描 报告数量等统计信息

增加爬虫插件, 可检测多种提交方式的 SQL 注入和反射型 XSS

**v1.2**

插件列表只显示私有插件, 公共插件不再显示且不可查看

插件默认为私有, 需联系管理员进行修改

扫描任务增加子域名和端口的可选项

**v1.1**

前端替换为 Ace Admin

更换成 Bugscan 的节点源码

启动前使用 compile 编译文件

任务扫描报告使用新的手风琴界面

删除原有的插件助手和代码编辑器

**v1.0**

增加邀请码机制

修复业务逻辑缺陷

可通过脚本自定义导入模块

增加插件编写助手和编辑器

Dashboard 可显示漏洞统计及任务状态

整理并导入 bugscan 中的 www 类插件

**v0.1**

项目第一版

采用自写节点

使用 Django Flat UI