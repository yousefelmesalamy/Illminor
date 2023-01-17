from views import breast_model
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import requests
import keras
import cv2
import os

class BREAST_MANGER(QtWidgets.QWidget, breast_model.Ui_Form):
    def __init__(self):
        super(BREAST_MANGER, self).__init__()
        self.setupUi(self)
        self.base_url= ""
        self.token=""
        self.show_result_btn.clicked.connect(self.run)
        # self.back_btn_2.clicked.connect(self.checker)
        self.pickProfile_lbl.mousePressEvent = self.getfiles
        self.msg = QtWidgets.QMessageBox()

    def getfiles(self , event):

        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', '', 'Images (*.png, *.jpeg , *.jpg) ')
        try :
            if len(self.fileName) >5 :
                image = QtGui.QImage(self.fileName)
                self.pickProfile_lbl.setPixmap(QtGui.QPixmap(image).scaled(400,400,QtCore.Qt.KeepAspectRatio))
            else:
                self.msg.setIcon(self.msg.Critical)
                self.msg.setWindowTitle("Alert")
                self.msg.setText("Please Select The X-Ray")
                self.msg.exec_()

        except Exception as e :
            print(e)
    def run(self):
        test_url = f"{self.base_url}/chestTest/"
        headers = {"Accept": "application/json ; indent=4",
                   "Content-Type": "application/json", "Authorization": f"Token {self.token}"}
        try :
            result = self.model_predict(self.fileName)
            data = {"result": result}
        except Exception as e :
            print(e)
            self.msg.setIcon(self.msg.Critical)
            self.msg.setWindowTitle("Alert")
            self.msg.setText("please select valid x-ray")
            self.msg.exec_()

        try:
            response = requests.post(test_url, json=data, headers=headers)
            if response.status_code == 200 :
                self.msg.setIcon(self.msg.Information)
                self.msg.setWindowTitle("Information")
                self.msg.setText(str(response.json()["response"]))
                self.msg.exec_()
            else:
                self.msg.setIcon(self.msg.Critical)
                self.msg.setWindowTitle("Error")
                self.msg.setText(str(response.json()["response"]))
                self.msg.exec_()
        except Exception as e :
            print(e)

    def model_predict(self,image_path):
        # os.path.join("model","chestExploration.hdf5")
        modedl_path = os.path.join("model","chestExploration.hdf5")
        model = keras.models.load_model(modedl_path)
        gray_image = cv2.imread(image_path, 0)
        resized_image = cv2.resize(gray_image, (100, 100))
        scaled_image = resized_image.astype("float32") / 255.0
        sample_batch = scaled_image.reshape(1, 100, 100, 1)  # 1 image, 100, 100 dim , 1 no of chanels
        result = model.predict(sample_batch)
        result[result >= 0.5] = 1  # Normal
        result[result < 0.5] = 0  # Pneimonia
        if result[0][0] == 1:
            result = "Normal"
        else:
            result = "Pneimonia"
        return result

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = BREAST_MANGER()
    window.show()
    app.exec_()
