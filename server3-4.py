#coding:utf8
'''
    上传文件程序
'''

from tornado.web import Application,url
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options,define,parse_command_line

import config

define('port',default=9000,help='input port')

from common import BaseHandler

class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('upload.html')

    def post(self, *args, **kwargs):
        files = self.request.files.get('image',None) #  获取所有文件
        message = self.upload_file(files)
        self.write(message)

if __name__ == '__main__':
    app = Application([
        (r'/upload/',IndexHandler),
        ],
        **config.settings
    )
    http_server = HTTPServer(app)
    http_server.bind(options.port)
    http_server.start()
    IOLoop.current().start()