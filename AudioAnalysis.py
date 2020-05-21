from __future__ import print_function
import librosa
import time
import sys
from PIL import Image, ImageTk, ImageChops
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import simpleaudio as sa
import soundfile as sf
from scipy.io.wavfile import write
from playsound import playsound
from firebase import Firebase
import config
from PyQt5 import QtCore, QtGui, QtWidgets
from email.message import EmailMessage
import smtplib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1280, 778)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 778))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 778))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #121212;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameFirstFile = QtWidgets.QFrame(self.centralwidget)
        self.frameFirstFile.setGeometry(QtCore.QRect(20, 80, 401, 681))
        self.frameFirstFile.setAutoFillBackground(False)
        self.frameFirstFile.setStyleSheet("background-color: #E53C17;border: 1px solid white;border-radius: 10px;")
        self.frameFirstFile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFirstFile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFirstFile.setObjectName("frameFirstFile")
        self.labelFirstFile = QtWidgets.QLabel(self.frameFirstFile)
        self.labelFirstFile.setGeometry(QtCore.QRect(120, 20, 161, 31))
        self.labelFirstFile.setStyleSheet("background-color: #121212;border-radius: 0px;border: 2px solid white;")
        self.labelFirstFile.setTextFormat(QtCore.Qt.RichText)
        self.labelFirstFile.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFirstFile.setObjectName("labelFirstFile")
        self.pushButtonRecordFirstAudio = QtWidgets.QPushButton(self.frameFirstFile)
        self.pushButtonRecordFirstAudio.setGeometry(QtCore.QRect(50, 100, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRecordFirstAudio.setFont(font)
        self.pushButtonRecordFirstAudio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonRecordFirstAudio.setMouseTracking(True)
        self.pushButtonRecordFirstAudio.setTabletTracking(True)
        self.pushButtonRecordFirstAudio.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonRecordFirstAudio.setAutoFillBackground(False)
        self.pushButtonRecordFirstAudio.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonRecordFirstAudio.setObjectName("pushButtonRecordFirstAudio")
        self.pushButtonPlaybackFirstAudio = QtWidgets.QPushButton(self.frameFirstFile)
        self.pushButtonPlaybackFirstAudio.setGeometry(QtCore.QRect(50, 170, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPlaybackFirstAudio.setFont(font)
        self.pushButtonPlaybackFirstAudio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonPlaybackFirstAudio.setMouseTracking(True)
        self.pushButtonPlaybackFirstAudio.setTabletTracking(True)
        self.pushButtonPlaybackFirstAudio.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonPlaybackFirstAudio.setAutoFillBackground(False)
        self.pushButtonPlaybackFirstAudio.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonPlaybackFirstAudio.setObjectName("pushButtonPlaybackFirstAudio")
        self.labelFirstImage = QtWidgets.QLabel(self.frameFirstFile)
        self.labelFirstImage.setGeometry(QtCore.QRect(20, 380, 361, 271))
        self.labelFirstImage.setStyleSheet("background-color: #121212;border: 0.5px solid white;border-radius: 8px;")
        self.labelFirstImage.setText("")
        self.labelFirstImage.setPixmap(QtGui.QPixmap("/Users/parthdoshi/Documents/Audio Processing/background.png"))
        self.labelFirstImage.setObjectName("labelFirstImage")
        self.pushButtonDisplayFirstSpectogram = QtWidgets.QPushButton(self.frameFirstFile)
        self.pushButtonDisplayFirstSpectogram.setGeometry(QtCore.QRect(50, 240, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDisplayFirstSpectogram.setFont(font)
        self.pushButtonDisplayFirstSpectogram.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonDisplayFirstSpectogram.setMouseTracking(True)
        self.pushButtonDisplayFirstSpectogram.setTabletTracking(True)
        self.pushButtonDisplayFirstSpectogram.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonDisplayFirstSpectogram.setAutoFillBackground(False)
        self.pushButtonDisplayFirstSpectogram.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonDisplayFirstSpectogram.setObjectName("pushButtonDisplayFirstSpectogram")
        self.frameSecondFile = QtWidgets.QFrame(self.centralwidget)
        self.frameSecondFile.setGeometry(QtCore.QRect(440, 80, 401, 681))
        self.frameSecondFile.setAutoFillBackground(False)
        self.frameSecondFile.setStyleSheet("background-color: #E53C17\n"
";border: 1px solid white;border-radius: 10px;")
        self.frameSecondFile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSecondFile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSecondFile.setObjectName("frameSecondFile")
        self.labelSecondFile = QtWidgets.QLabel(self.frameSecondFile)
        self.labelSecondFile.setGeometry(QtCore.QRect(120, 20, 161, 31))
        self.labelSecondFile.setStyleSheet("background-color: #121212;border-radius: 0px;border: 2px solid white;")
        self.labelSecondFile.setTextFormat(QtCore.Qt.RichText)
        self.labelSecondFile.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSecondFile.setObjectName("labelSecondFile")
        self.pushButtonRecordSecondAudio = QtWidgets.QPushButton(self.frameSecondFile)
        self.pushButtonRecordSecondAudio.setGeometry(QtCore.QRect(50, 100, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRecordSecondAudio.setFont(font)
        self.pushButtonRecordSecondAudio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonRecordSecondAudio.setMouseTracking(True)
        self.pushButtonRecordSecondAudio.setTabletTracking(True)
        self.pushButtonRecordSecondAudio.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonRecordSecondAudio.setAutoFillBackground(False)
        self.pushButtonRecordSecondAudio.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonRecordSecondAudio.setObjectName("pushButtonRecordSecondAudio")
        self.pushButtonPlaybackSecondAudio = QtWidgets.QPushButton(self.frameSecondFile)
        self.pushButtonPlaybackSecondAudio.setGeometry(QtCore.QRect(50, 170, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPlaybackSecondAudio.setFont(font)
        self.pushButtonPlaybackSecondAudio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonPlaybackSecondAudio.setMouseTracking(True)
        self.pushButtonPlaybackSecondAudio.setTabletTracking(True)
        self.pushButtonPlaybackSecondAudio.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonPlaybackSecondAudio.setAutoFillBackground(False)
        self.pushButtonPlaybackSecondAudio.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonPlaybackSecondAudio.setObjectName("pushButtonPlaybackSecondAudio")
        self.labelSecondImage = QtWidgets.QLabel(self.frameSecondFile)
        self.labelSecondImage.setGeometry(QtCore.QRect(20, 380, 361, 271))
        self.labelSecondImage.setStyleSheet("background-color: #121212;border: 0.5px solid white;border-radius: 8px;")
        self.labelSecondImage.setText("")
        self.labelSecondImage.setPixmap(QtGui.QPixmap("/Users/parthdoshi/Documents/Audio Processing/background.png"))
        self.labelSecondImage.setObjectName("labelSecondImage")
        self.pushButtonDisplaySecondSpectogram = QtWidgets.QPushButton(self.frameSecondFile)
        self.pushButtonDisplaySecondSpectogram.setGeometry(QtCore.QRect(50, 240, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDisplaySecondSpectogram.setFont(font)
        self.pushButtonDisplaySecondSpectogram.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonDisplaySecondSpectogram.setMouseTracking(True)
        self.pushButtonDisplaySecondSpectogram.setTabletTracking(True)
        self.pushButtonDisplaySecondSpectogram.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonDisplaySecondSpectogram.setAutoFillBackground(False)
        self.pushButtonDisplaySecondSpectogram.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonDisplaySecondSpectogram.setObjectName("pushButtonDisplaySecondSpectogram")
        self.frameResult = QtWidgets.QFrame(self.centralwidget)
        self.frameResult.setGeometry(QtCore.QRect(860, 80, 401, 681))
        self.frameResult.setAutoFillBackground(False)
        self.frameResult.setStyleSheet("background-color: #FE7D61\n"
";border: 1px solid white;border-radius: 10px;")
        self.frameResult.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameResult.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameResult.setObjectName("frameResult")
        self.labelResult = QtWidgets.QLabel(self.frameResult)
        self.labelResult.setGeometry(QtCore.QRect(120, 20, 161, 31))
        self.labelResult.setStyleSheet("background-color: #121212;border-radius: 0px;border: 2px solid white;")
        self.labelResult.setTextFormat(QtCore.Qt.RichText)
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setObjectName("labelResult")
        self.pushButtonComputeResult = QtWidgets.QPushButton(self.frameResult)
        self.pushButtonComputeResult.setGeometry(QtCore.QRect(50, 100, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonComputeResult.setFont(font)
        self.pushButtonComputeResult.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonComputeResult.setMouseTracking(True)
        self.pushButtonComputeResult.setTabletTracking(True)
        self.pushButtonComputeResult.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonComputeResult.setAutoFillBackground(False)
        self.pushButtonComputeResult.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonComputeResult.setObjectName("pushButtonComputeResult")
        self.pushButtonUpdateResult = QtWidgets.QPushButton(self.frameResult)
        self.pushButtonUpdateResult.setGeometry(QtCore.QRect(50, 600, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdateResult.setFont(font)
        self.pushButtonUpdateResult.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonUpdateResult.setMouseTracking(True)
        self.pushButtonUpdateResult.setTabletTracking(True)
        self.pushButtonUpdateResult.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonUpdateResult.setAutoFillBackground(False)
        self.pushButtonUpdateResult.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonUpdateResult.setObjectName("pushButtonUpdateResult")
#         self.labelResultImage = QtWidgets.QLabel(self.frameResult)
#         self.labelResultImage.setGeometry(QtCore.QRect(20, 180, 361, 271))
#         self.labelResultImage.setStyleSheet("background-color: #121212;border: 0.5px solid white;border-radius: 8px;")
#         self.labelResultImage.setText("")
#         self.labelResultImage.setPixmap(QtGui.QPixmap("/Users/parthdoshi/Documents/Audio Processing/background.png"))
#         self.labelResultImage.setObjectName("labelResultImage")
        self.labelResultWindow = QtWidgets.QLabel(self.frameResult)
        self.labelResultWindow.setGeometry(QtCore.QRect(50, 470, 301, 91))
        self.labelResultWindow.setStyleSheet("background-color: #121212;border: 0.5px solid white;border-radius: 8px;")
        self.labelResultWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResultWindow.setObjectName("labelResultWindow")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(20, 10, 700, 51))
        self.labelTitle.setObjectName("labelTitle")
        self.comboBoxBridge = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBridge.setGeometry(QtCore.QRect(750, 20, 220, 30))
        self.comboBoxBridge.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.comboBoxSite = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSite.setGeometry(QtCore.QRect(1020, 20, 220, 30))
        self.comboBoxSite.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelFirstFile.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Initial File</span></p></body></html>"))
        self.pushButtonRecordFirstAudio.setText(_translate("MainWindow", "Record First Audio"))
        self.pushButtonPlaybackFirstAudio.setText(_translate("MainWindow", "Playback First Audio"))
        self.pushButtonDisplayFirstSpectogram.setText(_translate("MainWindow", "Display Spectrogram"))
        self.labelSecondFile.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Test File</span></p></body></html>"))
        self.pushButtonRecordSecondAudio.setText(_translate("MainWindow", "Record Second Audio"))
        self.pushButtonPlaybackSecondAudio.setText(_translate("MainWindow", "Playback Second"))
        self.pushButtonDisplaySecondSpectogram.setText(_translate("MainWindow", "Display Spectrogram"))
        self.labelResult.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Results</span></p></body></html>"))
        self.pushButtonComputeResult.setText(_translate("MainWindow", "Compute Result"))
        self.pushButtonUpdateResult.setText(_translate("MainWindow", "Update Result"))
        self.labelResultWindow.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Result</span></p></body></html>"))
        self.labelTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Audio Processing</span></p></body></html>"))
        self.comboBoxBridge.addItems(["Airoli Bridge","Bandra-Worli Sea-Link","Mumbai Trans Harbour Link","Vashi Bridge"])
        self.comboBoxSite.addItems(["1","2","3","4","5","6","7","8","9","10"])
        
        # --------------------------------------Button Bindings--------------------------------------

        self.pushButtonRecordFirstAudio.clicked.connect(self.recordFirstAudio)
        self.pushButtonRecordSecondAudio.clicked.connect(self.recordSecondAudio)
        self.pushButtonPlaybackFirstAudio.clicked.connect(self.playbackFirstAudio)
        self.pushButtonPlaybackSecondAudio.clicked.connect(self.playbackSecondAudio)
        self.pushButtonDisplayFirstSpectogram.clicked.connect(self.displayFirstSpectogram)
        self.pushButtonDisplaySecondSpectogram.clicked.connect(self.displaySecondSpectogram)
        self.pushButtonComputeResult.clicked.connect(self.computeResult)
        self.pushButtonUpdateResult.clicked.connect(self.updateResult)

        # ---------------------------------------------------------------------------------------------

    # --------------------------------------Button Functions--------------------------------------

    def recordFirstAudio(self):
        print("Record First Audio")
        fs = 44100
        seconds = 5
        print('Recoding Now')
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write('output1.wav', fs, myrecording)
        print('Recoding Done')
        time.sleep(5)
        
    def recordSecondAudio(self):
        print("Record Second Audio")
        fs = 44100
        seconds = 5
        print('Recoding Now')
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write('output2.wav', fs, myrecording)
        print('Recoding Done')
        time.sleep(5)

    def playbackFirstAudio(self):
        print("Playback First Audio")
        filename = 'output1.wav'
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data,fs)
        status = sd.wait()

    def playbackSecondAudio(self):
        print("Playback Second Audio")
        filename = 'output2.wav'
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data,fs)
        status = sd.wait()

    def displayFirstSpectogram(self):
        print("Display First Spectogram")
        x,sr = librosa.load(r'C:\Users\Viraj\SoundAnalysis\output1.wav')
        d = librosa.amplitude_to_db(np.abs(librosa.stft(x)), ref=np.max)
        n_fft = 1024
        hop_length = int(librosa.time_to_samples(1./200, sr=sr))
        n_mels = 138
        S = librosa.feature.melspectrogram(x, sr=sr, n_fft=n_fft,hop_length=hop_length,n_mels=n_mels)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max),y_axis='mel',x_axis='time', sr=sr,hop_length=hop_length)
        plt.colorbar(format='%+2.0f dB')
        plt.savefig('audio1.png')
        self.firstImage = r'C:\Users\Viraj\SoundAnalysis\audio1.png'
        self.labelFirstImage.setPixmap(QtGui.QPixmap(self.firstImage).scaled(361,271))
        

    def displaySecondSpectogram(self):
        print("Display Second Spectogram")
        y,sr = librosa.load(r'C:\Users\Viraj\SoundAnalysis\output2.wav')
        d = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
        n_fft = 1024
        hop_length = int(librosa.time_to_samples(1./200, sr=sr))
        n_mels = 138
        S = librosa.feature.melspectrogram(y, sr=sr, n_fft=n_fft,hop_length=hop_length,n_mels=n_mels)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max),y_axis='mel',x_axis='time', sr=sr,hop_length=hop_length)
        plt.colorbar(format='%+2.0f dB')
        plt.savefig('audio2.png')
        self.secondImage = r'C:\Users\Viraj\SoundAnalysis\audio2.png'
        self.labelSecondImage.setPixmap(QtGui.QPixmap(self.secondImage).scaled(361,271))

    def computeResult(self):
        print("Compute Result")
        x,sr = librosa.load(r'C:\Users\Viraj\SoundAnalysis\output1.wav')
        y,sr = librosa.load(r'C:\Users\Viraj\SoundAnalysis\output2.wav')
        p = np.split(x,10)
        q = np.split(y,10)
        i = []
        aud1 = []
        aud2 = []
        for i in p:
            r = np.sqrt(np.mean(i**2))
            aud1.append(r)
        for i in q:
            s = np.sqrt(np.mean(i**2))
            aud2.append(s)
        x1 = np.asarray(aud1)
        y1 = np.asarray(aud2)
        j = 0
        k = []
        for j in range (len(x1)):
            d = (np.abs(x1[j]-y1[j]))*100
            e = ('%.3f'%d)
            k.append(e)
            print(d)
        val = ' '.join([str(elem) for elem in k])
        print(val)
        self.values = val
        self.res = max(k)
        print(self.res)
        self.labelResultWindow.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">" + self.res + "</span></p></body></html>")
        firebase = Firebase(config.FIREBASE_CONFIG)
        db = firebase.database()
        db.child(self.comboBoxBridge.currentText()).child(self.comboBoxSite.currentText()).push(self.res)

    def updateResult(self):
        print("Update Result")
        msg = EmailMessage()
        msg['Subject'] = "Audio Processing Result "+ self.res
        msg['From'] = config.EMAIL_ADDRESS
        msg['To'] = config.RESULT_EMAIL_ADDRESS
        message = "Initial Spectrogram " + self.firstImage + "\n Current Recording Spectorgram " + self.secondImage + "\n at " + self.comboBoxBridge.currentText() + " Site No.: " + self.comboBoxSite.currentText() + "RMS of Audio over 0.5 interval" + self.values + ""
        msg.set_content(message)
        attachments = [self.firstImage, self.secondImage]
        for path in attachments:
            with open(path,'rb') as file:
                data = file.read()
                name = path.split("\\")[-1]
            msg.add_attachment(data, maintype = 'application', subtype = 'octet-stream', filename = name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(config.EMAIL_ADDRESS, config.PASSWORD)
            smtp.send_message(msg)

    # ----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
