import threading
import ControlTab
import sys
import pandas as pd
import Universaltool.TransLogic.udp_logic as UDP
import Universaltool.TransLogic.Serial_logic as SER
import Universaltool.TransLogic.tcp_logic as TCP
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import Metadata
import struct
import pyqtgraph as pg
import Universaltool.TransLogic.stopThreading as THREAD

class ControlBoxTab(ControlTab.Ui_Form, QtWidgets.QWidget, UDP.UdpLogic, TCP.TcpLogic, SER.PyQt_Serial):
    def __init__(self, parent=None, ):
        super(ControlBoxTab,self).__init__(parent)
        self.setupUi(self)
        self.metadata = Metadata.metadata(5)
        if parent == None:
            self.resize(720, 1080)

        # 自动填充文字
        self.on_refreshCom()
        self.SBUDP.setValue(8090)
        self.SBTCPServer.setValue(8090)
        self.LETCPServer.setText(str(self.IP))
        self.LEUDP.setText(str(self.IP))

        #
        self.CONNECT()
        self.signal_write_terminal.emit(self.IP+'\n')

    def CONNECT(self):
        self.BTFilePath.clicked.connect(self.ChooseFile)
        self.PBSend.clicked.connect(self.Send)
        self.PBStop.clicked.connect(self.Disconnect)
        self.PBStart.clicked.connect(self.Connect)
        self.signal_PackedDataComing.connect(self.Datasplit)
        self.TAB.currentChanged.connect(self.Management)


    def write_msg(self, msg):
        self.TERceive.insertPlainText(msg+"\n") # 这个地方的坑在于继承类的加载顺序
        self.TERceive.moveCursor(QtGui.QTextCursor.End)

    def write_terminal(self, msg):
        self.TEcmd.insertPlainText(msg+"\n")
        # 滚动条移动到结尾
        self.TEcmd.moveCursor(QtGui.QTextCursor.End)

    def add_new_Client(self, tupleinfo):
        self.CBTCP2.addItem(tupleinfo[0] + ":" + str(tupleinfo[1]))

    def ChooseFile(self):
        files = QtWidgets.QFileDialog.getOpenFileNames(self, "CSV选择", "../res/data", "All Files (*)")[0]
        filecsv = pd.read_csv(files[0], sep=',')

        self.LEFilePath.setText(files[0])

    def on_refreshCom(self):
        self.CBSerial.clear()
        com = QSerialPort()
        for info in QSerialPortInfo.availablePorts():
            com.setPort(info)
            if com.open(QSerialPort.ReadWrite):
                self.CBSerial.addItem(info.portName())
                com.close()

    def Send(self):
        ans = self.TAB.currentIndex()
        if ans==0:
            self.udp_ip2 = self.LEUDP2.text()
            self.udp_port2 = self.SBUDP2.value()

        elif ans==1:
            self.CurrentClient = 0

        elif ans==2:
            pass

    def Connect(self):
        ans = self.TAB.currentIndex()
        if ans==0:
            self.udp_port1 = self.SBUDP.value()
            self.udp_server_start()
            self.signal_trigerthread.emit(1)
        elif ans==1:
            self.tcp_port1 = self.SBTCPServer.value()
            self.tcp_server_start()
        elif ans==2:
            self.ser_NAME = self.CBSerial.currentText()
            self.on_openSerial()
        elif ans==3:
            self.NewTimerX.start()
            self.NewTimerY.start()
            self.signal_trigerthread.emit(4)

    def Disconnect(self):
        ans = self.TAB.currentIndex()
        if ans==0:
            self.udp_close()
            self.metadata.save("./pb2.csv")
        elif ans ==1:
            self.tcp_close()
            self.metadata.save("./pb2.csv")
        elif ans==2:
            self.on_closeSerial()
            self.metadata.save("./pb2.csv")
        elif ans==3:
            THREAD.stop_thread(self.NewTimerX)
            THREAD.stop_thread(self.NewTimerY)
            self.metadata.save("./data.csv")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = ControlBoxTab()
    mainWindow.show()
    sys.exit(app.exec_())


    # def SendTest(self):
    #     num = int(self.LECheatBox.text())
    #     print(num)
    #     if num < 16:
    #         self.udp_socket.sendto(binascii.a2b_hex(hex(num).replace('0x', '0')),
    #                                ("192.168.43.167", 9999))
    #     else:
    #         self.udp_socket.sendto(binascii.a2b_hex(hex(num).replace('0x', '')),
    #                                ("192.168.43.167", 9999))
    #     print("!!!!!!!!!!!!!!!!!")