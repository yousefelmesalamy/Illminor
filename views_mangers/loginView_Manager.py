from PyQt5 import QtWidgets , QtCore
from views import login_view
import json
import requests
import os
class Login_Manager(QtWidgets.QWidget, login_view.Ui_login_Form):
    DoctorloginAcceptedSignal = QtCore.pyqtSignal()
    PatientloginAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(Login_Manager, self).__init__()
        self.setupUi(self)

        self.login_btn.clicked.connect(self.handle_login)
        self.base_url = "http://172.20.10.2:8000/login/"
        self.userToken = ''

    def handle_login(self):
        msg = QtWidgets.QMessageBox()
        username = self.username_lin.text()
        password = self.password_lin.text()
        if len(username) == 0:
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        elif len(password) == 0:
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        else:
            data = {
                    "username": username,
                    "password": password
                    }
            try:
                self.user_check = requests.post(self.base_url, data=data)
                self.json_response = self.user_check.json()
                self.json_statusCode = self.user_check.status_code
            except (requests.ConnectionError, requests.Timeout) as exception:
                print(exception)
                msg.setWindowTitle("Warning")
                msg.setText("No internet connection.")
                msg.exec_()
            except Exception as error:
                print(error)
            try:
                if self.json_statusCode == 200:
                    self.userToken = self.json_response['token']
                    if self.json_response["is_doctor"] == False :
                        self.PatientloginAcceptedSignal.emit()
                    else:
                        self.DoctorloginAcceptedSignal.emit()

                elif self.json_statusCode == 401:
                    msg.setWindowTitle("Warning")
                    msg.setText("username or password was incorrect")
                    msg.exec_()
                else:
                    msg.setWindowTitle("Warning")
                    msg.setText(str(self.user_check['Error']))
                    msg.exec_()

            except Exception as x:
                msg.setWindowTitle("Warning")
                msg.setText(str(x))
                msg.exec_()
    def clear(self):
        self.username_lin.setText("")
        self.password_lin.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Login_Manager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()