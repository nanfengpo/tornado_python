#coding:utf8

'''
    通用handler基类
'''

import tornado.web
import uuid
import os

from datetime import datetime # 根据日期来创建文件夹

base_dir = os.path.abspath(os.path.dirname(__file__))

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def make_dir(self,dname):  # 在upload目录下面创建一个名为dname的子目录
        dirname = os.path.join(base_dir,'upload/' + dname)
        if not os.path.exists(dirname): #文件夹不存在
            os.makedirs(dirname)
        return dirname

    def upload_file(self,files):
        for file in files:
            content_type = file.get('content_type',None) # 获取文件类型
            if not (content_type == 'image/jpeg' or content_type == 'image/png'):
                message = '文件类型不正确'
            else:
                # 获得根据当前日期命名的目录
                dirname = self.make_dir(datetime.strftime(datetime.now(),'%Y-%m'))
                filename = file.get('filename',None)  # 获取文件名
                body = file.get('body','')

                # 拼接文件的绝对路径和文件名
                # 文件名的前缀为uuid加密，后缀为文件格式
                fname = dirname +  '/' + str(uuid.uuid4()) + '.' + filename.split('.')[-1]
                with open(fname,'w+') as f:
                    f.write(body)
            message = 'upload ok'
        return message


