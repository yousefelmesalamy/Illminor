from PyQt5 import QtWidgets , QtCore
from views import register_view
import json
import requests
import os
class Register_Manager(QtWidgets.QWidget, register_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(Register_Manager, self).__init__()
        self.setupUi(self)

        self.siginup_btn.clicked.connect(self.run)
        self.base_url = ""
        self.userToken = ''
        self.is_doctor = False


    def run(self):
        self.register_url = f"{self.base_url}/users"


        try :

            data = {
                "age":age,
                "glucose":glucose,
                "bloodpressure":bloodpressure,
                "skinthickness":skinthickness,
                "insulin":insulin,
                "bmi":bmi,
                "dpf":dpf,
                "pregnancies":pregnancies,
            }
            headers = {"Accept":"application/json ; indent=4",
                       "Content-Type":"application/json"}

            try :
                response = requests.post(self.register_url, json=data, headers=headers)
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