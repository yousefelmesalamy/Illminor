from views import results_view
from PyQt5 import QtWidgets
import requests
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class RESULTS_MANAGER(QtWidgets.QWidget, results_view.Ui_Form):
    def __init__(self):
        super(RESULTS_MANAGER, self).__init__()
        self.setupUi(self)
        self.run()
        self.base_url = ''
        self.token = ''
        self.user = '' #copy
        self.test_url = f"{self.base_url}/users/"
        # self.tableWidget.verticalHeader().setVisible() #copy
        # self.user = -1
        # self.tableWidget.selectionModel().selectionChanged.connect(self.uers) # عطلان
    def run(self):
        self.tableWidget.setRowCount(0)
        msg = QtWidgets.QMessageBox()
        headers = {"Accept": "application/json ; indent=4","Content-Type": "application/json", "Authorization"
        : f"Token {self.token}"}
        try:

            self.reply = requests.get(self.base_url, headers=headers).json()
        except Exception as s:
            print("ss", s)

        rowPosition = self.tableWidget.rowCount()
        for rows in self.reply:
            try:

                self.tableWidget.insertRow(rowPosition)
                # [{'id': 1, 'product_name': 'testP', 'user_name': 'mok11', 'quantity': 5, 'acceptable_by': 'not accepted', 'user_id': 2}]

                self.tableWidget.setItem(0, 0, QTableWidgetItem(str(rows['user'])))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(str(rows['breast_model'])))
                self.tableWidget.setItem(0, 2, QTableWidgetItem(str(rows['bloodTest_model'])))
                self.tableWidget.setItem(0, 3, QTableWidgetItem(str(rows['diabtesTest_model'])))
                self.tableWidget.setItem(0, 4, QTableWidgetItem(str(rows['parkinsonTest_model'])))
                self.tableWidget.setItem(0, 5, QTableWidgetItem(str(rows['alzhimarTest_model'])))
                self.tableWidget.setItem(0, 6, QTableWidgetItem(str(rows['heartTest_model'])))

                try:

                    response = requests.post(self.test_url, json=rows, headers=headers)

                    print(response.json())

                except Exception as e:

                    print(e)

            except Exception as x:

                print(x)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = RESULTS_MANAGER()
    window.show()
    app.exec_()
