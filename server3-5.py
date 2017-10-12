#coding:utf8

'''
    正则提取变量
'''

from tornado.web import Application,RequestHandler
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options,define,parse_command_line

import config

define('port',default=9000,help='input port')


class PollHandler(RequestHandler):
    # 【注意】参数名可以随意指定
    def get(self, pid,*args, **kwargs):
        self.write(pid)

class Poll2Handler(RequestHandler):
    # 【注意】参数名必须和url中的名字相同
    def get(self, pid,name,*args, **kwargs):
        self.write(pid + ' ' + name)



if __name__ == '__main__':
    parse_command_line()
    app = Application(
        [
            (r'/poll/(\d+)',PollHandler), # 无名方式
            (r'/poll/(?P<pid>\d+)/(?P<name>[a-zA-Z0-9_]+)',Poll2Handler), # 命名方式
        ],
        debug=True
    )
    http_server = HTTPServer(app) # 实例化一个httpsever对象
    http_server.bind(options.port)
    http_server.start() # 参数默认1  进程数

    IOLoop.current().start()