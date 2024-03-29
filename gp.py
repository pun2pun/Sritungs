import pyqtgraph as pg 
from pyqtgraph import QtCore ,QtGui

class CandlestickItem(pg.GraphicsObject):
    def __init__(self,data):
        pg.GraphicsObject.__init__(self)
        self.data = data
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0]) - self.data[0][0] / 3 
        for (t,open,close,min,max) in self.data :
            p.drawLine(QtCore.QPointF(t,min),QtCore.QPointF(t,max))
            if open > close:
                p.setBrush(pg.mkBrush('r'))
            else:
                p.setBrush(pg.mkBrush('g'))
            p.drawRect(QtCore.QRectF(t-w,open,w*2,close-open))
        p.end()
    def paint(self,p,*args):
        p.drawPicture(0,0,self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())


data = [
    (1.,10,13,5,15),
    (2.,13,17,9,20),
    (3.,17,14,11,23)

]

item = CandlestickItem(data)
plt = pg.plot()
for i in range(3):
plt.addItem(item)

QtGui.QApplication.exec_()