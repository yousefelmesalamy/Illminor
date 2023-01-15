from PyQt5 import QtWidgets, QtCore
from views import profileClient
import json
import requests
import os
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPainterPath , QBrush
from PyQt5.QtCore import Qt


class PROFILE_CLIENT_Mnager(QtWidgets.QWidget, profileClient.Ui_Form):
    def __init__(self):
        super(PROFILE_CLIENT_Mnager, self).__init__()
        self.setupUi(self)
        self.base_url = ""
        self.username=""
        self.token = ""
        self.firstTime = True



    def run(self):
        msg = QtWidgets.QMessageBox()
        headers = {"Accept": "application/json ; indent=4",
                   "Content-Type": "application/json", "Authorization": f"Token {self.token}"}

        query_url = f"{self.base_url}/users/?user__username={self.username}"
        response = requests.get(query_url, headers=headers)
        statusCode_response = response.status_code

        if statusCode_response == 200 :
            json_response= response.json()
            data = json_response["results"][0]
            self.set_profileData(data)
            self.results_lbl(data)
            self.set_Picture(data)
            self.firstTime = False
        else:
            msg.setIcon(msg.critical)
            msg.setWindowTitle("Warning")
            msg.setText("Something want wrong !")
            msg.exec_()

    def set_profileData(self, response):
        username = response["user"]
        name = response["name"]
        email = response["email"]
        gander = response["gander"]
        phone_number = response["phone_number"]
        bio = response["bio"]
        is_doctor = response["is_doctor"]
        if is_doctor == True:
            is_doctor = "Doctor"
        else:
            is_doctor = "Patient"
        self.user_name_lbl.setText(username)
        self.name_lbl.setText(name)
        self.email_lbl.setText(email)
        self.gender_lbl.setText(gander)
        self.userdoctor_lbl.setText(is_doctor)
        self.phone_lbl.setText(phone_number)
        self.bio_lbl.setText(bio)

    def set_Picture(self, response):
        profilePic= response["profile_picture"]
        profile_Picture = QImage()
        profile_Picture.loadFromData(requests.get(profilePic).content)
        self.profile_lbl.setPixmap(QPixmap(profile_Picture).scaled(600, 600, QtCore.Qt.KeepAspectRatio))

    def results_lbl(self,response):
        bloodTest_model=response["bloodTest_model"]
        diabtesTest_model=response["diabtesTest_model"]
        parkinsonTest_model=response["parkinsonTest_model"]
        alzhimarTest_model=response["alzhimarTest_model"]
        heartTest_model=response["heartTest_model"]
        # chestTest_model=response["chestTest_model"]
        if bloodTest_model != None :
            self.bloodResult_lbl.setText("bloodTest_model")
        if diabtesTest_model != None :
            self.diabtesResult_lbl.setText("diabtesTest_model")
        if parkinsonTest_model != None :
            self.parkinsonResult_lbl.setText("parkinsonTest_model")
        if alzhimarTest_model != None :
            self.alzhimarResult_lbl.setText("alzhimarTest_model")
        if heartTest_model != None :
            self.heartResult_lbl.setText("heartTest_model")
        # if chestTest_model != None :
        #     self.chestResult_lbl.setText("chestTest_model")



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = PROFILE_CLIENT_Mnager()
    w.show()
    app.exec_()