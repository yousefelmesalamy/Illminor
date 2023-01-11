from PyQt5 import QtWidgets, QtCore
from views import profileClient
import json
import requests
import os

class PROFILE_CLIENT_Mnager(QtWidgets.QWidget, profileClient.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(PROFILE_CLIENT_Mnager, self).__init__()
        self.setupUi(self)

        self.loginAcceptedSignal.emit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = PROFILE_CLIENT_Mnager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()