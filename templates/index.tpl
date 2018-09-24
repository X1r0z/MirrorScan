<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta charset="utf-8" />
    <title>仪表板 - MirrorScan</title>

    <meta name="description" content="" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" />
    <link rel="icon" href="/static/favicon.ico">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/static/font-awesome/4.5.0/css/font-awesome.min.css" />
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
                    <a class="btn btn-success" href="/changelog">
                        <i class="ace-icon fa fa-signal"></i>
                    </a>

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
                <li class="active">
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

                <li class="">
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

                        <b class="arrow"></b>
                    </li>
                    <li class="">
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
                        <a href="/">主页</a>
                    </li>
                    <li class="active">仪表板</li>
                </ul>
            </div>

            <div class="page-content">
                <div class="page-header">
                    <h1>
                        仪表板
                        <small>
                            <i class="ace-icon fa fa-angle-double-right"></i>
                            总览 &amp; 状态
                        </small>
                    </h1>
                </div>

                <div class="row">
                    <div class="col-xs-12">
                        <div class="alert alert-block alert-success">
                            <button type="button" class="close" data-dismiss="alert">
                                <i class="ace-icon fa fa-times"></i>
                            </button>

                            <i class="ace-icon fa fa-check green"></i>

                            欢迎来到
                            <strong class="green">
                                云镜 (MirrorScan)
                                <small>v2.3</small>
                            </strong>
                            !
                        </div>
                        <div class="row">
                            <div class="col-sm-6">
                                <div class="widget-box transparent">
                                    <div class="widget-header widget-header-flat">
                                        <h4 class="widget-title lighter">
                                            <i class="ace-icon fa fa-star orange"></i>
                                            Top5 插件
                                        </h4>

                                        <div class="widget-toolbar">
                                            <a href="#" data-action="collapse">
                                                <i class="ace-icon fa fa-chevron-up"></i>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="widget-body">
                                        <div class="widget-main no-padding">
                                            <table class="table table-bordered table-striped">
                                                <thead class="thin-border-bottom">
                                                    <tr>
                                                        <th>
                                                            <i class="ace-icon fa fa-caret-right blue"></i>名称
                                                        </th>

                                                        <th>
                                                            <i class="ace-icon fa fa-caret-right blue"></i>服务
                                                        </th>

                                                        <th class="hidden-480">
                                                            <i class="ace-icon fa fa-caret-right blue"></i>调用
                                                        </th>
                                                    </tr>
                                                </thead>

                                                <tbody>
                                                    {% for item in top %}
                                                    <tr>
                                                        <td>{{ item.get('name') }}</td>

                                                        <td>
                                                            <b class="blue">{{ item.get('service') }}</b>
                                                        </td>

                                                        <td class="hidden-480">
                                                            {{ item.get('count') }}
                                                        </td>
                                                    </tr>
                                                    {% end %}
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-sm-5">
                                <div class="widget-box">
                                    <div class="widget-header widget-header-flat widget-header-small">
                                        <h5 class="widget-title">
                                            <i class="ace-icon fa fa-signal"></i>
                                            漏洞
                                        </h5>
                                    </div>

                                    <div class="widget-body">
                                        <div class="widget-main">
                                            <div id="piechart-placeholder"></div>

                                            <div class="hr hr8 hr-double"></div>

                                            <div class="clearfix">
                                                <div class="grid3">
                                                    <span class="grey">
                                                        &nbsp; 运行中
                                                    </span>
                                                    <h4 class="bigger pull-right">{{ running }}</h4>
                                                </div>

                                                <div class="grid3">
                                                    <span class="grey">
                                                        &nbsp; 等待
                                                    </span>
                                                    <h4 class="bigger pull-right">{{ wait }}</h4>
                                                </div>

                                                <div class="grid3">
                                                    <span class="grey">

                                                        &nbsp; 已完成
                                                    </span>
                                                    <h4 class="bigger pull-right">{{ completed }}</h4>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
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
    <script src="/static/js/jquery.easypiechart.min.js"></script>
    <script src="/static/js/jquery.sparkline.index.min.js"></script>
    <script src="/static/js/jquery.flot.min.js"></script>
    <script src="/static/js/jquery.flot.pie.min.js"></script>
    <script src="/static/js/jquery.flot.resize.min.js"></script>
    <script src="/static/js/ace-elements.min.js"></script>
    <script src="/static/js/ace.min.js"></script>

    <script type="text/javascript">
        jQuery(function($) {
            $('.easy-pie-chart.percentage').each(function(){
                var $box = $(this).closest('.infobox');
                var barColor = $(this).data('color') || (!$box.hasClass('infobox-dark') ? $box.css('color') : 'rgba(255,255,255,0.95)');
                var trackColor = barColor == 'rgba(255,255,255,0.95)' ? 'rgba(255,255,255,0.25)' : '#E2E2E2';
                var size = parseInt($(this).data('size')) || 50;
                $(this).easyPieChart({
                    barColor: barColor,
                    trackColor: trackColor,
                    scaleColor: false,
                    lineCap: 'butt',
                    lineWidth: parseInt(size/10),
                    animate: ace.vars['old_ie'] ? false : 1000,
                    size: size
                });
            })

            $('.sparkline').each(function(){
                var $box = $(this).closest('.infobox');
                var barColor = !$box.hasClass('infobox-dark') ? $box.css('color') : '#FFF';
                $(this).sparkline('html',
                {
                    tagValuesAttribute:'data-values',
                    type: 'bar',
                    barColor: barColor ,
                    chartRangeMin:$(this).data('min') || 0
                });
            });

              $.resize.throttleWindow = false;

              var placeholder = $('#piechart-placeholder').css({'width':'90%' , 'min-height':'150px'});
              var data = [
              { label: "Hole",  data: {{ hole }}, color: "#DA5430"},
              { label: "Warn",  data: {{ warn }}, color: "#FEE074"},
              { label: "Info",  data: {{ info }}, color: "#2091CF"},
              { label: "Note",  data: {{ note }}, color: "#68BC31"},
              ]
              function drawPieChart(placeholder, data, position) {
                  $.plot(placeholder, data, {
                    series: {
                        pie: {
                            show: true,
                            tilt:0.8,
                            highlight: {
                                opacity: 0.25
                            },
                            stroke: {
                                color: '#fff',
                                width: 2
                            },
                            startAngle: 2
                        }
                    },
                    legend: {
                        show: true,
                        position: position || "ne",
                        labelBoxBorderColor: null,
                        margin:[-30,15]
                    }
                    ,
                    grid: {
                        hoverable: true,
                        clickable: true
                    }
                })
              }
              drawPieChart(placeholder, data);

             placeholder.data('chart', data);
             placeholder.data('draw', drawPieChart);

              var $tooltip = $("<div class='tooltip top in'><div class='tooltip-inner'></div></div>").hide().appendTo('body');
              var previousPoint = null;

              placeholder.on('plothover', function (event, pos, item) {
                if(item) {
                    if (previousPoint != item.seriesIndex) {
                        previousPoint = item.seriesIndex;
                        var tip = item.series['label'] + " : " + item.series['percent']+'%';
                        $tooltip.show().children(0).text(tip);
                    }
                    $tooltip.css({top:pos.pageY + 10, left:pos.pageX + 10});
                } else {
                    $tooltip.hide();
                    previousPoint = null;
                }

            });

                $(document).one('ajaxloadstart.page', function(e) {
                    $tooltip.remove();
                });


                var d1 = [];
                for (var i = 0; i < Math.PI * 2; i += 0.5) {
                    d1.push([i, Math.sin(i)]);
                }

                var d2 = [];
                for (var i = 0; i < Math.PI * 2; i += 0.5) {
                    d2.push([i, Math.cos(i)]);
                }

                var d3 = [];
                for (var i = 0; i < Math.PI * 2; i += 0.2) {
                    d3.push([i, Math.tan(i)]);
                }

                var agent = navigator.userAgent.toLowerCase();
                if(ace.vars['touch'] && ace.vars['android']) {
                  $('#tasks').on('touchstart', function(e){
                    var li = $(e.target).closest('#tasks li');
                    if(li.length == 0)return;
                    var label = li.find('label.inline').get(0);
                    if(label == e.target || $.contains(label, e.target)) e.stopImmediatePropagation() ;
                });
              }

              $('#tasks').sortable({
                opacity:0.8,
                revert:true,
                forceHelperSize:true,
                placeholder: 'draggable-placeholder',
                forcePlaceholderSize:true,
                tolerance:'pointer',
                stop: function( event, ui ) {
                        $(ui.item).css('z-index', 'auto');
                    }
                }
                );
              $('#tasks').disableSelection();
              $('#tasks input:checkbox').removeAttr('checked').on('click', function(){
                if(this.checked) $(this).closest('li').addClass('selected');
                else $(this).closest('li').removeClass('selected');
            });

                $('#task-tab .dropdown-hover').on('mouseenter', function(e) {
                    var offset = $(this).offset();

                    var $w = $(window)
                    if (offset.top > $w.scrollTop() + $w.innerHeight() - 100)
                        $(this).addClass('dropup');
                    else $(this).removeClass('dropup');
                });})
    </script>
</body>
</html>