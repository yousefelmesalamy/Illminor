import requests

from views import diabetes_model
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class Diabetes_MANGER(QtWidgets.QWidget, diabetes_model.Ui_Form):
    def __init__(self):
        super(Diabetes_MANGER, self).__init__()
        self.setupUi(self)
        self.base_url= ""
        self.token=""
        self.show_result_btn.clicked.connect(self.run)

    def run(self):
        msg = QtWidgets.QMessageBox()
        msg.setStyleSheet("min-width: 10em; ")

        diabetes_url = f"{self.base_url}/diabtesTest/"


        pregnancies = float(self.pregnancies_sb.text())
        age = int(self.Age_SB.text())
        glucose = float(self.glucose_sb.text())
        bloodpressure = float(self.bloodpressure_sb.text())
        skinthickness = float(self.skinthickness_sb.text())
        insulin = float(self.insulin_sb.text())
        bmi = float(self.bmi_sb.text())
        dpf = float(self.dpf_sb.text())

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
                       "Content-Type":"application/json", "Authorization":f"Token {self.token}"}

            try :
                response = requests.post(diabetes_url, json=data, headers=headers)
                msg.setIcon(msg.Information)
                msg.setWindowTitle("Information")
                msg.setText(str(response.json()["response"]))
                msg.exec_()
            except Exception as e :
                print(e)
        except Exception as x :
            print(x)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = Diabetes_MANGER()
    window.show()
    app.exec_()
