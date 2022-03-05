import ParentUI.RAL as UI
import Universaltool.Control.ControlBoxTab as Control
import sys
import pyqtgraph as pg
import PyQt5
import socket

from PyQt5 import QtCore, QtGui, QtWidgets

class WinLayout(UI.Ui_MainWindow,QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(WinLayout, self).__init__(parent)
        self.setupUi(self)
        self.MyCB = Control.ControlBoxTab(self.ControlW)
        self.MyCB.RBTSerial.setChecked(True)
        ###
        # 画布1
        pg.setConfigOptions(leftButtonPan=True)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.LBlist = [self.LB1,self.LB2]
        self.VLlist = []
        self.PWlist = [pg.PlotWidget(self.centralwidget),pg.PlotWidget(self.centralwidget)]

        self.PWPlot1Ploterlist = []
        self.PWPlot1PloterlistS = []
        for i in range(self.LBlist.__len__()):
            self.VLlist.append(QtWidgets.QVBoxLayout(self.LBlist[i]))
            self.VLlist[i].addWidget(self.PWlist[i])
            self.PWlist[i].addLegend()
            self.PWlist[i].setAntialiasing(False)
            self.PWlist[i].setYRange(0, 4096)
            # self.plotWidget1.setLabel('left', 'Value', units='V')
            # self.PWPlot1.setLabel('left', 'G')
            # self.PWlist[i].setLabel('bottom', 'Time')
            self.PWPlot1Ploterlist.append(self.PWlist[i].plot(name='DataStream', pen=pg.mkPen(width=3, color='b')))
            # self.PWPlot1PloterlistS.append(self.PWlist[i].plot(name='DataStream', pen=pg.mkPen(width=3, color='r')))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = WinLayout()
    mainWindow.show()
    sys.exit(app.exec_())
