from PyQt5 import QtWidgets, QtGui, QtCore
from views_mangers.loginView_Manager import Login_Manager
from views_mangers.goal_view_manager import Goal_Manager
from views_mangers.register_view_manager import Register_Manager
from views_mangers.main_view_manager import Main_Mnager
from views_mangers.parkinson_Manager import Parkinson_Mnager
from views_mangers.alzhimer_manger import Alzahimer_MANGER
from views_mangers.blood_manger import Blood_MANGER
from views_mangers.breast_manger import BREAST_MANGER
from views_mangers.diabetes_manger import Diabetes_MANGER
from views_mangers.heart_manger import Heart_MANGER
import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
class Illminor(QtWidgets.QStackedWidget):
    def __init__(self , name=None, *args, **kwargs ):
        super(Illminor, self).__init__()

        self.base_url = "http://192.168.43.44:8000"

        #install widget
        self.login_manger = Login_Manager()
        self.goal_manager =Goal_Manager()
        self.register_manager=Register_Manager()
        self.main_manager=Main_Mnager()
        self.parkinson_manager=Parkinson_Mnager()
        self.alzahimer_manager=Alzahimer_MANGER()
        self.blood_manager=Blood_MANGER()
        self.breast_manager=BREAST_MANGER()
        self.diabetes_manager=Diabetes_MANGER()
        self.heart_manager=Heart_MANGER()

        # self.showFullScreen()


        # add widgets to the stack
        self.addWidget(self.login_manger) #0 done
        self.addWidget(self.goal_manager) #1
        self.addWidget(self.register_manager) #2
        self.addWidget(self.main_manager) #3
        self.addWidget(self.parkinson_manager) #4
        self.addWidget(self.alzahimer_manager) #5
        self.addWidget(self.blood_manager) #6
        self.addWidget(self.breast_manager) #7
        self.addWidget(self.diabetes_manager) #8
        self.addWidget(self.heart_manager) #9

        # install signals
        self.login_manger.DoctorloginAcceptedSignal.connect(self.handle_doctor_login)
        self.login_manger.PatientloginAcceptedSignal.connect(self.handle_patient_login)


        #success screen
        self.login_manger.signup_btn.clicked.connect(lambda :self.handel_signup)
        self.register_manager.login_pushbutton.clicked.connect(lambda :self.setCurrentIndex(0))
        self.goal_manager.doctor_btn.clicked.connect(lambda :self.setCurrentIndex(2))
        self.goal_manager.patient_btn.clicked.connect(lambda :self.setCurrentIndex(2))
        # self.login_manger.login_btn.clicked.connect(lambda :self.setCurrentIndex(3))
        self.main_manager.logout_btn.clicked.connect(lambda :self.setCurrentIndex(0))
        self.main_manager.parkinson_btn.clicked.connect(lambda :self.setCurrentIndex(4))
        self.main_manager.diabetes_btn.clicked.connect(self.handle_diabetes)
        self.parkinson_manager.back_btn.clicked.connect(lambda :self.setCurrentIndex(3))



        # self.login_manger.signup_lbl.clicked.connect(lambda :self.setCurrentIndex(1))



    def handle_doctor_login(self):
        self.setCurrentIndex(3)
    def handle_patient_login(self):
        self.main_manager.results_btn.setVisible(False)
        self.setCurrentIndex(3)
    def handle_signup(self):
        self.setCurrentIndex(2)

    def handle_diabetes(self):
        self.diabetes_manager.base_url=self.base_url
        self.diabetes_manager.token = self.login_manger.userToken
        self.setCurrentIndex(8)



if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    w = Illminor()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()