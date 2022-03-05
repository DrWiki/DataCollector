import WinLayout
import sys
import time
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import pyqtgraph as pg
import torch
from scipy.signal import butter, lfilter, freqz
import torch.nn.functional as F

class WinLogic(WinLayout.WinLayout):
    def __init__(self, parent=None):
        super(WinLogic, self).__init__(parent)
        self.CONNECT()
        self.th0 = threading.Thread(target=self.update0)
        self.th1 = threading.Thread(target=self.update1)
        self.CNN1D = None
        self.Loadnet()

    def butter_lowpass(self, cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    def butter_lowpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.butter_lowpass(cutoff, fs, order=order)
        y = lfilter(b, a, data)
        return y  # Filter requirements.

    def lowpass(self, data):
        return self.butter_lowpass_filter(data, 50, 200, order=5)

    def Loadnet(self):
        self.CNN1D = torch.load("./res/models/100GAS4.pth", map_location=torch.device('cpu'))
        print(self.CNN1D)

    def predict(self, li):
        li = li.reshape((1,1,1400))
        li = li.astype(np.float32)
        output = self.CNN1D(torch.from_numpy(li))

        temp = li
        for i in range(16):
            temp = np.concatenate((temp,li), axis=0)
        output = self.CNN1D(torch.from_numpy(temp))

        ans = F.log_softmax(output, dim=1).argmax(dim=1).detach().numpy()[0]
        return

    def CONNECT(self):
        # self.MyCB.signal_NewDataComing.connect(self.ProcessData)
        self.MyCB.signal_trigerthread.connect(self.triger)

    def triger(self, flag):
        if flag==1:
            self.th0.start()
            self.th1.start()

        if flag==4:
            self.th0.start()
            self.th1.start()

    def update0(self):
        tt = []
        t = 0
        while 1:
            if self.MyCB.metadata.datareadyX == True:
                self.MyCB.metadata.datareadyX = False
                tt.append(t)
                if t>1400:
                    self.PWPlot1Ploterlist[0].setData(np.array(tt[-1401:-1]),
                                                       np.array(self.MyCB.metadata.DataStreamX[-1401:-1]))
                elif t>3:
                    self.PWPlot1Ploterlist[0].setData(np.array(tt[0:t]),
                                                      np.array(self.MyCB.metadata.DataStreamX[0:t]))
                t += 1
            while not self.MyCB.metadata.datareadyX:
                pg.QtGui.QApplication.processEvents()

    def update1(self):
        tt = []
        t = 0
        while 1:
            if self.MyCB.metadata.datareadyY == True:
                self.MyCB.metadata.datareadyY = False
                tt.append(t)
                if t>1400:
                    self.PWPlot1Ploterlist[1].setData(np.array(tt[-1401:-1]),
                                                      np.array(self.MyCB.metadata.DataStreamY[-1401:-1]))
                elif t>3:
                    self.PWPlot1Ploterlist[1].setData(np.array(tt[0:t]),
                                                      np.array(self.MyCB.metadata.DataStreamY[0:t]))
                t += 1
            while not self.MyCB.metadata.datareadyY:
                pg.QtGui.QApplication.processEvents()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setAttribute(QtCore.Qt.AA_Use96Dpi)
    mainWindow = WinLogic()
    mainWindow.show()
    sys.exit(app.exec_())
