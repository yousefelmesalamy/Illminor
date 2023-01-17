from views import breast_model
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore

class BREAST_MANGER(QtWidgets.QWidget, breast_model.Ui_Form):
    acceptedSignal = pyqtSignal()
    def __init__(self):
        super(BREAST_MANGER, self).__init__()
        self.setupUi(self)
        self.back_btn_2.clicked.connect(self.checker)
        self.pickProfile_lbl.mousePressEvent = self.getfiles

    def getfiles(self , event):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '', 'Images (*.png, *.jpeg , *.jpg) ')
        try :
            image = QtGui.QImage(self.fileName)
            self.pickProfile_lbl.setPixmap(QtGui.QPixmap(image).scaled(400,400,QtCore.Qt.KeepAspectRatio))
            # self.file_path_lbl.setText(self.fileName)
            print(self.fileName)

        except Exception as e :
            print(e)

    def checker(self):
        self.acceptedSignal.emit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = BREAST_MANGER()
    window.show()
    app.exec_()
