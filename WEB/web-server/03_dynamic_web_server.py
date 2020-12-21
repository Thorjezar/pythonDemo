from socket import *
from multiprocessing import Process
import re
import sys

HOST_MAIN_PATH = "./html"

WSGI_MAIN_PATH = "./wsgipython"


class HttpServer(object):
    """"""
    def __init__(self, port):
        # 建立TCP的socket服务端
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # 消除重启后的端口复用问题
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定端口号
        self.serverSocket.bind(("", port))
        # 接收py程序返回的http报文头
        self.response_header = None

    def accept_info(self):
        # 被动套接字
        self.serverSocket.listen(5)
        while True:
            print("----等待新的客户端接入----")
            client_socket, client_addr = self.serverSocket.accept()
            print("----新客户端接入-%s---" % str(client_addr))
            p = Process(target=self.handle_socket, args=(client_socket, client_addr,))
            p.start()
            # 主进程关闭客户端
            client_socket.close()

    def start_response(self, status, handers):
        server_header = [
            ("Server", "My Server")
        ]  #  服务端返回的报文可以在py程序中添加
        response_handle = server_header + handers
        self.response_header = "HTTP/1.1" + " " + status + "\r\n"  # 格式HTTP/1.1 200 OK 注意空格和换行
        # print(self.response_header)
        for hands in response_handle:
            self.response_header += "%s : %s\r\n" % hands

    def handle_socket(self, client_socket, client_addr):
        recvData = client_socket.recv(2048)
        if recvData:
            # request = str(recvData.decode("utf-8")).split("\r\n")
            # 获取用户发来的请求
            request = str(recvData.decode("utf-8")).splitlines()  # 按行进行截断
            request_headline = request[0]  # 截取到第一行 GET / HTTP/1.1
            recvHead_path = re.match(r"\w+ +(/[^ ]*) ", request_headline).group(1)  # 正则提取请求路径
            method = re.match(r"(\w)+ +/[^ ]* ", request_headline).group(1)
            if recvHead_path.endswith(".py"):  # 判断请求的是否是一个py程序，动态的执行网页
                try:
                    m = __import__(recvHead_path[1:-3])  # 魔法函数 __import__() 相当于import如果是一个py程序那就截取出包名 例如/time.py 取出time
                except Exception as ex:
                    self.response_header = "HTTP/1.1 404 Not Found\r\n"
                    response_body = "Not Found This file" + "\n" + str(ex)
                    print(ex)
                else:
                    env = {
                        "PATH_INFO": recvHead_path,
                        "METHOD": method

                    }  # 客户端发送请求时，得到的客户端浏览器的一些环境信息
                    response_body = m.application(env, self.start_response)  # 进行WSGI方法的调用，返回的是HTTP报文体

                response_ht = self.response_header+"\r\n"+response_body  # 拼接HTTP报文
                print(response_ht)
                client_socket.send(bytes(response_ht, "utf-8"))  # 服务端返回HTTP 响应

            if "/" == recvHead_path:   # 这里面读取的静态网页
                try:
                    # if recvHead_type == "GET":
                    # print("准备传输html文档")
                    f = open(HOST_MAIN_PATH + recvHead_path + "index.html", "rb")
                    send_data = f.read()
                    # print(send_data)
                    response_data = "HTTP/1.1 200 OK\r\nServer: MyServer\r\n\r\n" + send_data.decode("utf-8")
                    # print(response_data.encode("utf-8"))
                    f.close()
                    # socket.send(response_data.encode("utf-8"))
                    client_socket.send(bytes(response_data, "utf-8"))
                except Exception as ex:
                    error_data = "HTTP/1.1 404 Not Found\r\nNot Found\r\nError: 404!!\r\n\r\n<p>error</p>"
                    print(ex)
                    client_socket.send(error_data.encode("utf-8"))

            else:
                print("客户端-%s已经退出" % str(client_addr))
                client_socket.close()


def main():
    sys.path.insert(1, WSGI_MAIN_PATH)  # 补充导入包的目录
    http_server = HttpServer(7788)
    http_server.accept_info()


if __name__=="__main__":
    main()