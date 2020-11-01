# Ahmet Furkan DEMIR
# 01/11/2020

# http://ahmetfurkandemir.com/
# https://github.com/AhmetFurkanDEMIR
# https://www.linkedin.com/in/1dfurkan/

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from time import sleep as sl
import numpy as np
import threading
import skvideo.io
import datetime
import mss
import sys
import cv2

class Ui_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 359)

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 631, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(10, 240, 491, 23))
        self.folder = ""

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(270, 280, 49, 26))
        self.spinBox.setMaximum(180)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 280, 251, 21))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(482, 284, 141, 31))
        self.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: green;}')

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(330, 280, 71, 21))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(-1, -5, 361, 221))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(366, -5, 266, 221))
        self.label_6.setObjectName("label_6")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 70, 321, 31))

        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(366, -5, 266, 221))
        self.label_7.setObjectName("label_7")
        self.label_7.setPixmap(QtGui.QPixmap("cam0.gif"))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 120, 351, 23))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setGeometry(QtCore.QRect(60, 30, 49, 26))
        self.spinBox_2.setMinimum(30)
        self.spinBox_2.setMaximum(60)
        self.spinBox_2.setSingleStep(30)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(13, 30, 61, 31))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(330, 290, 291, 21))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 170, 241, 31))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.checkBox.setText(_translate("Dialog", "Combine the screen recording and the camera image?"))
        self.label.setText(_translate("Dialog", "Let the recording begin after"))
        self.pushButton.setText(_translate("Dialog", "Start recording"))
        self.label_4.setText(_translate("Dialog", "seconds"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "TextLabel"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Desktop Recording"))
        self.checkBox_2.setText(_translate("Dialog", "Record the voice of the computer?"))
        self.checkBox_3.setText(_translate("Dialog", "Record the sound of the microphone?"))
        self.label_2.setText(_translate("Dialog", "FPS"))
        self.label_3.setText(_translate("Dialog", "Developer : Ahmet Furkan DEMIR"))
        self.pushButton_2.setText(_translate("Dialog", "Screen recording directory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Settings"))

        self.pushButton_2.clicked.connect(self.directory)
        self.pushButton.clicked.connect(self.run)

        self.video_capture = cv2.VideoCapture(0)
        self.vid = threading.Thread(target=self.loop)
        self.vid.start()

        self.vida = threading.Thread(target=self.loopa)
        self.vida.start()


    def directory(self):

        self.folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))

    def loop(self):

        with mss.mss() as sct:

            monitor = {'top': 0, 'left': 0, 'width': 1366, 'height': 768}

            while True:

                self.img = np.array(sct.grab(monitor))
         
                self.framea = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

                self.image_desktop = cv2.resize(self.framea, (380,215), interpolation = cv2.INTER_AREA)

                self.qimg0 = QtGui.QImage(self.image_desktop,self.image_desktop.shape[1], self.image_desktop.shape[0], QtGui.QImage.Format_RGB888)
                self.pixmapa = QtGui.QPixmap.fromImage(self.qimg0)
                self.label_5.setPixmap(self.pixmapa)


    def loopa(self):

        while True:

            if self.checkBox.isChecked() == True:

                _, self.frameb = self.video_capture.read()

                self.frameb = cv2.cvtColor(self.frameb, cv2.COLOR_BGR2RGB)
                
                self.image_cam = cv2.resize(self.frameb, (260,215), interpolation = cv2.INTER_AREA)

                self.qimg1 = QtGui.QImage(self.image_cam,self.image_cam.shape[1], self.image_cam.shape[0], QtGui.QImage.Format_RGB888)
                self.pixmapb = QtGui.QPixmap.fromImage(self.qimg1)
                self.label_6.setPixmap(self.pixmapb)


            else:

                self.label_6.setPixmap(QtGui.QPixmap("cam.image"))


    def run(self):

        if self.pushButton.text() == "Start recording":

            if int(self.spinBox.value()) == 0:

                Dialog.setWindowTitle("On record")

                self.pushButton.setText("Stop recording")

                self.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')

            self.kn = True
            
            self.fps = int(self.spinBox_2.value())
            self.width = 1366
            self.height = 768
            self.crf = 17

            self.an = datetime.datetime.now()
            self.yıl = self.an.year
            self.ay = self.an.month
            self.gun = self.an.day
            self.saat = str(self.an.hour) + ":" + str(self.an.minute)
            self.tarih = str(self.gun) + "_" +str(self.ay) + "_" + str(self.yıl) + "_" + self.saat

            if self.folder == "":

                self.kyt = self.tarih + ".mp4"

            else:
                
                self.kyt = self.folder + "/" + self.tarih + ".mp4"

            print(self.kyt)

            self.writer = skvideo.io.FFmpegWriter(self.kyt, 
                inputdict={'-r': str(self.fps), '-s':'{}x{}'.format(self.width,self.height)},
                outputdict={'-r': str(self.fps), '-c:v': 'libx264', '-crf': str(self.crf), '-preset': 'ultrafast', '-pix_fmt': 'yuv444p'})


            self.vida1 = threading.Thread(target=self.run_timer)
            self.vida1.start()

        elif self.pushButton.text() == "Stop recording":

            self.kn = False

            Dialog.setWindowTitle("Not recording")

            self.pushButton.setText("Start recording")

            self.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: green;}')

            self.vida1.join()
            self.writer.close()


    def run_timer(self):

        self.ccc = 0
        self.tim = int(self.spinBox.value())

        Dialog.setWindowTitle("{} Sn".format(self.tim-self.ccc))

        self.pushButton.setText("{} Sn".format(self.tim-self.ccc))

        while True:

            if self.ccc == self.tim:

                Dialog.setWindowTitle("On record")

                self.pushButton.setText("Stop recording")

                self.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')

                break

            else:

                self.ccc += 1

                sl(0.8)

                Dialog.setWindowTitle("{} Sn".format(self.tim-self.ccc))

                self.pushButton.setText("{} Sn".format(self.tim-self.ccc))

        while True:

            if self.kn == True:

                self.frameaa = self.framea.copy()

                if self.checkBox.isChecked() == True:

                    self.bs = self.frameaa.shape[0] - 230
                    self.sn = self.frameaa.shape[0] - 15

                    self.bs1 = self.frameaa.shape[1] - 275
                    self.sn1 = self.frameaa.shape[1] - 15

                    self.frameaa[self.bs:self.sn,self.bs1:self.sn1,0] = self.image_cam[:,:,0]
                    self.frameaa[self.bs:self.sn,self.bs1:self.sn1,1] = self.image_cam[:,:,1]
                    self.frameaa[self.bs:self.sn,self.bs1:self.sn1,2] = self.image_cam[:,:,2]

                    self.writer.writeFrame(self.frameaa)

                else:

                    self.writer.writeFrame(self.frameaa)

            else:

                break


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    Dialog.setWindowTitle("Not recording")
    Dialog.setFixedSize(639, 359)
    Dialog.show()
    
    sys.exit(app.exec_())
