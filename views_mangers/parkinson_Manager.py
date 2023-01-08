from PyQt5 import QtWidgets, QtCore
from views import parkinson_molde
import json
import requests
import os


class Parkinson_Mnager(QtWidgets.QWidget, parkinson_molde.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(Parkinson_Mnager, self).__init__()
        self.setupUi(self)

        self.loginAcceptedSignal.emit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Parkinson_Mnager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()