from django.apps import AppConfig


class BaiduConfig(AppConfig):
    name = 'apps.baidu'



from cgi import parse_qs,escape
from wsgiref.simple_server import make_server