"""

核心功能
1.连接到tftp服务器，端口号默认69
2.根据连接上的情况，去请求服务端下载文件
3.遵循tftp协议格式
4.从客户端上传一个文件到服务端

# 文档下载的步骤
1.在本地创建一个同名文件 f = open(xxx,'bw')
2.从服务端读取数据 标致位2
3.写入这个文件
4.关闭文件 f.close()

# 上传文档步骤
1.在服务端创建一个同名文件 f = open(xxx, '')
2.从客户端读取数据 标致位1
3.写入文件
4.关闭保存 f.close()
上传文件注意 服务端的随机端口
"""
from socket import *
from threading import Thread
from threading import Lock
import struct
import sys
import os

# 定义全局变量

lock1 = Lock()
lock2 = Lock()
lock2.acquire()  # 下载锁
lock3 = Lock()
lock3.acquire()  # 上传锁
trans_tuple = ()


# 定义线程子类
class MyThread(Thread):
    def __init__(self, udpsocket, ipaddr, iport, localport):
        self.ipaddr = ipaddr
        self.iport = iport
        self.localport = localport
        self.udpsocket = udpsocket

    # 上传功能
    def upload(self, num, filename):
        global trans_tuple
        block_num = num
        block_num += 1
        if lock3.acquire():
            f = open(filename, 'rb')
            while True:
                content = f.read(512)
                contentLen = len(content)
                tran_buf = struct.pack("!HH", 3, block_num) + content
                # tran_addr = (self.ipaddr, self.iport)
                # print(tran_addr)
                self.udpsocket.sendto(tran_buf, trans_tuple)
                recvDatas, recvAddrs = self.udpsocket.recvfrom(1024)
                cmdTuple = struct.unpack("!HH", recvDatas[:4])
                cmd = cmdTuple[0]  # 返回ack码
                recv_block_num = cmdTuple[1]  # 返回的是块编号

                trans_tuple = recvAddrs

                if cmd == 4:
                    if recv_block_num == block_num:
                        print('(%d)次上传到服务器' % block_num)
                        if contentLen < 512:
                            print('已上传完成')
                            lock1.release()
                            f.close()
                            break

                        block_num += 1
                if cmd == 5:
                    print("错误信息%s" % recvDatas)
                    f.close()
                    lock1.release()
                    break

    # 下载功能
    def download(self, result, filename):
        os.chdir('./download/')
        block_num = 1
        recv1, addr1 = result
        if lock2.acquire():
            f = open(filename, 'wb')
            f.write(recv1[4:])  # 头一次的写入要从传递进来的参数取
            print('(%d)次收到的数据' % block_num)
            ack_buf = struct.pack("!HH", 4, block_num)
            self.udpsocket.sendto(ack_buf, addr1)
            block_num += 1
            while True:
                recvData, recvAddr = self.udpsocket.recvfrom(1024)
                recvDataLen = len(recvData)
                cmdTuple = struct.unpack("!HH", recvData[:4])
                cmd = cmdTuple[0]  # 返回的是操作码
                recv_block_num = cmdTuple[1]  # 返回的是块的编号

                if cmd == 3:
                    if recv_block_num == block_num:
                        f.write(recvData[4:])
                        print('(%d)次收到的数据' % block_num)

                        ack_buf = struct.pack("!HH", 4, block_num)
                        self.udpsocket.sendto(ack_buf, addr1)
                        block_num += 1

                    if recvDataLen < 516:
                        f.close()
                        print('已经成功下载')
                        os.chdir('../')
                        lock1.release()  # 锁一解锁
                        break

                if cmd == 5:
                    print("错误块num=%d" % recv_block_num)
                    f.close()
                    lock1.release()
                    break

    # 读写请求与服务端判断
    def sendMessage(self, flag, filename, lock1):
        name_len = str(len(filename))
        bfilename = bytes(filename.encode('gb2312'))
        global trans_tuple
        tran_buf = struct.pack("!H" + name_len + "sb5sb", flag, bfilename, 0, b"octet", 0)
        tran_addr = (self.ipaddr, self.iport)
        if lock1.acquire():
            self.udpsocket.sendto(tran_buf, tran_addr)
            recvInfo = self.udpsocket.recvfrom(1024)
            result = struct.unpack("!HH", recvInfo[0][:4])
            if result[0] == 5:
                print("差错码num=%d" % result[1])
                lock1.release()
                return None
            elif result[0] == 3:  # 下载
                lock2.release()
                return recvInfo  # 返回一个元组
            elif result[0] == 4:  # 上传
                lock3.release()
                # self.upload(result[1], filename)
                trans_tuple = recvInfo[1]
                return result[1]  # 返回的是0编号


# 主线程
def main():
    UdpSocket = socket(AF_INET, SOCK_DGRAM)  # 创建网络套接字udp
    ipaddr = input('请输入服务端的ip：')  # 配置服务端
    iport = int(input('请输入服务端的端口：'))

    localport = int(input('请输入本机启用端口:'))
    try:
        UdpSocket.bind(("", localport))  # 本地端口绑定
    except Exception as ex:
        print(ex)

    t0 = MyThread(UdpSocket, ipaddr, iport, localport)
    t1 = MyThread(UdpSocket, ipaddr, iport, localport)
    t2 = MyThread(UdpSocket, ipaddr, iport, localport)
    os.chdir('./')
    if not os.path.exists('download/'):
        os.mkdir('download')

    # print(os.getcwd())

    while True:
        cmd = input('请输入操作方式(上传/下载):')
        if cmd == "上传":
            flag_num = 2  # 2是上传操作码
        elif cmd == "下载":
            flag_num = 1  # 1是下载操作码
        elif cmd == "0":
            print("关闭程序!")
            break
            sys.exit()
        else:
            print("输入错误!")
            continue

        filename_info = input('请输入操作文件名：')
        if flag_num == 2 and filename_info not in os.listdir('./'):
            print("没有找到这个文件")
            continue

        sendResult = t0.sendMessage(flag_num, filename_info, lock1)  # 发送请求
        if sendResult == None:
            continue
        if flag_num == 1:
            t1.download(sendResult, filename_info)
        if flag_num == 2:
            t2.upload(sendResult, filename_info)


if __name__ == "__main__":
    main()
