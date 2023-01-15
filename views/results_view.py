# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/results_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1487, 464)
        Form.setStyleSheet("background-color: rgb(239, 243, 252);\n"
"color: rgb(18, 32, 62);\n"
"font-family:Ubuntu;\n"
"font-size: 20px;")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(1251, 350))
        self.tableWidget.setMaximumSize(QtCore.QSize(1251, 350))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(26)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.gridLayout.addWidget(self.tableWidget, 2, 2, 2, 2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMaximumSize(QtCore.QSize(135, 16777215))
        font = QtGui.QFont()
        font.setFamily("arow")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(239, 243, 252,0);\n"
"font-family:arow;\n"
"font-size:30px;\n"
"color:rgb(18,32,62,255);\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.back_btn = QtWidgets.QPushButton(Form)
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICONS/icons/back-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(50, 50))
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout.addWidget(self.back_btn, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Form", "12"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Form", "13"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Form", "14"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Form", "15"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Form", "16"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Form", "17"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Form", "19"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Form", "20"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("Form", "21"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("Form", "22"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("Form", "23"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("Form", "24"))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("Form", "25"))
        item = self.tableWidget.verticalHeaderItem(23)
        item.setText(_translate("Form", "26"))
        item = self.tableWidget.verticalHeaderItem(24)
        item.setText(_translate("Form", "28"))
        item = self.tableWidget.verticalHeaderItem(25)
        item.setText(_translate("Form", "30"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "user"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "bloodTest_model"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "diabtesTest_model"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "parkinsonTest_model"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "alzhimarTest_model"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "heartTest_model"))
        self.label_4.setText(_translate("Form", "Results"))
import app_resources_rc
