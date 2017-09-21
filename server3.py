from tornado.web import Application,RequestHandler,url
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import tornado.options
import config

tornado.options.define('port',default=8000,type=int,help='import the server port.')

class IndexHandler(RequestHandler):
    def get(self):
        handler2_url = self.reverse_url('handler2')
        self.write("<a href='%s'>handler2</a>" %handler2_url)

class IndexHandler2(RequestHandler):
    def initialize(self,arg):
        self.arg = arg

    def get(self):
        self.write(self.arg)

handlers = [
    (r'/',IndexHandler),
    url(r'/2/',IndexHandler2,{'arg':'hello'},name='handler2'),
]

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application(handlers=handlers,**config.settings)
    http_server = HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    IOLoop.current().start()
