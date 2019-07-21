from PyQt4 import QtCore,QtGui
from pyqtgraph.Qt import QtCore,QtGui
import pyqtgraph as pg
from random import randrange
import sys
import Actions
import numpy as np
from math import sin
import cv2
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MainWindow(object):
    def setupUI(self,MainWindow):
       
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        #MainWindow.showMaximized()
        MainWindow.showFullScreen()
        MainWindow.setStyleSheet("QMainWindow{background-color:black;}")

        self.centralWidget = QtGui.QWidget(MainWindow)
        
        #------------------------------- Add Windiow for show --------------------------
        self.win = pg.GraphicsWindow()
        self.win2 = pg.GraphicsWindow()
        self.win3 = pg.GraphicsWindow()
        self.win4 = pg.GraphicsWindow()

        pg.setConfigOptions(antialias=True)

        #---------------------------------- Variable for store value --------------------------

        self.time_stack = []
        self.time_stack_overload = []
        self.time_stack_fall = []

        self.time_stack_2 = []
        self.time_stack_3 = []
        self.time_stack_4 = []

        #------------------------------------ Graph Option ----------------------------------

        self.p1 = self.win.addPlot(title="Machine 1")
        self.p1.showGrid(x=True, y=True)
        self.p1.setYRange(-3,3,padding=0)
        self.p1.setLabel('left', "Current(A) ")
        self.p1.setLabel('bottom', "time(s) ")

        self.p2 = self.win2.addPlot(title="Machine 2")
        self.p2.showGrid(x=True, y=True)
        self.p2.setYRange(-5,5,padding=0)
        self.p2.setLabel('left', "Current(A) ")
        self.p2.setLabel('bottom', "time(s) ")

        self.p3 = self.win3.addPlot(title="Machine 3")
        self.p3.showGrid(x=True, y=True)
        self.p3.setYRange(-5,5,padding=0)
        self.p3.setLabel('left', "Current(A) ")
        self.p3.setLabel('bottom', "time(s) ")

        self.p4 = self.win4.addPlot(title="Machine 4")
        self.p4.showGrid(x=True, y=True)
        self.p4.setYRange(-5,5,padding=0)
        self.p4.setLabel('left', "Current(A) ")
        self.p4.setLabel('bottom', "time(s) ")
        
        #------------------------------------- Graph line option ---------------------------------------

        self.curve1 = self.p1.plot(self.time_stack,pen=pg.mkPen('b',width=2))
        self.curve1_overload = self.p1.plot(self.time_stack,pen=pg.mkPen('r',width=1))
        self.curve1_fall = self.p1.plot(self.time_stack,pen=pg.mkPen('r',width=1))

        self.curve2 = self.p2.plot(self.time_stack_2,pen=pg.mkPen('g',width=2))
        self.curve3 = self.p3.plot(self.time_stack_3,pen=pg.mkPen('y',width=2))
        self.curve4 = self.p4.plot(self.time_stack_4,pen=pg.mkPen('w',width=2))

        #------------------------------------- Add Graph 1 ----------------------------------------------

        self.graph_area = QtGui.QWidget(self.centralWidget)
        self.graph_area.setGeometry(25,90,650,300)
        

        self.curret_text_1 = QtGui.QLabel(self.centralWidget)
        self.curret_text_1.setStyleSheet('QLabel{font:bold 34px; color:White;}')
        self.curret_text_1.setObjectName(_fromUtf8("label"))

        self.layout1 = QtGui.QVBoxLayout()
        self.layout1.addWidget(self.win)
        self.layout1.addWidget(self.curret_text_1)
        
        self.graph_area.setStyleSheet('QWidget{border:1px solid gray;}')
        self.graph_area.setLayout(self.layout1)
        

        self.graph_area.setObjectName(_fromUtf8("graph_area"))

        #------------------------------------- Add Graph 2 ----------------------------------------------
        self.graph_area_2 = QtGui.QWidget(self.centralWidget)
        self.graph_area_2.setGeometry(700,90,650,300)
        

        self.curret_text_2 = QtGui.QLabel(self.centralWidget)
        self.curret_text_2.setStyleSheet('QLabel{font:bold 34px; color:White;}')
        self.curret_text_2.setObjectName(_fromUtf8("label"))

        self.layout2 = QtGui.QVBoxLayout()
        self.layout2.addWidget(self.win2)
        self.layout2.addWidget(self.curret_text_2)
        
        self.graph_area_2.setStyleSheet('QWidget{border:1px solid gray;}')
        self.graph_area_2.setLayout(self.layout2)
        

        self.graph_area_2.setObjectName(_fromUtf8("graph_area"))

        #------------------------------------- Add Graph 3 ----------------------------------------------
        self.graph_area_3 = QtGui.QWidget(self.centralWidget)
        self.graph_area_3.setGeometry(25,400,650,300)
        

        self.curret_text_3 = QtGui.QLabel(self.centralWidget)
        self.curret_text_3.setStyleSheet('QLabel{font:bold 34px; color:White;}')
        self.curret_text_3.setObjectName(_fromUtf8("label"))

        self.layout3 = QtGui.QVBoxLayout()
        self.layout3.addWidget(self.win3)
        self.layout3.addWidget(self.curret_text_3)
        
        self.graph_area_3.setStyleSheet('QWidget{border:1px solid gray;}')
        self.graph_area_3.setLayout(self.layout3)
        

        self.graph_area_3.setObjectName(_fromUtf8("graph_area_3"))

        #------------------------------------- Add Graph 4 ----------------------------------------------
        self.graph_area_4 = QtGui.QWidget(self.centralWidget)
        self.graph_area_4.setGeometry(700,400,650,300)
        

        self.curret_text_4 = QtGui.QLabel(self.centralWidget)
        self.curret_text_4.setStyleSheet('QLabel{font:bold 34px; color:White;}')
        self.curret_text_4.setObjectName(_fromUtf8("label"))

        self.layout4 = QtGui.QVBoxLayout()
        self.layout4.addWidget(self.win4)
        self.layout4.addWidget(self.curret_text_4)
        
        self.graph_area_4.setStyleSheet('QWidget{border:1px solid gray;}')
        self.graph_area_4.setLayout(self.layout4)
        

        self.graph_area_4.setObjectName(_fromUtf8("graph_area_4"))
        #------------------------------------- Add Image ----------------------------------------------
        ref_image = cv2.imread("ref.png")
        ref_image = cv2.cvtColor(ref_image,cv2.COLOR_BGR2RGB)

        scale_percent = 45
        width = int(ref_image.shape[1] * scale_percent / 100)
        height = int(ref_image.shape[0] * scale_percent / 100)
        dim = (width, height) 

        ref_image = cv2.resize(ref_image, dim, interpolation = cv2.INTER_AREA) 
        ref_image = QtGui.QImage(ref_image, ref_image.shape[1],ref_image.shape[0], ref_image.shape[1] * 3,QtGui.QImage.Format_RGB888)
        ref_pix = QtGui.QPixmap(ref_image)

        self.ref_image = QtGui.QLabel(self.centralWidget)
        self.ref_image.setGeometry(QtCore.QRect(1, 2, width, height))
        self.ref_image.setPixmap(ref_pix)


        #------------------------------------- Add Label ----------------------------------------------

   

       
        self.title_text =QtGui.QLabel(self.centralWidget)
        self.title_text.setGeometry(980,20,500,34)
        self.title_text.setStyleSheet('QLabel{font:italic bold 34px Azonix;  color:White;}')
        self.title_text.setObjectName(_fromUtf8("title_text"))
        

        self.title_text_add =QtGui.QLabel(self.centralWidget)
        self.title_text_add.setGeometry(1200,43,500,34)
        self.title_text_add.setStyleSheet('QLabel{font: 15px; color:White;}')
        self.title_text_add.setObjectName(_fromUtf8("title_text_add"))

        self.time_text =QtGui.QLabel(self.centralWidget)
        self.time_text.setGeometry(1200,720,200,34)
        self.time_text.setStyleSheet('QLabel{font: 15px; color:White;}')
        self.time_text.setObjectName(_fromUtf8("time_text"))

    #------------------------------------- End Add Label ----------------------------------------------


        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.time = 0
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(500)

    def update(self):
        self.time += 1
     
        data = 2*sin(2*3.14*50*self.time)
        data_2 = (2*sin(2*3.14*50*self.time) - randrange(-2,2))
        data_3 = (1*sin(2*3.14*50*self.time) + randrange(-2,2))
        data_4 = (1*sin(2*3.14*50*self.time) + randrange(-1,1))

        self.time_stack.append(data)
        self.time_stack_overload.append(2.4)
        self.time_stack_fall.append(-2.6)

        self.time_stack_2.append(data_2)
        self.time_stack_3.append(data_3)
        self.time_stack_4.append(data_4)

        self.curve1.setData(self.time_stack)
        self.curve1_overload.setData(self.time_stack_overload)
        self.curve1_fall.setData(self.time_stack_fall)

        self.curve2.setData(self.time_stack_2)
        self.curve3.setData(self.time_stack_3)
        self.curve4.setData(self.time_stack_4)

        self.curret_text_1.setText(QtGui.QApplication.translate("MainWindow","Current                        %.2f        A."%(data), None, QtGui.QApplication.UnicodeUTF8))
        self.curret_text_2.setText(QtGui.QApplication.translate("MainWindow","Current                        %.2f        A."%(data_2), None, QtGui.QApplication.UnicodeUTF8))
        self.curret_text_3.setText(QtGui.QApplication.translate("MainWindow","Current                        %.2f        A."%(data_3), None, QtGui.QApplication.UnicodeUTF8))
        self.curret_text_4.setText(QtGui.QApplication.translate("MainWindow","Current                        %.2f        A."%(data_4), None, QtGui.QApplication.UnicodeUTF8))


        self.time_text.setText(QtGui.QApplication.translate("MainWindow", time.ctime(), None, QtGui.QApplication.UnicodeUTF8))
        
    def retranslateUi(self, MainWindow):

        self.title_text.setText(QtGui.QApplication.translate("MainWindow","SRITUNG-Scadar", None, QtGui.QApplication.UnicodeUTF8))
        self.title_text_add.setText(QtGui.QApplication.translate("MainWindow","Developed by EE-UBU", None, QtGui.QApplication.UnicodeUTF8))

        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))       
        self.curret_text_1.setText(QtGui.QApplication.translate("MainWindow", "  PLOTS", None, QtGui.QApplication.UnicodeUTF8))
        self.curret_text_2.setText(QtGui.QApplication.translate("MainWindow", "  PLOTS", None, QtGui.QApplication.UnicodeUTF8))
        
   
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
