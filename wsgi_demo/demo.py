# 将environment字典的内容返回给客户端

from wsgiref.simple_server import make_server


def application(environ,start_response):
    response_body = [
        '%s: %s' % (key,value) for key,value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 ok'
    response_header = [
        ('Content_Type','text/plain'),
        ('Content_Length',str(len(response_body)))
    ]
    start_response(status,response_header)

    return [response_body]


# 实例化WSGI server
httpd = make_server('127.0.0.1',8051,application)
httpd.handle_request()
print('end...')
