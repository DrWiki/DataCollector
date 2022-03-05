# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlTab.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(345, 775)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.TAB = QtWidgets.QTabWidget(Form)
        self.TAB.setTabPosition(QtWidgets.QTabWidget.North)
        self.TAB.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.TAB.setElideMode(QtCore.Qt.ElideLeft)
        self.TAB.setUsesScrollButtons(True)
        self.TAB.setDocumentMode(False)
        self.TAB.setTabsClosable(False)
        self.TAB.setMovable(False)
        self.TAB.setTabBarAutoHide(False)
        self.TAB.setObjectName("TAB")
        self.TABUDP = QtWidgets.QWidget()
        self.TABUDP.setObjectName("TABUDP")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.TABUDP)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LEUDP = QtWidgets.QLineEdit(self.TABUDP)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LEUDP.setFont(font)
        self.LEUDP.setObjectName("LEUDP")
        self.verticalLayout_2.addWidget(self.LEUDP)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SBUDP = QtWidgets.QSpinBox(self.TABUDP)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SBUDP.setFont(font)
        self.SBUDP.setMaximum(65535)
        self.SBUDP.setProperty("value", 1122)
        self.SBUDP.setObjectName("SBUDP")
        self.horizontalLayout.addWidget(self.SBUDP)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.CBUDPHEXR = QtWidgets.QCheckBox(self.TABUDP)
        self.CBUDPHEXR.setMaximumSize(QtCore.QSize(16777215, 20))
        self.CBUDPHEXR.setObjectName("CBUDPHEXR")
        self.verticalLayout.addWidget(self.CBUDPHEXR)
        self.CBUDPHEXT = QtWidgets.QCheckBox(self.TABUDP)
        self.CBUDPHEXT.setMaximumSize(QtCore.QSize(16777215, 20))
        self.CBUDPHEXT.setObjectName("CBUDPHEXT")
        self.verticalLayout.addWidget(self.CBUDPHEXT)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 78, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.LEUDP2 = QtWidgets.QLineEdit(self.TABUDP)
        self.LEUDP2.setMinimumSize(QtCore.QSize(100, 0))
        self.LEUDP2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LEUDP2.setFont(font)
        self.LEUDP2.setObjectName("LEUDP2")
        self.horizontalLayout_14.addWidget(self.LEUDP2)
        self.SBUDP2 = QtWidgets.QSpinBox(self.TABUDP)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SBUDP2.setFont(font)
        self.SBUDP2.setMaximum(65535)
        self.SBUDP2.setProperty("value", 1122)
        self.SBUDP2.setObjectName("SBUDP2")
        self.horizontalLayout_14.addWidget(self.SBUDP2)
        self.horizontalLayout_14.setStretch(0, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/24gf-network2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TAB.addTab(self.TABUDP, icon, "")
        self.TABTCP = QtWidgets.QWidget()
        self.TABTCP.setObjectName("TABTCP")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.TABTCP)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.LETCPServer = QtWidgets.QLineEdit(self.TABTCP)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LETCPServer.setFont(font)
        self.LETCPServer.setObjectName("LETCPServer")
        self.verticalLayout_5.addWidget(self.LETCPServer)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SBTCPServer = QtWidgets.QSpinBox(self.TABTCP)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SBTCPServer.setFont(font)
        self.SBTCPServer.setMaximum(65535)
        self.SBTCPServer.setProperty("value", 8080)
        self.SBTCPServer.setObjectName("SBTCPServer")
        self.horizontalLayout_3.addWidget(self.SBTCPServer)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.CBTCPHEXR = QtWidgets.QCheckBox(self.TABTCP)
        self.CBTCPHEXR.setMaximumSize(QtCore.QSize(16777215, 20))
        self.CBTCPHEXR.setObjectName("CBTCPHEXR")
        self.verticalLayout_4.addWidget(self.CBTCPHEXR)
        self.CBTCPHEXT = QtWidgets.QCheckBox(self.TABTCP)
        self.CBTCPHEXT.setMaximumSize(QtCore.QSize(16777215, 20))
        self.CBTCPHEXT.setObjectName("CBTCPHEXT")
        self.verticalLayout_4.addWidget(self.CBTCPHEXT)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 68, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.CBTCP2 = QtWidgets.QComboBox(self.TABTCP)
        self.CBTCP2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.CBTCP2.setObjectName("CBTCP2")
        self.verticalLayout_6.addWidget(self.CBTCP2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.TAB.addTab(self.TABTCP, icon, "")
        self.TABSerial = QtWidgets.QWidget()
        self.TABSerial.setObjectName("TABSerial")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.TABSerial)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.CBSerial = QtWidgets.QComboBox(self.TABSerial)
        self.CBSerial.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CBSerial.setFont(font)
        self.CBSerial.setObjectName("CBSerial")
        self.verticalLayout_7.addWidget(self.CBSerial)
        self.CBSerialBaudRate = QtWidgets.QComboBox(self.TABSerial)
        self.CBSerialBaudRate.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CBSerialBaudRate.setFont(font)
        self.CBSerialBaudRate.setDuplicatesEnabled(True)
        self.CBSerialBaudRate.setModelColumn(0)
        self.CBSerialBaudRate.setObjectName("CBSerialBaudRate")
        self.CBSerialBaudRate.addItem("")
        self.CBSerialBaudRate.addItem("")
        self.CBSerialBaudRate.addItem("")
        self.verticalLayout_7.addWidget(self.CBSerialBaudRate)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.CBSERHEXR = QtWidgets.QCheckBox(self.TABSerial)
        self.CBSERHEXR.setMaximumSize(QtCore.QSize(16777215, 35))
        self.CBSERHEXR.setObjectName("CBSERHEXR")
        self.horizontalLayout_5.addWidget(self.CBSERHEXR)
        self.CBSERHEXT = QtWidgets.QCheckBox(self.TABSerial)
        self.CBSERHEXT.setMaximumSize(QtCore.QSize(16777215, 35))
        self.CBSERHEXT.setObjectName("CBSERHEXT")
        self.horizontalLayout_5.addWidget(self.CBSERHEXT)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.TAB.addTab(self.TABSerial, "")
        self.TABFile = QtWidgets.QWidget()
        self.TABFile.setObjectName("TABFile")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.TABFile)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.LEFilePath = QtWidgets.QLineEdit(self.TABFile)
        self.LEFilePath.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LEFilePath.setFont(font)
        self.LEFilePath.setText("")
        self.LEFilePath.setObjectName("LEFilePath")
        self.verticalLayout_8.addWidget(self.LEFilePath)
        self.BTFilePath = QtWidgets.QPushButton(self.TABFile)
        self.BTFilePath.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.BTFilePath.setFont(font)
        self.BTFilePath.setObjectName("BTFilePath")
        self.verticalLayout_8.addWidget(self.BTFilePath)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.CBFHEXR = QtWidgets.QCheckBox(self.TABFile)
        self.CBFHEXR.setMaximumSize(QtCore.QSize(16777215, 35))
        self.CBFHEXR.setObjectName("CBFHEXR")
        self.horizontalLayout_6.addWidget(self.CBFHEXR)
        self.CBFHEXT = QtWidgets.QCheckBox(self.TABFile)
        self.CBFHEXT.setMaximumSize(QtCore.QSize(16777215, 35))
        self.CBFHEXT.setObjectName("CBFHEXT")
        self.horizontalLayout_6.addWidget(self.CBFHEXT)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.TAB.addTab(self.TABFile, "")
        self.horizontalLayout_11.addWidget(self.TAB)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.PBStart = QtWidgets.QPushButton(Form)
        self.PBStart.setMinimumSize(QtCore.QSize(50, 50))
        self.PBStart.setMaximumSize(QtCore.QSize(50, 50))
        self.PBStart.setAutoRepeat(False)
        self.PBStart.setAutoDefault(False)
        self.PBStart.setDefault(True)
        self.PBStart.setFlat(False)
        self.PBStart.setObjectName("PBStart")
        self.verticalLayout_9.addWidget(self.PBStart)
        self.PBStop = QtWidgets.QPushButton(Form)
        self.PBStop.setMinimumSize(QtCore.QSize(50, 50))
        self.PBStop.setMaximumSize(QtCore.QSize(50, 50))
        self.PBStop.setAutoRepeat(False)
        self.PBStop.setAutoDefault(False)
        self.PBStop.setDefault(True)
        self.PBStop.setFlat(False)
        self.PBStop.setObjectName("PBStop")
        self.verticalLayout_9.addWidget(self.PBStop)
        self.horizontalLayout_11.addLayout(self.verticalLayout_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.TESend = QtWidgets.QTextEdit(Form)
        self.TESend.setMinimumSize(QtCore.QSize(0, 60))
        self.TESend.setMaximumSize(QtCore.QSize(16777215, 60))
        self.TESend.setObjectName("TESend")
        self.verticalLayout_10.addWidget(self.TESend)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.PBSend = QtWidgets.QPushButton(Form)
        self.PBSend.setMaximumSize(QtCore.QSize(16777215, 35))
        self.PBSend.setAutoRepeat(False)
        self.PBSend.setAutoDefault(False)
        self.PBSend.setDefault(True)
        self.PBSend.setFlat(False)
        self.PBSend.setObjectName("PBSend")
        self.horizontalLayout_12.addWidget(self.PBSend)
        self.PB01 = QtWidgets.QPushButton(Form)
        self.PB01.setText("")
        self.PB01.setObjectName("PB01")
        self.horizontalLayout_12.addWidget(self.PB01)
        self.PB02 = QtWidgets.QPushButton(Form)
        self.PB02.setText("")
        self.PB02.setObjectName("PB02")
        self.horizontalLayout_12.addWidget(self.PB02)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.TEcmd = QtWidgets.QTextEdit(Form)
        self.TEcmd.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.TEcmd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TEcmd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TEcmd.setReadOnly(False)
        self.TEcmd.setObjectName("TEcmd")
        self.horizontalLayout_13.addWidget(self.TEcmd)
        self.TERceive = QtWidgets.QTextEdit(Form)
        self.TERceive.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.TERceive.setObjectName("TERceive")
        self.horizontalLayout_13.addWidget(self.TERceive)
        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.verticalLayout_10.setStretch(1, 2)
        self.verticalLayout_10.setStretch(3, 100)
        self.horizontalLayout_15.addLayout(self.verticalLayout_10)

        self.retranslateUi(Form)
        self.TAB.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LEUDP.setText(_translate("Form", "192.168.192.192"))
        self.CBUDPHEXR.setText(_translate("Form", "HEX<-"))
        self.CBUDPHEXT.setText(_translate("Form", "HEX->"))
        self.LEUDP2.setText(_translate("Form", "192.168.192.192"))
        self.TAB.setTabText(self.TAB.indexOf(self.TABUDP), _translate("Form", "UDP"))
        self.LETCPServer.setText(_translate("Form", "192.168.192.168"))
        self.CBTCPHEXR.setText(_translate("Form", "HEX<-"))
        self.CBTCPHEXT.setText(_translate("Form", "HEX->"))
        self.TAB.setTabText(self.TAB.indexOf(self.TABTCP), _translate("Form", "TCP"))
        self.CBSerialBaudRate.setCurrentText(_translate("Form", "115200"))
        self.CBSerialBaudRate.setItemText(0, _translate("Form", "115200"))
        self.CBSerialBaudRate.setItemText(1, _translate("Form", "38400"))
        self.CBSerialBaudRate.setItemText(2, _translate("Form", "9600"))
        self.CBSERHEXR.setText(_translate("Form", "HEX<-"))
        self.CBSERHEXT.setText(_translate("Form", "HEX->"))
        self.TAB.setTabText(self.TAB.indexOf(self.TABSerial), _translate("Form", "串口"))
        self.BTFilePath.setText(_translate("Form", "Open"))
        self.CBFHEXR.setText(_translate("Form", "HEX<-"))
        self.CBFHEXT.setText(_translate("Form", "HEX->"))
        self.TAB.setTabText(self.TAB.indexOf(self.TABFile), _translate("Form", "文件"))
        self.PBStart.setText(_translate("Form", "ON"))
        self.PBStop.setText(_translate("Form", "OFF"))
        self.PBSend.setText(_translate("Form", "------>"))