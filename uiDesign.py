'''uiDesign module for Data/Ia Dev Script -- Nicolas Autexier -- contact = nicolas.atx@gmx.fr '''
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import ress_rc


class Ui_MoviesPredictor(object):
    
    def setupUi(self, MoviesPredictor):
        MoviesPredictor.setObjectName("MoviesPredictor")
        MoviesPredictor.resize(954, 819)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        MoviesPredictor.setFont(font)
        self.lineEdit_7 = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 430, 375, 44))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit_8.setGeometry(QtCore.QRect(470, 490, 375, 44))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit_9.setGeometry(QtCore.QRect(470, 550, 375, 44))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit_10.setGeometry(QtCore.QRect(470, 610, 375, 44))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit_11.setGeometry(QtCore.QRect(470, 680, 375, 44))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.PredButton = QtWidgets.QPushButton(MoviesPredictor)
        self.PredButton.setGeometry(QtCore.QRect(530, 20, 271, 111))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.PredButton.setFont(font)
        self.PredButton.setStyleSheet("font: 14pt \"Cooper Black\";\n"
        "text-decoration: underline;")
        self.PredButton.setObjectName("PredButton")
        self.Result = QtWidgets.QLabel(MoviesPredictor)
        self.Result.setGeometry(QtCore.QRect(600, 140, 211, 171))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Result.setFont(font)
        self.Result.setToolTipDuration(-6)
        self.Result.setObjectName("Result")
        self.Title = QtWidgets.QTextEdit(MoviesPredictor)
        self.Title.setEnabled(True)
        self.Title.setGeometry(QtCore.QRect(12, 12, 491, 311))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.lineEdit_3 = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 360, 375, 44))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 430, 375, 44))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit.setGeometry(QtCore.QRect(10, 490, 375, 44))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 550, 375, 44))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 610, 375, 44))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(MoviesPredictor)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 680, 375, 44))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(MoviesPredictor)
        QtCore.QMetaObject.connectSlotsByName(MoviesPredictor)

    def retranslateUi(self, MoviesPredictor):
        _translate = QtCore.QCoreApplication.translate
        MoviesPredictor.setWindowTitle(_translate("MoviesPredictor", "Movies Predictor"))
        self.lineEdit_7.setText(_translate("MoviesPredictor", "Enter Director"))
        self.lineEdit_8.setText(_translate("MoviesPredictor", "Enter People"))
        self.lineEdit_9.setText(_translate("MoviesPredictor", "Enter Produceur"))
        self.lineEdit_10.setText(_translate("MoviesPredictor", "Enter Country"))
        self.lineEdit_11.setText(_translate("MoviesPredictor", "Enter Writer"))
        self.PredButton.setText(_translate("MoviesPredictor", "Make Prediction"))
        self.Result.setText(_translate("MoviesPredictor", "0.5"))
        self.Title.setHtml(_translate("MoviesPredictor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Cooper Black\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/logo/10501.png\" /></p></body></html>"))
        self.lineEdit_3.setText(_translate("MoviesPredictor", "Enter Title"))
        self.lineEdit_2.setText(_translate("MoviesPredictor", "Enter Synopsis"))
        self.lineEdit.setText(_translate("MoviesPredictor", "Enter Rating"))
        self.lineEdit_4.setText(_translate("MoviesPredictor", "Enter Genre"))
        self.lineEdit_5.setText(_translate("MoviesPredictor", "Enter Duration"))
        self.lineEdit_6.setText(_translate("MoviesPredictor", "Enter Release date"))
        self.PredButton.clicked.connect(self.singlePrediction)

    def singlePrediction(self):
        _translate = QtCore.QCoreApplication.translate
        self.Result.setText(_translate("MoviesPredictor", "Working on prediction"))
        from biglearn import singlePredProd as SP
        
        model_id = "model/5e09292b3514cd286f01ece4"

        array_to_send = [self.lineEdit_3.text(),self.lineEdit_2.text(),self.lineEdit.text(),self.lineEdit_4.text(),self.lineEdit_5.text(),
                         self.lineEdit_6.text(),self.lineEdit_7.text(),self.lineEdit_8.text(),self.lineEdit_9.text(),self.lineEdit_10.text(),
                         self.lineEdit_11.text()]

        pred_value = SP.singlePred(model_id,array_to_send)

        self.Result.setText(_translate("MoviesPredictor", f"{round(pred_value,2)}"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MoviesPredictor = QtWidgets.QWidget()
    ui = Ui_MoviesPredictor()
    ui.setupUi(MoviesPredictor)
    MoviesPredictor.show()
    sys.exit(app.exec_())
