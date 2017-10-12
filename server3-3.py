
# coding:utf8

'''
    获取请求体的信息
'''

from tornado.web import Application,RequestHandler,url
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define,options,parse_command_line

import config

define('port',default=9000,type=int,help='input port')

class IndexHandler(RequestHandler):
    def get(self):
        print 'method:',self.request.method
        print 'host:',self.request.host
        print 'uri:',self.request.uri
        print 'path:',self.request.path
        print 'query:',self.request.query
        print 'version:',self.request.version
        print 'type of headers:',type(self.request.headers)
        print 'User-Agent:',self.request.headers['User-Agent']
        print 'body:',self.request.body
        print 'remote_ip:',self.request.remote_ip
        print 'files:',self.request.files

        return self.render('index.html')


if __name__ == '__main__':
    parse_command_line()
    app = Application([
        (r'/',IndexHandler),
        ],
        **config.settings
    )
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.current().start()