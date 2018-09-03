# -*- coding:utf-8 -*-

from controller import Index
from controller import Login
from controller import Logout
from controller import Register
from controller import User
from controller import Task
from controller import Plugin
from controller import Node
from controller import U
from controller import Service

urls = [
    (r'/', Index.IndexHandler),
    (r'/login', Login.LoginHandler),
    (r'/logout', Logout.LogoutHandler),
    (r'/register', Register.RegisterHandler),
    (r'/user', User.UserHandler),
    (r'/task/?([A-Za-z]{3,6})?/?([0-9a-z]{40})?', Task.TaskHandler),
    (r'/plugin/?([A-Za-z]{3,4})?/?([0-9a-z]{40})?', Plugin.PluginHandler),
    (r'/node/?([A-Za-z]{4})?/?([0-9]{1,})?', Node.NodeHandler),
    (r'/u/([0-9a-z]{40})/?(\w{4})?', U.UHandler),
    (r'/service', Service.ServiceHandler),
]