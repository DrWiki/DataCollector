import Signal
import stopThreading
import socket
import threading
import struct
class UdpLogic(Signal.Signals):
    def __init__(self):
        super(UdpLogic, self).__init__()
        self.udp_socket = None
        self.udp_recieve_thread = None
        self.udp_port = 0
        self.link = False
        self.IP = self.get_ip()
        self.udp_ip = self.IP

        self.udp_target_ip = "0.0.0.0"
        self.udp_target_port = 0

    # 自动获取本机IP
    def get_ip(self):
        # 获取本机ip
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        my_addr = None
        try:
            s.connect(('8.8.8.8', 80))
            my_addr = s.getsockname()[0]
            # self.signal_write_terminal.emit("UDP 自动获取IP " + str(my_addr) + "\n")
        except Exception as ret:
            # 若无法连接互联网使用，会调用以下方法
            try:
                my_addr = socket.gethostbyname(socket.gethostname())
            except Exception as ret_e:
                self.signal_write_terminal.emit("TCP 无法获取ip，请连接网络！")
        finally:
            s.close()
        return my_addr

    def udp_server_start(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            address = ('', self.udp_port)
            self.udp_socket.bind(address)
            self.link = True
        except Exception as ret:
            self.signal_write_terminal.emit('请检查端口号\n')
        else:
            self.udp_recieve_thread = threading.Thread(target=self.udp_recieve)
            self.udp_recieve_thread.start()
            self.signal_write_terminal.emit('UDP服务端正在监听端口:{}\n'.format(self.udp_port))

    def udp_recieve(self):
        while True:
            recv_msg, recv_addr = self.udp_socket.recvfrom(500)
            if len(recv_msg)==22:
                self.signal_PackedDataComing.emit(recv_msg[0:20])
            else:
                msg = recv_msg.decode('utf-8')
                print("recv_msg", recv_msg)
                self.signal_write_msg.emit('from IP :{} port :{}: {}\n'.format(recv_addr[0], recv_addr[1], msg))

    def udp_send(self, send_msg):
        if self.link is False:
            self.signal_write_terminal.emit('UDP 请选择服务，并点击连接网络\n')
        else:
            try:
                # send_msg = sendstr.encode('utf-8')
                self.udp_socket.sendto(send_msg, (self.udp_target_ip, self.udp_target_port))
                self.signal_write_terminal.emit('UDP客户端已发送\n')
            except Exception as ret:
                self.signal_write_terminal.emit('发送失败\n')

    def udp_close(self):
        try:
            stopThreading.stop_thread(self.udp_recieve_thread)
            self.signal_write_terminal.emit('接收线程删除\n')
        except Exception:
            pass

        try:
            self.udp_socket.close()
            if self.link is True:
                self.signal_write_terminal.emit('已断开网络\n')
        except Exception as ret:
            pass
        self.link = False
