from socket import *
from multiprocessing import Process
import re

HOST_MAIN_PATH = "./html"


class HttpServer(object):
    """"""
    def __init__(self, port):
        # 建立TCP的socket服务端
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # 消除重启后的端口复用问题
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定端口号
        self.serverSocket.bind(("", port))

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

    def handle_socket(self, client_socket, client_addr):
        recvData = client_socket.recv(2048)
        if recvData:
            # request = str(recvData.decode("utf-8")).split("\r\n")
            # 获取用户发来的请求 GET / HTTP/1.1
            request = str(recvData.decode("utf-8")).splitlines()  # 按行进行截断
            # print(request)
            request_headline = request[0]
            # recvHead_type = re.match(r"\w+ +(/[^ ]*) ", request_headline).group(0)
            recvHead_path = re.match(r"\w+ +(/[^ ]*) ", request_headline).group(1)
            # recvHead_propr = re.match(r"\w+ +(/[^ ]*) ", request_headline).group(2)
            # recvHead = request[0]
            # recvHead_type = recvHead.split( )[0]
            # recvHead_path = recvHead.split( )[1]
            # recvHead_propr = recvHead.split( )[2]
            # print(recvHead_path)
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
            finally:
                print("客户端-%s已经退出" % str(client_addr))
                client_socket.close()

                # socket.send(sendData) 确保浏览器可以进行渲染，所以要以http的格式发送
        else:
            print("客户端-%s已经退出" % str(client_addr))
            client_socket.close()


def main():
    http_server = HttpServer(7788)
    http_server.accept_info()


if __name__=="__main__":
    main()