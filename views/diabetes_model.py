# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/diabetes_model.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1066, 744)
        Form.setStyleSheet("\n"
"font-family:Ubuntu;\n"
"font-size: 20px;\n"
"    color:black;\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.back_btn = QtWidgets.QPushButton(Form)
        self.back_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.back_btn.setMaximumSize(QtCore.QSize(60, 60))
        self.back_btn.setStyleSheet("QPushButton {\n"
"    background-color:rgba(6,103,184,255);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #827397;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-postion:calc(100% - 10px) center;}\n"
"")
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICONS/icons/back-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(30, 30))
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout_2.addWidget(self.back_btn, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(391, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 6, 5, 1, 2)
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setStyleSheet("background-color: rgb(85, 255, 127,0);\n"
"font-size:40px")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 0, 2, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(310, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 96, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 7, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 5, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(389, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 6, 0, 1, 3)
        self.show_result_btn = QtWidgets.QPushButton(Form)
        self.show_result_btn.setMinimumSize(QtCore.QSize(250, 50))
        self.show_result_btn.setMaximumSize(QtCore.QSize(330, 50))
        self.show_result_btn.setStyleSheet("QPushButton {\n"
"    background-color:rgba(6,103,184,255);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #827397;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-postion:calc(100% - 10px) center;}\n"
"")
        self.show_result_btn.setObjectName("show_result_btn")
        self.gridLayout_2.addWidget(self.show_result_btn, 6, 3, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(242, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(330, 450))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(" border-color:transparent;\n"
"background-color:transparent;")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.Age_SB = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Age_SB.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.Age_SB.setObjectName("Age_SB")
        self.horizontalLayout_7.addWidget(self.Age_SB)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.glucose_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.glucose_sb.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.glucose_sb.setObjectName("glucose_sb")
        self.horizontalLayout_6.addWidget(self.glucose_sb)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.bloodpressure_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.bloodpressure_sb.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.bloodpressure_sb.setObjectName("bloodpressure_sb")
        self.horizontalLayout_5.addWidget(self.bloodpressure_sb)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.skinthickness_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.skinthickness_sb.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.skinthickness_sb.setObjectName("skinthickness_sb")
        self.horizontalLayout_4.addWidget(self.skinthickness_sb)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.insulin_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.insulin_sb.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.insulin_sb.setObjectName("insulin_sb")
        self.horizontalLayout_3.addWidget(self.insulin_sb)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bmi_lin = QtWidgets.QLabel(self.groupBox)
        self.bmi_lin.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.bmi_lin.setObjectName("bmi_lin")
        self.horizontalLayout_2.addWidget(self.bmi_lin)
        self.bmi_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.bmi_sb.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.bmi_sb.setObjectName("bmi_sb")
        self.horizontalLayout_2.addWidget(self.bmi_sb)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.dpf_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.dpf_sb.setStyleSheet("background-color: rgb(119, 118, 123,0);\n"
"  cursor: pointer;\n"
"  float: right;\n"
"  padding: 5px 20px;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
"")
        self.dpf_sb.setObjectName("dpf_sb")
        self.horizontalLayout.addWidget(self.dpf_sb)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 3, 2, 2, 4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_25.setText(_translate("Form", "CHECK DIABETES"))
        self.show_result_btn.setText(_translate("Form", "Show result"))
        self.label.setText(_translate("Form", "Age"))
        self.label_3.setText(_translate("Form", "glucose"))
        self.label_4.setText(_translate("Form", "bloodpressure"))
        self.label_5.setText(_translate("Form", "skinthickness"))
        self.label_6.setText(_translate("Form", "insulin"))
        self.bmi_lin.setText(_translate("Form", "bmi"))
        self.label_8.setText(_translate("Form", "dpf"))
import app_resources_rc
