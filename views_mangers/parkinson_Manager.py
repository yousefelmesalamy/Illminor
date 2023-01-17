from PyQt5 import QtWidgets, QtCore
from views import parkinson_molde
import json
import requests
import os

class Parkinson_Mnager(QtWidgets.QWidget, parkinson_molde.Ui_Form):
    def __init__(self):
        super(Parkinson_Mnager, self).__init__()
        self.setupUi(self)

        self.base_url = ''
        self.token = ''
        self.show_result_btn.clicked.connect(self.run)

    def run(self):
        msg = QtWidgets.QMessageBox()
        try:
            self.test_url = f"{self.base_url}/parkinsonTest/"

            MDVP_Fo_Hz = float(self.MDVP_Fo_Hz_sb.text())
            MDVP_Fhi_Hz = float(self.MDVP_Fhi_Hz_sb.text())
            MDVP_Flo_Hz = float(self.MDVP_Flo_Hz_sb.text())
            MDVP_Jitter = float(self.MDVP_Jitter_sb.text())
            MDVP_Jitter_Abs = float(self.MDVP_Jitter_Abs_sb.text())
            MDVP_RAP = float(self.MDVP_RAP_sb.text())
            MDVP_PPQ = float(self.MDVP_PPQ_sb.text())
            Jitter_DDP = float(self.Jitter_DDP_sb.text())
            MDVP_Shimmer = float(self.MDVP_Shimmer_sb.text())
            MDVP_Shimmer_dB = float(self.MDVP_Shimmer_dB_sb.text())
            Shimmer_APQ3 = float(self.Shimmer_APQ3_sb.text())
            Shimmer_APQ5 = float(self.Shimmer_APQ5_sb.text())
            MDVP_APQ = float(self.MDVP_APQ_sb.text())
            Shimmer_DDA = float(self.Shimmer_DDA_sb.text())
            NHR = float(self.NHR_sb.text())
            HNR = float(self.HNR_sb.text())
            RPDE = float(self.RPDE_sb.text())
            DFA = float(self.DFA_sb.text())
            spread1 = float(self.spread1_sb.text())
            spread2 = float(self.spread2_sb.text())
            D2 = float(self.D2_sb.text())
            PPE = float(self.PPE_sb.text())


        except Exception as param_errors:
            print("param errors", param_errors)

        try:

            data = {
                "MDVP_Fo_Hz": MDVP_Fo_Hz,
                "MDVP_Fhi_Hz": MDVP_Fhi_Hz,
                "MDVP_Flo_Hz": MDVP_Flo_Hz,
                "MDVP_Jitter":MDVP_Jitter,
                "MDVP_Jitter_Abs": MDVP_Jitter_Abs,
                "MDVP_RAP": MDVP_RAP,
                "MDVP_PPQ": MDVP_PPQ,
                "Jitter_DDP": Jitter_DDP,
                "MDVP_Shimmer": MDVP_Shimmer,
                "MDVP_Shimmer_dB": MDVP_Shimmer_dB,
                "Shimmer_APQ3": Shimmer_APQ3,
                "Shimmer_APQ5": Shimmer_APQ5,
                "MDVP_APQ": MDVP_APQ,
                "Shimmer_DDA": Shimmer_DDA,
                "NHR": NHR,
                "HNR": HNR,
                "RPDE": RPDE,
                "DFA": DFA,
                "spread1": spread1,
                "spread2": spread2,
                "D2": D2,
                "PPE": PPE,

            }
            headers = {"Accept": "application/json ; indent=4",
                       "Content-Type": "application/json", "Authorization": f"Token {self.token}"}

            try:
                response = requests.post(self.test_url, json=data, headers=headers)
                msg.setIcon(msg.Information)
                msg.setWindowTitle("Information")
                msg.setText(str(response.json()["response"]))
                msg.exec_()
            except Exception as e:
                print(e)
        except Exception as x:
            print(x)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Parkinson_Mnager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()