from PyQt5 import QtWidgets, QtCore
from views import change_password
import json
import requests
import os

class CHANGE_PASSWORD_Mnager(QtWidgets.QWidget, change_password.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(CHANGE_PASSWORD_Mnager, self).__init__()
        self.setupUi(self)

        self.loginAcceptedSignal.emit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = CHANGE_PASSWORD_Mnager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()