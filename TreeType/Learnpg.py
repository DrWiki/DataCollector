import argparse
from collections import deque
from time import perf_counter
import numpy as np
import pyqtgraph as pg
import pyqtgraph.functions as fn
import pyqtgraph.parametertree as ptree
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# don't limit frame rate to vsync
sfmt = QtGui.QSurfaceFormat()
sfmt.setSwapInterval(0)
QtGui.QSurfaceFormat.setDefaultFormat(sfmt)

global data, connect_array, ptr


class MonkeyCurveItem(pg.PlotCurveItem):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.monkey_mode = ''

    def setMethod(self, param, value):
        self.monkey_mode = value

    def paint(self, painter, opt, widget):
        if self.monkey_mode not in ['drawPolyline']:
            return super().paint(painter, opt, widget)

        painter.setRenderHint(painter.RenderHint.Antialiasing, self.opts['antialias'])
        painter.setPen(pg.mkPen(self.opts['pen']))

        if self.monkey_mode == 'drawPolyline':
            painter.drawPolyline(fn.arrayToQPolygonF(self.xData, self.yData))

class Treepara(ptree.ParameterTree):
    def __init__(self, exchild):
        super(Treepara, self).__init__(showHeader=False)
        if exchild==None:
            self.children = [
                dict(name='sigopts', title='Signal Options', type='group', children=[
                    dict(name='noise', type='bool', value=True),
                    dict(name='nsamples', type='int', limits=[0, None], value=5000),
                    dict(name='frames', type='int', limits=[1, None], value=1000),
                    dict(name='fsample', title='sample rate', type='float', value=1000, units='Hz'),
                    dict(name='frequency', type='float', value=1000, units='Hz'),
                    dict(name='amplitude', type='float', value=1000),
                ]),
                dict(name='useOpenGL', type='bool', value=pg.getConfigOption('useOpenGL'), readonly=not True),
                dict(name='enableExperimental', type='bool', value=pg.getConfigOption('enableExperimental')),
                dict(name='pen', type='pen', value=pg.mkPen(color="b")),
                dict(name='antialias', type='bool', value=pg.getConfigOption('antialias')),
                dict(name='connect', type='list', limits=['all', 'pairs', 'finite', 'array'], value='all'),
                dict(name='fill', type='bool', value=False),
                dict(name='skipFiniteCheck', type='bool', value=False),
                dict(name='plotMethod', title='Plot Method', type='list', limits=['pyqtgraph', 'drawPolyline'])
            ]
        else:
            self.children = exchild

        self.params = ptree.Parameter.create(name='Parameters', type='group', children=self.children)
        self.setParameters(self.params)
        self.params.child("sigopts").addChildren(
            [dict(name='XXXXX', title='Plot XXXXX', type='list', limits=['pyqtgraph', 'drawPolyline'])])






class Wdigetfortree(QtWidgets.QSplitter):
    def __init__(self):
        super(Wdigetfortree, self).__init__()
        self.pTree = Treepara(None)
        self.pw = pg.PlotWidget()
        self.pw.setWindowTitle('pyqtgraph example: PlotSpeedTest')
        self.pw.setLabel('bottom', 'Index', units='B')
        self.curve = MonkeyCurveItem(pen=pg.mkPen(), brush='g')
        self.pw.addItem(self.curve)
        self.addWidget(self.pTree)
        self.addWidget(self.pw)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(0)
        self.CONNET()
        self.makeData()
        global elapsed, fpsLastUpdate

        rollingAverageSize = 1000
        elapsed = deque(maxlen=rollingAverageSize)
        fpsLastUpdate = perf_counter()

    def makeData(self,*args):
        global data, connect_array, ptr
        sigopts = self.pTree.params.child('sigopts')
        nsamples = sigopts['nsamples']
        frames = sigopts['frames']
        Fs = sigopts['fsample']
        A = sigopts['amplitude']
        F = sigopts['frequency']
        ttt = np.arange(frames * nsamples, dtype=np.float64) / Fs
        data = A * np.sin(2 * np.pi * F * ttt).reshape((frames, nsamples))
        if sigopts['noise']:
            data += np.random.normal(size=data.shape)
        connect_array = np.ones(data.shape[-1], dtype=bool)
        ptr = 0
        self.pw.setRange(QtCore.QRectF(0, -10, nsamples, 20))

    def resetTimings(self, *args):
        elapsed.clear()
    def update(self):
        global curve, data, ptr, elapsed, fpsLastUpdate

        options = ['antialias', 'connect', 'skipFiniteCheck']
        kwds = { k : self.pTree.params[k] for k in options }
        if kwds['connect'] == 'array':
            kwds['connect'] = connect_array
        #
        # Measure
        t_start = perf_counter()
        self.curve.setData(data[ptr], **kwds)
        app.processEvents(QtCore.QEventLoop.ProcessEventsFlag.AllEvents)
        t_end = perf_counter()
        elapsed.append(t_end - t_start)
        ptr = (ptr + 1) % data.shape[0]

        # update fps at most once every 0.2 secs
        if t_end - fpsLastUpdate > 0.2:
            fpsLastUpdate = t_end
            average = np.mean(elapsed)
            fps = 1 / average
            self.pw.setTitle('%0.2f fps - %0.1f ms avg' % (fps, average * 1_000))

    def CONNET(self):
        self.pTree.params.child('sigopts').sigTreeStateChanged.connect(self.makeData)
        self.pTree.params.child('useOpenGL').sigValueChanged.connect(self.onUseOpenGLChanged)
        self.pTree.params.child('enableExperimental').sigValueChanged.connect(self.onEnableExperimentalChanged)
        self.pTree.params.child('pen').sigValueChanged.connect(self.onPenChanged)
        self.pTree.params.child('fill').sigValueChanged.connect(self.onFillChanged)
        self.pTree.params.child('plotMethod').sigValueChanged.connect(self.curve.setMethod)
        self.pTree.params.sigTreeStateChanged.connect(self.resetTimings)
        pass

    def onUseOpenGLChanged(self, param, enable):
        self.pw.useOpenGL(enable)

    def onEnableExperimentalChanged(self,param, enable):
        pg.setConfigOption('enableExperimental', enable)

    def onPenChanged(self,param, pen):
        self.curve.setPen(pen)

    def onFillChanged(self,param, enable):
        self.curve.setFillLevel(0.0 if enable else None)


if __name__ == '__main__':
    app = pg.mkQApp("Plot Speed Test")
    w = Wdigetfortree()
    w.show()
    pg.exec()
