from PyQt4 import QtCore,QtGui
from pyqtgraph.Qt import QtCore,QtGui
import pyqtgraph as pg
from random import randrange
import sys
import Actions
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MainWindow(object):
    def setupUI(self,MainWindow):
       
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.showMaximized()
        
       # MainWindow.showFullScreen()
        MainWindow.setStyleSheet("QMainWindow{background-color:black;}")

        self.centralWidget = QtGui.QWidget(MainWindow)
        

        self.win = pg.GraphicsWindow(title="Basic plotting examples")
        self.win.setWindowTitle('pyqtgraph example: Plotting')

        self.win2 = pg.GraphicsWindow(title="Basic plotting examples")
        self.win2.setWindowTitle('pyqtgraph example: Plotting')

        pg.setConfigOptions(antialias=True)

        self.time_stack = []
        
        self.p1 = self.win.addPlot(title="Cerrent 1")
        self.p2 = self.win2.addPlot(title="Cerrent 2")

        self.curve1 = self.p1.plot(self.time_stack,pen=pg.mkPen('b',width=1))

        #------------------------------------- Add Graph 1 ----------------------------------------------

        self.graph_area = QtGui.QWidget(self.centralWidget)
        self.graph_area.setGeometry(25,90,500,300)
        self.graph_area.setStyleSheet('QWidget{border:1px solid gray;}')

        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(20,20,70,34)
        self.label.setStyleSheet('QLabel{font:bold 34px; color:White;}')
        self.label.setObjectName(_fromUtf8("label"))

        self.layout1 = QtGui.QVBoxLayout()
        self.layout1.addWidget(self.win)
        self.layout1.addWidget(self.label)
        
        self.graph_area.setLayout(self.layout1)
        

        self.graph_area.setObjectName(_fromUtf8("graph_area"))

        #------------------------------------- Add Graph 2 ----------------------------------------------

        self.graph_area_2 = QtGui.QWidget(self.centralWidget)
        self.graph_area_2.setGeometry(700,90,500,300)
        self.graph_area_2.setStyleSheet('QWidget{border:1px solid gray;}')

        self.label = QtGui.QLabel(self.centralWidget)
        #self.label.setGeometry(20,20,70,34)
        self.label.setStyleSheet('QLabel{font:bold 34px; color:White;}')
        self.label.setObjectName(_fromUtf8("label"))

        self.layout2 = QtGui.QVBoxLayout()
        self.layout2.addWidget(self.win2)
        self.layout2.addWidget(self.label)
      
        
        self.graph_area_2.setLayout(self.layout2)
        

        self.graph_area_2.setObjectName(_fromUtf8("graph_area_2"))
        #------------------------------------- Add Label ----------------------------------------------

   


        self.title_text =QtGui.QLabel(self.centralWidget)
        self.title_text.setGeometry(1050,20,500,34)
        self.title_text.setStyleSheet('QLabel{font:bold 34px;  color:White;}')
        self.title_text.setObjectName(_fromUtf8("title_text"))

        self.title_text_add =QtGui.QLabel(self.centralWidget)
        self.title_text_add.setGeometry(1200,43,500,34)
        self.title_text_add.setStyleSheet('QLabel{font: 15px; color:White;}')
        self.title_text_add.setObjectName(_fromUtf8("title_text_add"))

    #------------------------------------- Add Label ----------------------------------------------


        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.time = 0
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(500)

    def update(self):
        self.time += 1
     
        data = self.time*randrange(-10,10)
        self.time_stack.append(data)
        self.curve1.setData(self.time_stack)
        self.label.setText(QtGui.QApplication.translate("MainWindow", str(data)+"  A.", None, QtGui.QApplication.UnicodeUTF8))

    def retranslateUi(self, MainWindow):

        self.title_text.setText(QtGui.QApplication.translate("MainWindow","SRITUNG-Scadar", None, QtGui.QApplication.UnicodeUTF8))
        self.title_text_add.setText(QtGui.QApplication.translate("MainWindow","Developed by EE-UBU", None, QtGui.QApplication.UnicodeUTF8))

        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))       
        self.label.setText(QtGui.QApplication.translate("MainWindow", "  PLOTS", None, QtGui.QApplication.UnicodeUTF8))
        
   
        '''
        self.btn_test = QtGui.QPushButton()
        self.btn_test.setGeometry(20,20,200,100)
        self.btn_test.setStyleSheet('QPushButton{background-color:red;}')
        self.btn_test.setText('Test Buton')
        self.btn_test.clicked.connect(Actions.ButtonAction.TestClick)
        self.btn_test.show()
        '''



if __name__ == "__main__":
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUI(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
