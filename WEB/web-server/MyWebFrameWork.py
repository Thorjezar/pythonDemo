"""

服务器端的通用适配网站框架
利用WSGI协议来实现

app = Application(urls) # 初始化使用__init__
Http_Server = HttpServer(app) # app() 调用要使用__call__
Http_Server.bind(8000)
Http_Server.start()

"""
import time
# from MyWebServer import HttpServer

HOST_MAIN_ROOT = "./html"


class Application(object):
    """通用网站框架核心部分"""
    def __init__(self, urls):
        # 初始化的路由 以列表和元组的方式传递[()]
        self.urls = urls

    def __call__(self, env, start_response):
        # 字典使用get方法，如果键值不存在，程序不会崩溃，第二个参数是给缺省值 /
        path = env.get("PATH_INFO", "/")
        # /static/xxx.html 是静态网页的默认路径,静态文件必须以static开头
        if path.startswith("/static"):
            file_name = path[7:]
            try:
                f = open(HOST_MAIN_ROOT + file_name, "rb")
            except Exception as ex:
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "404 Not Found"
            else:
                send_data = f.read()
                f.close()
                status = "200 OK"
                headers = []
                start_response(status, headers)
                return send_data.decode("utf-8")

        for url, handler in self.urls:
            # url = ("/ctime", show_ctime)
            if path == url:
                # self.handler返回的是响应体 response_body
                return handler(env, start_response)
        # 未找到路由信息，错误404
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "404 Not Found"


def show_ctime(env, start_response):
    env = env
    # print(env)
    status = "200 OK"
    content = [
        ("Content-Type", "text/html")
    ]
    start_response(status, content)
    return time.ctime()


def say_hello(env, start_response):
    env = env
    status = "200 OK"
    content = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, content)
    return "use python programe"


def say_haha(env, start_response):
    env = env
    status = "200 OK"
    content = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, content)
    return "say ha~"


# 定义路由
urls = [
        ("/ctime", show_ctime),
        ("/hello", say_hello),
        ("/haha", say_haha)

    ]

# 创建框架的对象
app = Application(urls)
# if __name__=="__main__":
#     # 将对象传入到httpserver 中去
#     http_server = HttpServer(app)
#     http_server.accept_info()

