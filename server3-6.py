#coding:utf8
'''
    3.3 输出
'''

from tornado.web import Application,RequestHandler
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options,define,parse_command_line

'''
    在同一个处理方法中多次使用write方法
'''
class IndexHandler(RequestHandler):
    def get(self):
        self.write('hello world')
        self.write('hello world')
        self.write('hello world')


'''
    利用write方法写json数据；set_header();set_default_headers()
'''
import json

class JsonHandler(RequestHandler):
    def get(self):
        print '我在get方法中'
        dic = {
            'name':'john',
            'age':'23',
            'position':'Shanghai'
        }
        js = json.dumps(dic)
        self.set_header("Content-Type","text/html;charset=UTF-8")
        self.write(js)

    def set_default_headers(self):
        print '我在设置默认headers'
        self.set_header('Content-Type',"application/json;charset=UTF-8")
        self.set_header('python','django')

'''
    为响应设置状态码set_status()
'''
class Error404Handler(RequestHandler):
    def get(self):
        self.write('hello 404')
        self.set_status(404) # 标准状态码，不用设置reason

class Error210Handler(RequestHandler):
    def get(self):
        self.write('hello 210')
        self.set_status(210)

'''
    重定向：redirect(url)
'''
class LoginHandler(RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        self.redirect('/')

'''
    抛出错误：send_error
'''
class SendErrorHandler(RequestHandler):
    def get(self):
        self.write('hello') # 不会显示在页面。报错后缓冲区的数据都丢失了
        self.send_error(404,content='找不到页面了')
        self.write('world')

    def write_error(self, status_code, **kwargs):
        self.write(kwargs['content'])


if __name__ == '__main__':
    app = Application([
        (r'/',IndexHandler),
        (r'/json/',JsonHandler),
        (r'/404/',Error404Handler),
        (r'/210/',Error210Handler),
        (r'/login/',LoginHandler),
        (r'/senderror/',SendErrorHandler),
        ],
        debug=True,
        template_path='html',
    )
    http_server = HTTPServer(app)
    http_server.bind(9000)
    http_server.start()
    IOLoop.current().start()
