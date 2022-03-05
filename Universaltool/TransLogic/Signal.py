from PyQt5 import QtCore, QtWidgets


class Signals():
    # 信号槽机制：设置一个信号，用于触发接收区写入动作
    signal_write_msg = QtCore.pyqtSignal(str)
    signal_write_terminal = QtCore.pyqtSignal(str)
    signal_NewClientAdded = QtCore.pyqtSignal(tuple)
    signal_NewDataComing = QtCore.pyqtSignal(str)
    signal_PackedDataComing = QtCore.pyqtSignal(bytes)
    signal_trigerthread = QtCore.pyqtSignal(int)
    def __init__(self):
        self.connect()

    def connect(self):
        self.signal_write_msg.connect(self.write_msg)
        self.signal_write_terminal.connect(self.write_terminal)
        self.signal_NewClientAdded.connect(self.NewClient)

    def NewClient(self,dp):

        return
    def write_terminal(self, msg):
    #     # signal_write_msg_ter信号会触发这个函数
        return
    #
    def write_msg(self, msg):
    #     # signal_write_msg信号会触发这个函数
        return
