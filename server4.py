from tornado.web import Application,RequestHandler,url
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define,options,parse_command_line

import config

define('port',default=9000,type=int,help='input port')

class IndexHandler(RequestHandler):
    def get(self):
        return self.render('index.html')

    def post(self):
        query_arg = self.get_query_argument('a')
        query_args = self.get_query_arguments('a')
        body_arg = self.get_body_argument('a')
        body_args = self.get_body_arguments('a')
        arg = self.get_argument('a')
        args = self.get_arguments('a')

        print query_arg
        print query_args
        print body_arg
        print body_args
        print arg
        print args


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