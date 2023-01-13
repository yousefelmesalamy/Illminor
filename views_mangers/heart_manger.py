from views import heart_model
from PyQt5 import QtWidgets
import requests
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class Heart_MANGER(QtWidgets.QWidget, heart_model.Ui_Form):
    def __init__(self):
        super(Heart_MANGER, self).__init__()
        self.setupUi(self)
        self.base_url = ''
        self.token = ''
        self.show_result_btn_2.clicked.connect(self.run)
    def run(self):
        try :
            self.test_url = f"{self.base_url}/heartTest/"

            age = int(self.age_sb.text())
            sex = self.sex_comboBox.currentText()
            if sex == "Male" :
                sex = 0
            else:
                sex = 1

            cp = float(self.cp_sb.text())
            trestbps = float(self.trestbps_sb.text())
            chol = float(self.chol_sb.text())
            fbs = float(self.fbs_sb.text())
            restecg = float(self.restecg_sb.text())
            thalach = float(self.thalach_sb.text())
            exang = float(self.exang_sb.text())
            oldpeak = float(self.oldpeak_sb.text())
            slope = float(self.slope_sb.text())
            ca = float(self.ca_sb.text())
            thal = float(self.thal_sb.text())

        except Exception as param_errors :
            print("param errors",param_errors)

        try :

            data = {

                "age":age,
                "sex":sex,
                "cp": cp,
                "trestbps":trestbps,
                "chol":chol,
                "fbs":fbs,
                "restecg":restecg,
                "thalach":thalach,
                "exang":exang,
                "oldpeak":oldpeak,
                "slope":slope,
                "ca":ca,
                "thal":thal,
            }
            headers = {"Accept":"application/json ; indent=4",
                       "Content-Type":"application/json", "Authorization":f"Token {self.token}"}

            try :
                response = requests.post(self.test_url, json=data, headers=headers)
                print(response.json())
            except Exception as e :
                print(e)
        except Exception as x :
            print(x)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = Heart_MANGER()
    window.show()
    app.exec_()
