<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta charset="utf-8" />
    <title>编辑插件 - MirrorScan</title>

    <meta name="description" content="" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" />
    <link rel="icon" href="/static/favicon.ico">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/static/font-awesome/4.5.0/css/font-awesome.min.css" />
    <link rel="stylesheet" href="/static/css/jquery-ui.custom.min.css" />
    <link rel="stylesheet" href="/static/css/chosen.min.css" />
    <link rel="stylesheet" href="/static/css/fonts.googleapis.com.css" />
    <link rel="stylesheet" href="/static/css/ace.min.css" class="ace-main-stylesheet" id="main-ace-style" />
    <link rel="stylesheet" href="/static/css/ace-skins.min.css" />
    <link rel="stylesheet" href="/static/css/ace-rtl.min.css" />
    <script src="/static/js/ace-extra.min.js"></script>
</head>

<body class="no-skin">
    <div id="navbar" class="navbar navbar-default ace-save-state">
        <div class="navbar-container ace-save-state" id="navbar-container">
            <button type="button" class="navbar-toggle menu-toggler pull-left" id="menu-toggler" data-target="#sidebar">
                <span class="sr-only">Toggle sidebar</span>

                <span class="icon-bar"></span>

                <span class="icon-bar"></span>

                <span class="icon-bar"></span>
            </button>

            <div class="navbar-header pull-left">
                <a href="/" class="navbar-brand">
                    <small>
                        <i class="fa fa-leaf"></i>
                        MirrorScan
                    </small>
                </a>
            </div>

            <div class="navbar-buttons navbar-header pull-right" role="navigation">
                <ul class="nav ace-nav">

                    <li class="light-blue dropdown-modal">
                        <a data-toggle="dropdown" href="#" class="dropdown-toggle">
                            <img class="nav-user-photo" src="/static/images/avatars/user.jpg" alt="Jason's Photo" />
                            <span class="user-info">
                                <small>欢迎你,</small>
                                {{ user }}
                            </span>

                            <i class="ace-icon fa fa-caret-down"></i>
                        </a>

                        <ul class="user-menu dropdown-menu-right dropdown-menu dropdown-yellow dropdown-caret dropdown-close">
                            <li>
                                <a href="/user">
                                    <i class="ace-icon fa fa-user"></i>
                                    个人信息
                                </a>
                            </li>

                            <li class="divider"></li>

                            <li>
                                <a href="/logout">
                                    <i class="ace-icon fa fa-power-off"></i>
                                    登出
                                </a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <div class="main-container ace-save-state" id="main-container">
        <script type="text/javascript">
            try{ace.settings.loadState('main-container')}catch(e){}
        </script>

        <div id="sidebar" class="sidebar responsive ace-save-state">
            <script type="text/javascript">
                try{ace.settings.loadState('sidebar')}catch(e){}
            </script>

            <div class="sidebar-shortcuts" id="sidebar-shortcuts">
                <div class="sidebar-shortcuts-large" id="sidebar-shortcuts-large">
                    <button class="btn btn-success">
                        <i class="ace-icon fa fa-signal"></i>
                    </button>

                    <button class="btn btn-info">
                        <i class="ace-icon fa fa-pencil"></i>
                    </button>

                    <button class="btn btn-warning">
                        <i class="ace-icon fa fa-users"></i>
                    </button>

                    <button class="btn btn-danger">
                        <i class="ace-icon fa fa-cogs"></i>
                    </button>
                </div>

                <div class="sidebar-shortcuts-mini" id="sidebar-shortcuts-mini">
                    <span class="btn btn-success"></span>

                    <span class="btn btn-info"></span>

                    <span class="btn btn-warning"></span>

                    <span class="btn btn-danger"></span>
                </div>
            </div>

            <ul class="nav nav-list">
                <li class="">
                    <a href="/">
                        <i class="menu-icon fa fa-tachometer"></i>
                        <span class="menu-text"> 仪表板 </span>
                    </a>

                    <b class="arrow"></b>
                </li>

                <li class="">
                    <a href="#" class="dropdown-toggle">
                        <i class="menu-icon fa fa-desktop"></i>
                        <span class="menu-text">
                            节点
                        </span>

                        <b class="arrow fa fa-angle-down"></b>
                    </a>

                    <b class="arrow"></b>

                    <ul class="submenu">
                        <li class="">
                            <a href="/node">
                                <i class="menu-icon fa fa-caret-right"></i>
                                列表
                            </a>

                            <b class="arrow"></b>
                        </li>
                    </ul>
                </li>

                <li class="">
                    <a href="#" class="dropdown-toggle">
                        <i class="menu-icon fa fa-list"></i>
                        <span class="menu-text"> 任务 </span>

                        <b class="arrow fa fa-angle-down"></b>
                    </a>

                    <b class="arrow"></b>

                    <ul class="submenu">
                        <li class="">
                            <a href="/task">
                                <i class="menu-icon fa fa-caret-right"></i>
                                列表
                            </a>

                            <b class="arrow"></b>
                        </li>
                        <li class="">
                            <a href="/task/Add">
                                <i class="menu-icon fa fa-caret-right"></i>
                                添加
                            </a>

                            <b class="arrow"></b>
                        </li>
                    </ul>
                </li>

                <li class="active">
                    <a href="#" class="dropdown-toggle">
                        <i class="menu-icon fa fa-pencil-square-o"></i>
                        <span class="menu-text"> 插件 </span>

                        <b class="arrow fa fa-angle-down"></b>
                    </a>

                    <b class="arrow"></b>

                    <ul class="submenu">
                        <li class="">
                            <a href="/plugin">
                                <i class="menu-icon fa fa-caret-right"></i>
                                列表
                            </a>
                        </li>
                        <li class="active">
                            <a href="/plugin/Edit">
                                <i class="menu-icon fa fa-caret-right"></i>
                                添加
                            </a>

                            <b class="arrow"></b>
                        </li>

                    </ul>
                </li>

                <li class="">
                    <a href="/">
                        <i class="menu-icon fa fa-list-alt"></i>
                        <span class="menu-text"> 开发中 </span>
                    </a>

                    <b class="arrow"></b>
                </li>

            </ul>
        </div>

        <div class="main-content">
            <div class="main-content-inner">
                <div class="breadcrumbs ace-save-state" id="breadcrumbs">
                    <ul class="breadcrumb">
                        <li>
                            <i class="ace-icon fa fa-home home-icon"></i>
                            <a href="/home">主页</a>
                        </li>

                        <li>
                            <a href="/plugin">插件</a>
                        </li>
                        <li class="active">编辑插件</li>
                    </ul>
                </div>

                <div class="page-content">
                    <div class="page-header">
                        <h1>
                            插件
                            <small>
                                <i class="ace-icon fa fa-angle-double-right"></i>
                                编辑插件
                            </small>
                        </h1>
                    </div>

                    <div class="row">
                        <div class="col-xs-12">
                            <form class="form-horizontal" role="form" action="/plugin/Edit/{% if 'info' in globals() %}{{ info.get('phash') }}{% else %}{% end %}" method="post" id="form">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label no-padding-right"> 名称 </label>
                                    <div class="col-sm-9">
                                        <input type="text" class="col-xs-10 col-sm-5" name="name" value="{% if 'info' in globals() %}{{ info.get('name') }}{% else %}{% end %}" />
                                    </div>
                                </div>

                                <div class="form-group">
                                    <label class="col-sm-3 control-label no-padding-right"> 作者 </label>
                                    <div class="col-sm-9">
                                        <input type="text"class="col-xs-10 col-sm-5" name="author" value="{% if 'info' in globals() %}{{ info.get('author') }}{% else %}{% end %}" />
                                    </div>
                                </div>

                                <div class="form-group">
                                    <label class="col-sm-3 control-label no-padding-right"> 服务 </label>
                                    <div class="col-sm-9">
                                        <input type="text" class="col-xs-10 col-sm-5" name="service" value="{% if 'info' in globals() %}{{ info.get('service') }}{% else %}{% end %}" />
                                    </div>
                                </div>

                                <div class="form-group">
                                    <label class="col-sm-3 control-label no-padding-right"> 信息 </label>
                                    <div class="col-sm-9">
                                        <input type="text" class="col-xs-10 col-sm-5" name="info" value="{% if 'info' in globals() %}{{ info.get('info') }}{% else %}{% end %}" />
                                    </div>
                                </div>

                                <div class="form-group">
                                    <label class="col-sm-3 control-label no-padding-right"> 代码 </label>
                                    <div class="col-sm-9">
                                        <textarea class="form-control" name="body" style="width:41.55%;height:400px">
{% if 'info' in globals() %}{{ info.get('body') }}{% else %}def assign(service, arg):
    if service == "www":
        return True, arg

    def audit(arg):
        payload = ''
        target = arg + payload
        code, head, res, err, _ = curl.curl2(target)
        if 'flag' in res:
            security_note(target){% end %}</textarea>
                                    </div>
                                </div>

                                <div class="clearfix form-actions">
                                    <div class="col-md-offset-3 col-md-9">
                                        <button class="btn btn-info" type="submit" form="form">
                                            <i class="ace-icon fa fa-check bigger-110"></i>
                                            提交
                                        </button>
                                        &nbsp; &nbsp; &nbsp;
                                        <button class="btn" type="reset">
                                            <i class="ace-icon fa fa-undo bigger-110"></i>
                                            清空
                                        </button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="footer">
            <div class="footer-inner">
                <div class="footer-content">
                    <span class="bigger-120">
                        <span class="blue bolder">云镜</span>
                        MirrorScan &copy; 2018
                    </span>

                    &nbsp; &nbsp;
                    <span class="action-buttons">
                        <a href="#">
                            <i class="ace-icon fa fa-twitter-square light-blue bigger-150"></i>
                        </a>

                        <a href="#">
                            <i class="ace-icon fa fa-facebook-square text-primary bigger-150"></i>
                        </a>

                        <a href="#">
                            <i class="ace-icon fa fa-rss-square orange bigger-150"></i>
                        </a>
                    </span>
                </div>
            </div>
        </div>

        <a href="#" id="btn-scroll-up" class="btn-scroll-up btn btn-sm btn-inverse">
            <i class="ace-icon fa fa-angle-double-up icon-only bigger-110"></i>
        </a>
</div>

    <script src="/static/js/jquery-2.1.4.min.js"></script>
    <script type="text/javascript">
        if('ontouchstart' in document.documentElement) document.write("<script src='/static/js/jquery.mobile.custom.min.js'>"+"<"+"/script>");
    </script>
    <script src="/static/js/bootstrap.min.js"></script>
    <script src="/static/js/jquery-ui.custom.min.js"></script>
    <script src="/static/js/jquery.ui.touch-punch.min.js"></script>
    <script src="/static/js/ace-elements.min.js"></script>
    <script src="/static/js/ace.min.js"></script>
</body>
</html>
