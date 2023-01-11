from views import heart_model
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class Heart_MANGER(QtWidgets.QWidget, heart_model.Ui_Form):
    acceptedSignal = pyqtSignal()
    def __init__(self):
        super(Heart_MANGER, self).__init__()
        self.setupUi(self)

    def run(self):
        diabetes_url = self.base_url+"/diabetes"

        age = int(self.Age_SB.text())
        glucose = float(self.glucose_sb.text())
        bloodpressure = float(self.bloodpressure_sb.text())
        skinthickness = float(self.skinthickness_sb.text())
        insulin = float(self.insulin_sb.text())
        bmi = float(self.bmi_sb.text())
        dpf = float(self.dpf_sb.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = Heart_MANGER()
    window.show()
    app.exec_()
