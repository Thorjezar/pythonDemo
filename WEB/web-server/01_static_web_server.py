"""
1.HTTP的静态服务端网站
2.建立TCP的服务端
3.HTTP的报文格式接受和返回
requeset响应头：
GET / HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
Cache-Control: max-age=0
DNT: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: BIDUPSID=0D0894D8E9F710E618512C0414261EBB;
PSTM=1607907921; BAIDUID=D0F0EDA993045750D10DB7BCC19B26A4:FG=1;
BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;
 BAIDUID_BFESS=D0F0EDA993045750D10DB7BCC19B26A4:FG=1;
 H_PS_645EC=f4ffsNMetqriBDfbGq9pIdEUJQ%2Bx%2BtoHuVNfaRu%2BrrYse%2Be2DdBGSkPFTWI; BD_HOME=1;
 H_PS_PSSID=1444_33222_33061_33256_31254_33099_33100_32846_33199_22158; BA_HECTOR=810h0l25818k240ls21fte2dg0q

 respones响应头:
 GET / HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
Cache-Control: max-age=0
DNT: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: BIDUPSID=0D0894D8E9F710E618512C0414261EBB;
PSTM=1607907921; BAIDUID=D0F0EDA993045750D10DB7BCC19B26A4:FG=1;
BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;
BAIDUID_BFESS=D0F0EDA993045750D10DB7BCC19B26A4:FG=1;
H_PS_645EC=f4ffsNMetqriBDfbGq9pIdEUJQ%2Bx%2BtoHuVNfaRu%2BrrYse%2Be2DdBGSkPFTWI; BD_HOME=1;
 H_PS_PSSID=1444_33222_33061_33256_31254_33099_33100_32846_33199_22158; BA_HECTOR=810h0l25818k240ls21fte2dg0q
\r\n
响应体
"""
from socket import *
from multiprocessing import Process
import re

HOST_MAIN_PATH = "./html"

# 处理客户端请求的函数
def handle_sock(socket, addr):
    recvData = socket.recv(2048)
    if recvData:
        # request = str(recvData.decode("utf-8")).split("\r\n")
        # 获取用户发来的请求 GET / HTTP/1.1
        request = str(recvData.decode("utf-8")).splitlines()  # 按行进行截断
        # print(request)
        request_headline = request[0]
        #recvHead_type = re.match(r"\w+ +(/[^ ]*) ", request_headline).group(0)
        recvHead_path = re.match(r"\w+ +(/[^ ]*) ", request_headline).group(1)
        # recvHead_propr = re.match(r"\w+ +(/[^ ]*) ", request_headline).group(2)
        # recvHead = request[0]
        # recvHead_type = recvHead.split( )[0]
        # recvHead_path = recvHead.split( )[1]
        # recvHead_propr = recvHead.split( )[2]
        # print(recvHead_path)
        try:
            #if recvHead_type == "GET":
            # print("准备传输html文档")
            f = open(HOST_MAIN_PATH+recvHead_path+"index.html", "rb")
            send_data = f.read()
            # print(send_data)
            response_data = "HTTP/1.1 200 OK\r\nServer: MyServer\r\n\r\n" + send_data.decode("utf-8")
            # print(response_data.encode("utf-8"))
            f.close()
            # socket.send(response_data.encode("utf-8"))
            socket.send(bytes(response_data, "utf-8"))
        except Exception as ex:
            error_data = "HTTP/1.1 404 Not Found\r\nNot Found\r\nError: 404!!\r\n\r\n<p>error</p>"
            print(ex)
            socket.send(error_data.encode("utf-8"))
        finally:
            print("客户端-%s已经退出" % str(addr))
            socket.close()

            # socket.send(sendData) 确保浏览器可以进行渲染，所以要以http的格式发送
    else:
        print("客户端-%s已经退出" % str(addr))
        socket.close()

def main():
    # 建立TCP的socket服务端
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 消除重启后的端口复用问题
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定地址
    addrs = ("", 7788)
    serverSocket.bind(addrs)
    # 被动套接字
    serverSocket.listen(5)
    while 1:
        print("----等待新的客户端接入----")
        client_socket, client_addr = serverSocket.accept()
        print("----新客户端接入-%s---" % str(client_addr))
        p = Process(target=handle_sock, args=(client_socket, client_addr, ))
        p.start()
        # 主进程关闭客户端
        client_socket.close()

if __name__=="__main__":
    main()