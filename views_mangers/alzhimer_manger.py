from views import alzhimer_model
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
import requests

# response = requests.get(http://illacc.pythonanywhere.com/alzheimer")
class Alzahimer_MANGER(QtWidgets.QWidget, alzhimer_model.Ui_Form):
    def __init__(self):

        super(Alzahimer_MANGER, self).__init__()
        self.setupUi(self)
        self.base_url = ''
        self.token = ''
        self.show_result_btn.clicked.connect(self.run)
    def run(self):
        msg = QtWidgets.QMessageBox()
        msg.setStyleSheet("min-width: 10em; ")
        try :
            self.test_url = f"{self.base_url}/alzhimarTest/"

            Age = int(self.Age_sb.text())
            gender = self.gender_comboBox.currentText()
            if gender == "Male":
                gender = 0
            else:
                gender = 1

            EDUC = self.EDUC_sb.text()
            SES = self.SES_sb.text()
            MMSE = self.MMSE_sb.text()
            eTIV = self.eTIV_sb.text()
            nWBV = self.nWBV_sb.text()
            ASF = self.ASF_sb.text()
        except Exception as param_errors :
            print("param errors",param_errors)

        try :

            data = {
                "gender": gender,
                "Age":Age,
                "EDUC":EDUC,
                "SES":SES,
                "MMSE":MMSE,
                "eTIV":eTIV,
                "nWBV":nWBV,
                "ASF":ASF,

            }
            headers = {"Accept":"application/json ; indent=4",
                       "Content-Type":"application/json", "Authorization":f"Token {self.token}"}

            try:
                response = requests.post(self.test_url, json=data, headers=headers)
                msg.setIcon(msg.Information)
                msg.setWindowTitle("Information")
                msg.setText(str(response.json()["response"]))
                msg.exec_()
            except Exception as e:
                print(e)
        except Exception as x:
            print(x)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = Alzahimer_MANGER()
    window.show()
    app.exec_()
