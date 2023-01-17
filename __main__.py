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
from views_mangers.change_password_manager import CHANGE_PASSWORD_Mnager
from views_mangers.profileclient_manager import PROFILE_CLIENT_Mnager
from views_mangers.profileclient_edit_manager import PROFILE_CLIENT_EDIT_Mnager
from views_mangers.results_manager import RESULTS_MANAGER
import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot

class Illminor(QtWidgets.QStackedWidget):
    def __init__(self , name=None, *args, **kwargs ):
        super(Illminor, self).__init__()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":ICONS/icons/Untitled-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Illminor"))

        self.base_url = "https://illacc.pythonanywhere.com"

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
        self.change_password_manager=CHANGE_PASSWORD_Mnager()
        self.profile_manager=PROFILE_CLIENT_Mnager()
        self.profile_edit_manager=PROFILE_CLIENT_EDIT_Mnager()
        self.results_manager=RESULTS_MANAGER()


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
        self.addWidget(self.change_password_manager) #9
        self.addWidget(self.profile_manager) #10
        self.addWidget(self.profile_edit_manager) #11
        self.addWidget(self.heart_manager) #12
        self.addWidget(self.results_manager) #13



        # install signals
        self.login_manger.DoctorloginAcceptedSignal.connect(self.handle_doctor_login)
        self.login_manger.PatientloginAcceptedSignal.connect(self.handle_patient_login)


        #istall back-btns
        self.parkinson_manager.back_btn.clicked.connect(lambda: self.setCurrentIndex(3))
        self.heart_manager.back_btn.clicked.connect(lambda: self.setCurrentIndex(3))
        self.breast_manager.back_btn_2.clicked.connect(lambda: self.setCurrentIndex(3))
        self.blood_manager.back_btn.clicked.connect(lambda: self.setCurrentIndex(3))
        self.diabetes_manager.back_btn.clicked.connect(lambda: self.setCurrentIndex(3))
        self.alzahimer_manager.back_btn.clicked.connect(lambda: self.setCurrentIndex(3))
        self.results_manager.back_btn.clicked.connect(lambda: self.setCurrentIndex(3))

        #success screen
        self.login_manger.signup_btn.clicked.connect(self.handle_signup_to_goal)
        self.main_manager.user_btn.clicked.connect(self.handle_main_to_user_profile)
        self.main_manager.change_password_btn.clicked.connect(self.handle_main_to_change_password)
        self.main_manager.brain_cancer_btn.clicked.connect(self.handle_main_to_alzahimer)
        self.main_manager.heart_btn.clicked.connect(self.handle_main_to_heart)
        self.main_manager.blood_btn.clicked.connect(self.handle_main_to_blood)
        self.main_manager.breast_btn.clicked.connect(self.handle_main_to_breast)
        self.main_manager.parkinson_btn.clicked.connect(self.handle_main_to_parkinsor)
        self.main_manager.diabetes_btn.clicked.connect(self.handle_diabetes)
        self.main_manager.results_btn.clicked.connect(self.main_to_results)


        self.register_manager.login_btn.clicked.connect(self.signup_to_login)
        self.register_manager.signupAcceptedSignal.connect(self.signup_to_login)

        self.goal_manager.doctor_btn.clicked.connect(self.goal_to_signup_doctor)
        self.goal_manager.patient_btn.clicked.connect(self.goal_to_patient_signup)
        self.profile_manager.home_btn.clicked.connect(self.hndle_profile_to_home)
        self.profile_manager.change_password_btn.clicked.connect(self.hndle_profile_to_change_password)
        self.profile_manager.editprofile_btn.clicked.connect(self.profile_to_edit_profile)
        self.profile_manager.logout_btn.clicked.connect(self.handle_logout)

        self.profile_edit_manager.change_password_btn.clicked.connect(self.hndle_profile_edit_to_change_password)
        self.profile_edit_manager.home_btn.clicked.connect(self.hndle_profile_edit_to_home)
        self.profile_edit_manager.logout_btn.clicked.connect(self.handle_logout)
        self.profile_manager.logout_btn.clicked.connect(self.handle_logout)
        self.change_password_manager.home_btn.clicked.connect(self.chanage_password_to_home)
        self.change_password_manager.user_btn.clicked.connect(self.chanage_password_to_profile)
        self.profile_manager.editprofile_btn.clicked.connect(self.profile_to_edit_profile)

        self.register_manager.login_btn.clicked.connect(self.signup_to_login)

        self.profile_edit_manager.cancel_btn.clicked.connect(self.profile_edit_to_profile)

    def goal_to_patient_signup(self):
        self.register_manager.base_url = self.base_url
        self.register_manager.is_doctor = False
        self.setCurrentIndex(2)

    def goal_to_signup_doctor(self):
        self.register_manager.base_url = self.base_url
        self.register_manager.is_doctor = True
        self.setCurrentIndex(2)

    def handle_doctor_login(self):
        self.profile_manager.firstTime = True
        self.main_manager.results_btn.setVisible(True)
        self.profile_manager.groupBox_4.setVisible(False)
        self.setCurrentIndex(3)

    def handle_patient_login(self):
        self.profile_manager.firstTime = True
        self.profile_manager.groupBox_4.setVisible(True)
        self.main_manager.results_btn.setVisible(False)
        self.setCurrentIndex(3)

    def handle_main_to_change_password(self):
        self.setCurrentIndex(9)

    def handle_main_to_user_profile(self):
        if self.profile_manager.firstTime:
            self.profile_manager.username = self.login_manger.username
            self.profile_manager.token = self.login_manger.userToken
            self.profile_manager.base_url = self.base_url
            self.profile_manager.run()
        self.setCurrentIndex(10)

    def handle_main_to_parkinsor(self):
        self.parkinson_manager.base_url=self.base_url
        self.parkinson_manager.token = self.login_manger.userToken
        self.setCurrentIndex(4)

    def  handle_main_to_breast(self):
        self.breast_manager.base_url=self.base_url
        self.breast_manager.token = self.login_manger.userToken
        self.setCurrentIndex(7)
    def handle_main_to_blood(self):
        self.blood_manager.base_url = self.base_url
        self.blood_manager.token = self.login_manger.userToken
        self.setCurrentIndex(6)
    def handle_main_to_heart(self):
        self.heart_manager.base_url=self.base_url
        self.heart_manager.token = self.login_manger.userToken
        # self.heart_manager.run()
        self.setCurrentIndex(12)
    def handle_main_to_alzahimer(self):
        self.alzahimer_manager.base_url=self.base_url
        self.alzahimer_manager.token = self.login_manger.userToken
        self.setCurrentIndex(5)
    def main_to_results(self):
        self.results_manager.base_url = self.base_url
        self.results_manager.token = self.login_manger.userToken
        self.setCurrentIndex(13)
    def signup_to_login(self):
        self.clear_login()
        self.setCurrentIndex(0)
    def profile_edit_to_profile(self):
        self.setCurrentIndex(10)

    def profile_to_edit_profile(self):
        self.setCurrentIndex(11)
    def chanage_password_to_profile(self):
        self.setCurrentIndex(10)
    def chanage_password_to_home(self):
        self.setCurrentIndex(3)
    def handle_logout(self):
        self.clear_login()
        self.setCurrentIndex(0)
    def hndle_profile_edit_to_home(self):
        self.setCurrentIndex(3)
    def hndle_profile_edit_to_change_password(self):
        self.setCurrentIndex(9)
    def hndle_profile_to_change_password(self):
        self.setCurrentIndex(9)
    def hndle_profile_to_home(self):
        self.setCurrentIndex(3)

    def handle_signup_to_goal(self):
        self.setCurrentIndex(1)

    def handle_diabetes(self):
        self.diabetes_manager.base_url=self.base_url
        self.diabetes_manager.token = self.login_manger.userToken
        self.setCurrentIndex(8)

    def clear_login(self):
        self.login_manger.username_lin.clear()
        self.login_manger.password_lin.clear()

if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    w = Illminor()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()