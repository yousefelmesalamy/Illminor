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
        msg = QtWidgets.QMessageBox()
        msg.setStyleSheet("min-width: 10em; ")
        try :
            self.test_url = f"{self.base_url}/heartTest/"

            Age = int(self.Age_sb.text())

            Sex = self.Sex_combobox.currentText()
            if Sex == "Male":
                Sex = 0
            else:
                Sex = 1
            ChestPainType = float(self.ChestPainType_sb.text())
            Cholesterol = float(self.Cholesterol_sb.text())
            FastingBS = float(self.FastingBS_sb.text())
            MaxHR = float(self.MaxHR_sb.text())
            ExerciseAngina = float(self.ExerciseAngina_sb.text())
            Oldpeak = float(self.Oldpeak_sb.text())
            ST_Slope = float(self.ST_Slope_sb.text())


        except Exception as param_errors :
            print("param errors",param_errors)

        try :

            data = {

                "Age":Age,
                "Sex":Sex,
                "Cholesterol": Cholesterol,
                "ChestPainType":ChestPainType,
                "FastingBS":FastingBS,
                "MaxHR":MaxHR,
                "ExerciseAngina":ExerciseAngina,
                "ST_Slope":ST_Slope,
                "Oldpeak":Oldpeak,

            }
            headers = {"Accept":"application/json ; indent=4",
                       "Content-Type":"application/json", "Authorization":f"Token {self.token}"}

            try :
                response = requests.post(self.test_url, json=data, headers=headers)
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
    window = Heart_MANGER()
    window.show()
    app.exec_()
