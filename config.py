# coding:utf8
import os

# Mysql配置
mysql_options = {
    'host':'127.0.0.1',
    'database':'tornado',
    'user':'root',
    'password':'abc123!@#',
}

# App配置
settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'html'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'debug':True,
}
