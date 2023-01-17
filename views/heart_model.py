# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/heart_model.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1022, 912)
        Form.setStyleSheet("background-color: rgb(239, 243, 252);\n"
"font-family:Ubuntu;\n"
"font-size: 20px;\n"
"    color:black;\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayout.addWidget(self.back_btn, 0, 0, 1, 1)
        self.show_result_btn_2 = QtWidgets.QPushButton(Form)
        self.show_result_btn_2.setMinimumSize(QtCore.QSize(250, 50))
        self.show_result_btn_2.setMaximumSize(QtCore.QSize(330, 50))
        self.show_result_btn_2.setStyleSheet("QPushButton {\n"
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
        self.show_result_btn_2.setObjectName("show_result_btn_2")
        self.gridLayout.addWidget(self.show_result_btn_2, 4, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(330, 450))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(" border-color:transparent;\n"
"background-color:transparent;")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)
        self.thalach_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.thalach_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.thalach_sb.setMaximum(99999999999.0)
        self.thalach_sb.setObjectName("thalach_sb")
        self.gridLayout_2.addWidget(self.thalach_sb, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.slope_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.slope_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.slope_sb.setObjectName("slope_sb")
        self.gridLayout_2.addWidget(self.slope_sb, 9, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 9, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 11, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.chol_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.chol_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.chol_sb.setMaximum(999999999999.0)
        self.chol_sb.setObjectName("chol_sb")
        self.gridLayout_2.addWidget(self.chol_sb, 4, 1, 1, 1)
        self.oldpeak_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.oldpeak_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.oldpeak_sb.setObjectName("oldpeak_sb")
        self.gridLayout_2.addWidget(self.oldpeak_sb, 12, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 12, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.restecg_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.restecg_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.restecg_sb.setObjectName("restecg_sb")
        self.gridLayout_2.addWidget(self.restecg_sb, 6, 1, 1, 1)
        self.thal_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.thal_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.thal_sb.setObjectName("thal_sb")
        self.gridLayout_2.addWidget(self.thal_sb, 11, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.trestbps_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.trestbps_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.trestbps_sb.setMaximum(9999999999.0)
        self.trestbps_sb.setObjectName("trestbps_sb")
        self.gridLayout_2.addWidget(self.trestbps_sb, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.fbs_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.fbs_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.fbs_sb.setObjectName("fbs_sb")
        self.gridLayout_2.addWidget(self.fbs_sb, 5, 1, 1, 1)
        self.pregnancies_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.pregnancies_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.pregnancies_sb.setObjectName("pregnancies_sb")
        self.gridLayout_2.addWidget(self.pregnancies_sb, 14, 1, 1, 1)
        self.ca_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.ca_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.ca_sb.setObjectName("ca_sb")
        self.gridLayout_2.addWidget(self.ca_sb, 10, 1, 1, 1)
        self.exang_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.exang_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.exang_sb.setObjectName("exang_sb")
        self.gridLayout_2.addWidget(self.exang_sb, 8, 1, 1, 1)
        self.sex_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.sex_comboBox.setMinimumSize(QtCore.QSize(0, 49))
        self.sex_comboBox.setStyleSheet("background:transparent;\n"
"  border-radius: 20px;\n"
"color:white    ;\n"
" border: 2px solid  #ffffff;\n"
"font-size:20px;\n"
"padding:15px;\n"
"\n"
"")
        self.sex_comboBox.setObjectName("sex_comboBox")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/male.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sex_comboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/female.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sex_comboBox.addItem(icon2, "")
        self.gridLayout_2.addWidget(self.sex_comboBox, 1, 1, 1, 1)
        self.cp_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.cp_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.cp_sb.setObjectName("cp_sb")
        self.gridLayout_2.addWidget(self.cp_sb, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 8, 0, 1, 1)
        self.age_sb = QtWidgets.QSpinBox(self.groupBox)
        self.age_sb.setStyleSheet("  height: 32px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #959595;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  width: 80px;\n"
"  outline: none;\n"
"\n"
"  caret-color: transparent;;\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #ABAFB7;\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 3px solid #555;\n"
"}\n"
"\n"
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
        self.age_sb.setObjectName("age_sb")
        self.gridLayout_2.addWidget(self.age_sb, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 10, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 14, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 2, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(389, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 3)
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setStyleSheet("background-color: rgb(85, 255, 127,0);\n"
"font-size:40px")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 0, 2, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(347, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 4, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(283, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(307, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 1, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.show_result_btn_2.setText(_translate("Form", "Show result"))
        self.label_8.setText(_translate("Form", "thalach"))
        self.label_6.setText(_translate("Form", "fbs"))
        self.label_2.setText(_translate("Form", "Gander"))
        self.label_9.setText(_translate("Form", "slope"))
        self.label_12.setText(_translate("Form", "thal"))
        self.label.setText(_translate("Form", "age"))
        self.label_26.setText(_translate("Form", "oldpeak"))
        self.label_4.setText(_translate("Form", "trestbps"))
        self.label_7.setText(_translate("Form", "restecg"))
        self.label_3.setText(_translate("Form", "cp"))
        self.sex_comboBox.setItemText(0, _translate("Form", "Male"))
        self.sex_comboBox.setItemText(1, _translate("Form", "Female"))
        self.label_10.setText(_translate("Form", "exang"))
        self.label_5.setText(_translate("Form", "chol"))
        self.label_11.setText(_translate("Form", "ca"))
        self.label_27.setText(_translate("Form", "pregnancies"))
        self.label_25.setText(_translate("Form", "HEART CHECK"))
import app_resources_rc
