什么是WSGI

WSGI的全称是Web Server Gateway Interface，这是一个规范，
描述了web server如何与web application交互、web application如何处理请求。
该规范的具体描述在PEP 3333。注意，WSGI既要实现web server，也要实现web application。


WSGI application结构：

def application(environ,start_response):
   response_body = 'Request method:%s' % environ['REQUEST_METHOD']
    
    # http响应状态
   status = '200 ok'
    
    # http响应头，注意格式
   response_headers = [
        ('Content-Type','text/plain'),
        ('Content-Length',str(len(response_body)))
    ]
    
    #将响应状态和响应头交给WSGI server
   start_response = (status,response_headers)
    
    #返回响应正文
   return [response_body]