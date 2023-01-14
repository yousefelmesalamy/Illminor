from PyQt5 import QtWidgets , QtCore
from views import register_view
from PyQt5 import QtGui

from PyQt5.QtGui import QPixmap

import json
import requests
import os
class Register_Manager(QtWidgets.QWidget, register_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(Register_Manager, self).__init__()
        self.setupUi(self)

        self.siginup_btn_4.clicked.connect(self.run)
        self.base_url = ""
        self.userToken = ''
        self.is_doctor = False
        # pixmap = QPixmap("")
        # self.profile_picture_lbl.setPixmap(pixmap)
        self.profile_picture_lbl_4.mousePressEvent = self.getfiles


    def getfiles(self , event):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '', 'Images (*.png, *.jpeg , *.jpg) ')
        try :
            self.image = QtGui.QImage(self.fileName)
            self.profile_picture_lbl.setPixmap(QtGui.QPixmap(self.image).scaled(150,150))
        except Exception as e :
            print(e)

    def run(self):
        try :
            self.register_url = f"{self.base_url}/users"

            username = (self.username_lin.text())
            first_name = (self.first_name_lin.text())
            last_name = (self.last_name_lin.text())
            name = (self.name_lin.text())
            email = (self.email_lin.text())
            bio = self.bio_lin.toPlainText()
            phone_number = self.phone_number_lin.text()
            gander = self.gander_combobox.currentText()
            if gander == "Male":
                sex = 0
            else:
                sex = 1
            age = float(self.age_sb.text())
            password2 = (self.password2_lin.text())
            password1 = (self.password1_lin.text())
        except Exception as ww:
            print(ww)

        try :

            data = {
                "username":username,
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
            headers = {"Accept":"application/json ; indent=4","Content-Type":"application/json"}
            try :
                files = [
                    ('profile_picture', (self.fileName, open(self.fileName, 'rb').read(), 'image/jpeg'))
                ]
            except Exception as RRR :
                print(RRR)
            try :
                response = requests.post(self.register_url, json=data, files=files, headers=headers)
                print(response.json())
            except Exception as e:
                print(e)
        except Exception as x:
            print(x)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Register_Manager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()