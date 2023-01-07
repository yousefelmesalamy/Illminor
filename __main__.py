from PyQt5 import QtWidgets, QtGui, QtCore
from views_mangers.loginView_Manager import Login_Manager
import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot

class Illminor(QtWidgets.QStackedWidget):
    def __init__(self , name=None, *args, **kwargs ):
        super(Illminor, self).__init__()

        self.login_manger = Login_Manager()


        self.showFullScreen()


        # add widgets to the stack
        self.addWidget(self.login_manger) #0 done


        # install signals
        # self.login_manger.loginAcceptedSignal.connect(self.handle_login_accepted)


        '''
        new order view signals
        '''

        # self.newOrder_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))



if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Illminor()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()