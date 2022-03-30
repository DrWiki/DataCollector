import numpy as np
import pyqtgraph as pg
from pyqtgraph.console import ConsoleWidget
from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea
from pyqtgraph.Qt import QtWidgets


class TreeDockWidget(QtWidgets.QWidget):
    def __init__(self):
        super(TreeDockWidget, self).__init__()
        self.area = DockArea()
        # self.setCentralWidget(self.area)
        self.l = QtWidgets.QVBoxLayout()
        self.setLayout(self.l)
        self.l.addWidget(self.area)
        self.d1 = Dock("Dock1",closable=False)     ## give this dock the minimum possible size
        self.d2 = Dock("Dock2 - Console", closable=False)
        self.area.addDock(self.d1, 'left')      ## place d1 at left edge of dock area (it will fill the whole space since there are no other docks yet)
        self.area.addDock(self.d2, 'right')     ## place d2 at right edge of dock area
        ## first dock gets save/restore buttons
        self.w1 = pg.LayoutWidget()
        self.label = QtWidgets.QTextEdit()
        self.label.setText("          ")
        self.saveBtn = QtWidgets.QPushButton('Save dock state')
        self.restoreBtn = QtWidgets.QPushButton('Restore dock state')
        self.restoreBtn.setEnabled(False)
        self.w1.addWidget(self.label, row=0, col=0)
        self.w1.addWidget(self.saveBtn, row=1, col=0)
        self.w1.addWidget(self.restoreBtn, row=2, col=0)
        self.d1.addWidget(self.w1)

        self.saveBtn.clicked.connect(self.save)
        self.restoreBtn.clicked.connect(self.load)
        self.w2 = ConsoleWidget()
        self.d2.addWidget(self.w2)
    def save(self):
        self.state = self.area.saveState()
        self.restoreBtn.setEnabled(True)
    def load(self):
        self.area.restoreState(self.state)

if __name__ == '__main__':
    app = pg.mkQApp("DockArea Example")

    win = TreeDockWidget()
    win.show()
    pg.exec()
