import Signal
import socket
import threading
import stopThreading
import time

class TcpLogic(Signal.Signals):

    def __init__(self):
        super(TcpLogic, self).__init__()
        self.tcp_socket = None
        self._mode = {"Poor_thread": 0, "Rich_thread": 1}
        self.working_mode = self._mode["Poor_thread"]
        self.tcp_client_socket_list = []
        self.current_client_index = -2
        self.tcp_port = 8080

        self.tcp_receive_thread = None
        self.tcp_listen_thread = None

        self.tcp_link = False  # 用于标记是否开启了连接
        self.tcp_ip = self.get_ip_tcp()

    # 自动获取本机IP 本功能由UDP代为执行
    def get_ip_tcp(self):
        # 获取本机ip
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM -> TCP/ GRRAM -> UDP
        my_addr = None
        try:
            s.connect(('8.8.8.8', 80))
            my_addr = s.getsockname()[0]
            # self.signal_write_terminal.emit("TCP 自动获取IP "+str(my_addr)+"\n")
        except Exception as ret:
            # 若无法连接互联网使用，会调用以下方法
            try:
                my_addr = socket.gethostbyname(socket.gethostname())
            except Exception as ret_e:
                self.signal_write_terminal.emit("TCP 无法获取ip，请连接网络！\n")
        finally:
            s.close()
        return my_addr

    def tcp_server_start(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 取消主动断开连接四次握手后的TIME_WAIT状态
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 设定套接字为非阻塞式
        self.tcp_socket.setblocking(False)
        try:
            self.tcp_socket.bind((self.tcp_ip, self.tcp_port))
        except Exception as ret:
            self.signal_write_terminal.emit('请检查端口号\n')
        else:
            self.tcp_socket.listen()
            self.tcp_listen_thread = threading.Thread(target=self.tcp_server_concurrency)
            self.tcp_listen_thread.start()
            self.signal_write_terminal.emit('TCP服务端正在监听端口:%s\n' % str(self.tcp_port))

    def tcp_recieve_run(self, sock, addr):
        while True:
            recv_msg, recv_addr = sock.recvfrom(500)
            if len(recv_msg)==22:
                self.signal_PackedDataComing.emit(recv_msg[0:20])
            else:
                msg = recv_msg.decode('utf-8')
                print("recv_msg", recv_msg)
                self.signal_write_msg.emit('from IP :{} port :{}: {}\n'.format(addr[0], addr[1], msg))
        sock.close()

    def tcp_server_concurrency(self):
        client_socket = None
        client_address = None
        while True:
            try:
                client_socket, client_address = self.tcp_socket.accept()
            except Exception as ret:
                time.sleep(0.001)
            else:
                client_socket.setblocking(self.working_mode)
                # 将创建的客户端套接字存入列表,client_address为ip和端口的元组
                self.tcp_client_socket_list.append((client_socket, client_address))
                self.signal_NewClientAdded.emit(client_address)
                self.signal_write_terminal.emit('TCP服务端已连接 : %s \n' % client_address)
                self.tcp_link = True

                if self.working_mode == self._mode["Rich_thread"]:
                    self.tcp_receive_thread[client_address] = (threading.Thread(name=client_address, target=self.tcp_recieve_run,args=(client_socket, client_address)))
                    self.tcp_receive_thread[client_address].start()

                # 轮询客户端套接字列表，接收数据
            if self.working_mode==self._mode["Poor_thread"]:
                for i in range(len(self.tcp_client_socket_list)):
                    client_socket, address = self.tcp_client_socket_list[i]
                    try:
                        recv_msg = client_socket.recv(1024)
                    except Exception as ret:
                        pass
                    else:
                        if recv_msg:
                            msg = recv_msg.decode('utf-8')
                            self.signal_PackedDataComing.emit(msg)
                            self.signal_write_msg.emit('TCP from IP :{} port:{}:\n{}\n'.format(address[0], address[1], msg))
                        else:
                            client_socket.close()
                            self.tcp_client_socket_list.remove((client_socket, address))
                            stopThreading.stop_thread(self.tcp_receive_thread["address"])
                            del self.tcp_receive_thread["address"]
                            self.signal_write_terminal.emit('断开连接:%s\n' % address)
    def tcp_send(self, sendstr):
        if self.tcp_link is False:
            self.signal_write_msg.emit('TCP 请选择服务，并点击连接网络\n')
        else:
            try:
                if self.current_client_index == -1:
                    # 向所有连接的客户端发送消息
                    for client, address in self.tcp_client_socket_list:
                        client.send(sendstr)
                    self.signal_write_terminal.emit('TCP服务端已全部发送\n')
                else:
                    client, address = self.tcp_client_socket_list[self.current_client_index]
                    client.send(sendstr)
                    self.signal_write_terminal.emit('TCP客户端已定点发送\n')
            except Exception as ret:
                self.signal_write_terminal.emit('发送失败 %d\n', self.current_client_index)

    def tcp_close(self):
        try:
            stopThreading.stop_thread(self.tcp_listen_thread)
            self.signal_write_terminal.emit('监听线程删除\n')
            if self.working_mode==self._mode["Rich_thread"]:
                for key in self.tcp_receive_thread:
                    stopThreading.stop_thread(self.tcp_receive_thread[key])
                    self.signal_write_terminal.emit('接收线程删除: %s\n' % key)

        except Exception:
            pass

        try:
            for client, address in self.tcp_client_socket_list:
                client.close()
            self.tcp_socket.close()
            if self.tcp_link is True:
                self.signal_write_terminal.emit('Clients已断开网络\n')
        except Exception as ret:
            pass

        try:
            self.tcp_socket.close()
            if self.tcp_link is True:
                self.signal_write_terminal.emit('Server已断开网络\n')
        except Exception as ret:
            pass
        self.tcp_link = False


