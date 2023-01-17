from views import blood_model
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
import requests


class Blood_MANGER(QtWidgets.QWidget, blood_model.Ui_Form):
    acceptedSignal = pyqtSignal()
    def __init__(self):
        super(Blood_MANGER, self).__init__()
        self.setupUi(self)
        self.base_url = ""
        self.token = ""
        self.show_result_btn.clicked.connect(self.run)

    def run(self):
        msg = QtWidgets.QMessageBox()
        msg.setStyleSheet("min-width: 10em; ")
        try :
            self.blood_url = f"{self.base_url}/bloodTest/"
            age = int(self.age_lin.text())
            bmi = float(self.bmi_sb.text())
            glucouse = float(self.glucouse_sb.text())
            insuline = float(self.insuline_sb.text())
            homa = float(self.homa_sb.text())
            leptin = float(self.leptin_sb.text())
            adiponcetin = float(self.adiponcetin_sb.text())
            resistiin = float(self.resistiin_sb.text())
            mcp = float(self.mcp_sb.text())
        except Exception as param_errors :
            print("param errors",param_errors)

        try :

            data = {
                "age":age,
                "bmi": bmi,
                "glucouse":glucouse,
                "insuline":insuline,
                "homa":homa,
                "leptin":leptin,
                "adiponcetin":adiponcetin,
                "resistiin":resistiin,
                "mcp":mcp,
            }
            headers = {"Accept":"application/json ; indent=4",
                       "Content-Type":"application/json", "Authorization":f"Token {self.token}"}

            try :
                response = requests.post(self.blood_url, json=data, headers=headers)
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
    window = Blood_MANGER()
    window.show()
    app.exec_()
