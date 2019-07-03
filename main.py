from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
import random
import time 

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        MainWindow.resize(self,1380,800)
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.GetBegin = QtGui.QPushButton("Start")
        self.GetBegin.setGeometry(QtCore.QRect(10, 10, 10, 100))
        '''
        self.login_widget = LoginWidget(self)
        self.login_widget.button.clicked.connect(self.plotter)
        self.login_widget.setGeometry(QtCore.QRect(10, 10, 550, 300))

        self.login_widget_2 = LoginWidget_2(self)
        self.login_widget_2.button_2.clicked.connect(self.plotter_2)
        self.login_widget_2.setGeometry(QtCore.QRect(650, 10, 550, 300))

        
        self.login_widget_3 = LoginWidget_3(self)
        self.login_widget_3.button_3.clicked.connect(self.plotter_2)
        self.login_widget_3.setGeometry(QtCore.QRect(10, 350, 550, 300))

        self.login_widget_4 = LoginWidget_4(self)
        self.login_widget_4.button_4.clicked.connect(self.plotter_2)
        self.login_widget_4.setGeometry(QtCore.QRect(650, 350, 550, 300))
        '''

    def plotter(self):
        self.data =[0]
        self.curve = self.login_widget.plot.getPlotItem().plot()
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(0)

    def plotter_2(self):
      
        self.data_2 =[0]
        self.curve_2 = self.login_widget_2.plot_2.getPlotItem().plot()

        self.timer_2 = QtCore.QTimer()
        self.timer_2.timeout.connect(self.updater_2)
        self.timer_2.start(0)
        
    def updater(self):

        self.data.append(self.data[-1]+0.2*(0.5-random.random()) )
        self.curve.setData(self.data)


    def updater_2(self):

        self.data_2.append(self.data_2[-1]+0.2*(0.5-random.random()) )
        self.curve_2.setData(self.data_2)

class LoginWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.button = QtGui.QPushButton('Curent 1')
        layout.addWidget(self.button)
        
        self.plot = pg.PlotWidget()
        
        layout.addWidget(self.plot)
             
        self.setLayout(layout)

class LoginWidget_2(QtGui.QWidget):
    def __init__(self,parent=None):
        super(LoginWidget_2, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.button_2 = QtGui.QPushButton('Curent 2 ')
        layout.addWidget(self.button_2)
        self.plot_2 = pg.PlotWidget()       
        layout.addWidget(self.plot_2)            
        self.setLayout(layout)


class LoginWidget_3(QtGui.QWidget):
    def __init__(self,parent=None):
        super(LoginWidget_3, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.button_3 = QtGui.QPushButton('Curent 3 ')
        layout.addWidget(self.button_3)
        self.plot_3 = pg.PlotWidget()       
        layout.addWidget(self.plot_3)            
        self.setLayout(layout)


class LoginWidget_4(QtGui.QWidget):
    def __init__(self,parent=None):
        super(LoginWidget_4, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.button_4 = QtGui.QPushButton('Curent 4 ')
        layout.addWidget(self.button_4)
        self.plot_4 = pg.PlotWidget()       
        layout.addWidget(self.plot_4)            
        self.setLayout(layout)



if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()