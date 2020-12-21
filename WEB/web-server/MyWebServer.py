"""

通用型的网站服务端
利用WSGI协议来实现

利用命令行来启动server
python3 MyWebServer.py module_name:app

可以使用不同框架，来配合使用

"""
from socket import *
from multiprocessing import Process
import re
import sys

HOST_MAIN_ROOT = "./html"

WSGI_MAIN_ROOT = "./wsgipython"


class HttpServer(object):
    # 初始化一个服务器网络套接字
    def __init__(self, application):
        # 接受application 这个是框架中的app
        self.app = application
        # 定义TCP网络套接字
        self.socket = socket(AF_INET, SOCK_STREAM)
        # 绑定网络地址
        self.socket.bind(("", 7789))  # 给出默认的端口
        # 取消重复使用端口的问题
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 添加响应报文头, WSGI使用
        self.response_header = None
        # 添加响应报文体
        self.response_body = None

    def accept_info(self):
        # 变为被动套接字
        self.socket.listen(5)
        while True:
            print("-"*4 + "等待新客户端接入" + "-"*4)
            clientsocket, clientaddrs = self.socket.accept()
            print("-"*4 + "新客户端接入%s--" % str(clientaddrs))
            # 新建进程去执行请求的响应
            p = Process(target=self.handle_info, args=(clientsocket, clientaddrs, ))
            p.start()
            # 主进程关闭客户端套接字
            clientsocket.close()

    # 这里处理的是响应的报文头，
    def start_response(self, status, headers):
        server_header = [
            ("Server", "My server")
        ]
        response_handle = server_header + headers
        # 拼接报文响应头 HTTP/1.1 200 OK
        self.response_header = "HTTP/1.1" + " " + status + "\r\n"
        for handle in response_handle:
            self.response_header += "%s : %s\r\n" % handle

    def handle_info(self, client_socket, addres):
        recvData = client_socket.recv(1024)
        if recvData:
            request = str(recvData.decode("utf-8")).splitlines() # 按行进行截取
            request_header = request[0] # 截取到第一行 GET / HTTP/1.1
            recvhead_path = re.match(r"\w+ +(/[^ ]*) ", request_header).group(1)
            method = re.match(r"(\w)+ +/[^ ]* ", request_header).group(1)
            env = {
                "PATH_INFO": recvhead_path,
                "METHOD": method
            }
            self.response_body = self.app(env, self.start_response)
            # 拼接HTTP报文
            response_info = self.response_header + "\r\n" + self.response_body
            client_socket.send(bytes(response_info, "utf-8"))
            # 关闭客户端套接字
            client_socket.close()


def main():
    # 补充导入包的目录
    sys.path.insert(1, WSGI_MAIN_ROOT)
    if len(sys.argv) < 2:  # 如果小于2代表只有一个参数
        sys.exit("python3 MyWebServer.py module_name:app")  # 退出应用时会发送此消息
    else:
        # python3 MyWebServer.py MyWebFrameWork:Application替换成app
        # module_name = "MyWebFrameWork"
        # app_name = "Application"替换成app
        module_name, app_name = sys.argv[1].split(":")
        # 动态导入包
        m = __import__(module_name)
        # 利用getattr(m, "属性名")来获取包中的类名
        # Application = getattr(m, app_name)
        app = getattr(m, app_name)
        # app = Application()
    # 创建服务端的对象实例
    http_server = HttpServer(app)
    http_server.accept_info()


if __name__ == "__main__":
    main() 