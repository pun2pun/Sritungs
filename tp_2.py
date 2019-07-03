
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.setWindowTitle('SRITUNG : Scadar')
mw.resize(1300,720)
cw = QtGui.QWidget()
mw.setCentralWidget(cw)
l = QtGui.QVBoxLayout()
cw.setLayout(l)

win = pg.GraphicsWindow()
win.setWindowTitle('SRITUNG : Scadar')


p1 = win.addPlot()
p2 = win.addPlot()



data1 = np.random.normal(size=300)
curve1 = p1.plot(data1,pen=pg.mkPen('b',width=1))
curve2 = p2.plot(data1,data1,pen=pg.mkPen('r',width=1))



ptr1 = 0
def update1():
    global data1, curve1, ptr1
    data1[:-1] = data1[1:]  # shift data in the array one sample left
                            # (see also: np.roll)
    data1[-1] = np.random.normal()
    curve1.setData(data1)
    
    ptr1 += 1
    curve2.setData(data1)
    curve2.setPos(ptr1, 0)
    

win.nextRow()
p3 = win.addPlot()
p4 = win.addPlot()


p3.setDownsampling(mode='peak')
p4.setDownsampling(mode='peak')
p3.setClipToView(True)
p4.setClipToView(True)
p3.setRange(xRange=[-100, 0])
p3.setLimits(xMax=0)
curve3 = p3.plot()
curve4 = p4.plot()

data3 = np.empty(100)
ptr3 = 0

def update2():
    global data3, ptr3
    data3[ptr3] = np.random.normal()
    ptr3 += 1
    if ptr3 >= data3.shape[0]:
        tmp = data3
        data3 = np.empty(data3.shape[0] * 2)
        data3[:tmp.shape[0]] = tmp
    curve3.setData(data3[:ptr3])
    curve3.setPos(-ptr3, 0)
    curve4.setData(data3[:ptr3])



startTime = pg.ptime.time()
win.nextRow()


def update():
    update1()
    update2()
    
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
