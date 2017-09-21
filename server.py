# coding:utf8

import os
from datetime import datetime

import tornado.web
import tornado.httpserver
import tornado.ioloop

import torndb
from tornado.options import options,define,parse_command_line


base_dir = os.path.abspath(os.path.dirname(__file__))

define('port',default=8000,type=int,help='import the server port.')

class InsertHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.render('add.html')

    def post(self):
        name = self.get_argument("name")
        add_day = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        position = self.get_argument("position")
        gender = self.get_argument("gender")
        # insert_sql = "insert into users(name, add_day, position, gender) values('%s', '%s', '%s', '%s')" %(name, add_day, position, gender)
        try:
            result = self.application.db.execute("insert into users(name, add_day, position, gender) values(%s, %s, %s, %s)",name, add_day, position, gender)
            self.write("OK %d" % result)
        except Exception as e:
            self.write("DB error:%s" % e)

class GetHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        """访问方式为http://127.0.0.1/get?id=111"""
        id = self.get_argument('id')
        get_sql = 'select * from users where id="%s"' %id
        user = self.application.db.get(get_sql)
        print type(user) # <class 'torndb.Row'>
        return self.render('search.html',users=[user])

class QueryHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        position = self.get_argument('position')
        query_sql = 'select * from users where position="%s"' %position
        users = self.application.db.query(query_sql)
        print type(users)
        return self.render('search.html',users=users)


class App(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r'/add/',InsertHandler),
            (r'/get/',GetHandler),
            (r'/query/',QueryHandler),
        ]

        settings = dict(
            debug = True,
            static_path = os.path.join(base_dir,'static'),
            template_path = os.path.join(base_dir,'html'),
        )

        super(App,self).__init__(handlers,**settings)

        self.db = torndb.Connection(
            host='127.0.0.1',
            database='tornado',
            user='root',
            password='abc123!@#',
        )

if __name__ == '__main__':
    options.parse_command_line()
    app = App()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()