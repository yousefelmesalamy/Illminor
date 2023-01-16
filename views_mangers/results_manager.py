from views import results_view
from PyQt5 import QtWidgets
import requests
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *



class RESULTS_MANAGER(QtWidgets.QWidget, results_view.Ui_Form):
    def __init__(self):
        super(RESULTS_MANAGER, self).__init__()
        self.setupUi(self)
        self.base_url = "https://illacc.pythonanywhere.com"
        self.token = "ad144b2560cc077fe1dd116d8c007c09c80aeac4"
        self.run()


    def run(self):
        # self.tableWidget.setRowCount(0)
        table_headers = ['patient', 'blood test', 'diabtes test', 'parkinson test', 'alzhimar test', 'heart test']
        self.tableWidget.setHorizontalHeaderLabels(table_headers)

        self.result_url = f"{self.base_url}/users/"
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        try:
            self.reply = requests.get(self.result_url , headers=headers).json()
            # print(self.reply)
        except Exception as s :
            print("ss",s)

        rowPosition = self.tableWidget.rowCount()
        for rows in self.reply['results'] :

            try:
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(0, 0, QTableWidgetItem(rows['user']))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(rows['bloodTest_model']))
                self.tableWidget.setItem(0, 2, QTableWidgetItem(rows['diabtesTest_model']))
                self.tableWidget.setItem(0, 3, QTableWidgetItem(rows['parkinsonTest_model']))
                self.tableWidget.setItem(0, 4, QTableWidgetItem(rows['alzhimarTest_model']))
                self.tableWidget.setItem(0, 5, QTableWidgetItem(rows['heartTest_model']))
            except Exception as e:
                print('QTableWidgetItem Error', e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = RESULTS_MANAGER()
    window.show()
    app.exec_()

