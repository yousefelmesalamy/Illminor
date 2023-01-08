from PyQt5 import QtWidgets, QtGui, QtCore
from views_mangers.loginView_Manager import Login_Manager
from views_mangers.goal_view_manager import Goal_Manager
from views_mangers.register_view_manager import Register_Manager
from views_mangers.main_view_manager import Main_Mnager
from views_mangers.parkinson_Manager import Parkinson_Mnager
import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
class Illminor(QtWidgets.QStackedWidget):
    def __init__(self , name=None, *args, **kwargs ):
        super(Illminor, self).__init__()

        #install widget
        self.login_manger = Login_Manager()
        self.goal_manager =Goal_Manager()
        self.register_manager=Register_Manager()
        self.main_manager=Main_Mnager()
        self.parkinson_manager=Parkinson_Mnager()

        # self.showFullScreen()


        # add widgets to the stack
        self.addWidget(self.login_manger) #0 done
        self.addWidget(self.goal_manager) #1
        self.addWidget(self.register_manager) #2

        self.addWidget(self.main_manager) #3
        self.addWidget(self.parkinson_manager) #4


        # install signals
        # self.login_manger.loginAcceptedSignal.connect(self.handle_login_accepted)



        #success screen
        self.login_manger.signup_btn.clicked.connect(lambda :self.setCurrentIndex(1))
        self.register_manager.login_pushbutton.clicked.connect(lambda :self.setCurrentIndex(0))
        self.goal_manager.doctor_btn.clicked.connect(lambda :self.setCurrentIndex(2))
        self.goal_manager.patient_btn.clicked.connect(lambda :self.setCurrentIndex(2))
        self.login_manger.login_btn.clicked.connect(lambda :self.setCurrentIndex(3))
        self.main_manager.logout_btn.clicked.connect(lambda :self.setCurrentIndex(0))
        self.main_manager.parkinson_btn.clicked.connect(lambda :self.setCurrentIndex(4))
        self.parkinson_manager.back_btn.clicked.connect(lambda :self.setCurrentIndex(3))




        # self.login_manger.signup_lbl.clicked.connect(lambda :self.setCurrentIndex(1))


        '''
        new order view signals
        '''

        # self.newOrder_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(1))



if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    w = Illminor()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()