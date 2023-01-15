from PyQt5 import QtWidgets , QtCore
from views import register_view
from PyQt5 import QtGui

from PyQt5.QtGui import QPixmap

import json
import requests
import os
class Register_Manager(QtWidgets.QWidget, register_view.Ui_Form):
    signupAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(Register_Manager, self).__init__()
        self.setupUi(self)
        self.siginup_btn_4.clicked.connect(self.run)
        self.base_url = ""
        self.userToken = ''
        self.is_doctor = False
        self.profile_picture_lbl_4.mousePressEvent = self.getfiles

    def getfiles(self , event):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '', 'Images (*.png, *.jpeg , *.jpg) ')
        try :
            self.image = QtGui.QImage(self.fileName)
            self.profile_picture_lbl_4.setPixmap(QtGui.QPixmap(self.image).scaled(150,150))
        except Exception as e:
            print(e)

    def run(self):
        msg = QtWidgets.QMessageBox()
        headers = {"Accept":"application/json ; indent=4"}
        try :
            self.register_url = f"{self.base_url}/users/"

            username = self.username_lin_4.text()
            first_name = self.first_name_lin_4.text()
            last_name = self.last_name_lin_4.text()
            name = self.name_lin_4.text()
            email = self.email_lin_4.text()
            bio = self.bio_lin_4.toPlainText()
            phone_number = self.phone_number_lin_4.text()
            gander = self.gander_combobox_4.currentText()
            if gander == "Male":
                sex = 0
            else:
                sex = 1
            age = self.age_sb_4.text()
            password2 = (self.password2_lin_4.text())
            password1 = (self.password1_lin_4.text())
        except Exception as ww:
            print("labels error", ww)

        try :
            data = {
                'username':username,
                "first_name":first_name,
                "last_name":last_name,
                "name":name,
                "email":email,
                "bio":bio,
                "phone_number":phone_number,
                "gander":gander,
                "age":age,
                "password2":password2,
                "password1":password1,
                "is_doctor":self.is_doctor,
            }
        except Exception as x:
            print("data error",x)
        try :
            files = [
                ('profile_picture', (self.fileName, open(self.fileName, 'rb').read(), 'image/jpeg'))
            ]
        except Exception as RRR :
            print("file_error",RRR)
        try :
            response = requests.post(self.register_url, data=data, files=files, headers=headers)
            if response.status_code == 201:
                msg.setWindowTitle("Successfully")
                msg.setText("Successfully Registered \n You Can Log in Now")
                msg.exec_()
                self.signupAcceptedSignal.emit()
            else:
                msg.setWindowTitle("Warning")
                msg.setText(str(response.json()["Response"]))
                msg.exec_()

        except Exception as e:
            print("response error",e)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Register_Manager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()