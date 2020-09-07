from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
import os.path
import subprocess
import subprocess
import time
import logging
import os
import glob
from configparser import ConfigParser
config = ConfigParser()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 557)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setGeometry(QtCore.QRect(140, 460, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_play.setFont(font)
        self.pushButton_play.setObjectName("pushButton_play")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(210, 10, 361, 71))
        self.pushButton_play.clicked.connect(self.runBtn)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(40, 110, 311, 301))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("./image/SCP.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(380, 110, 415, 301))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_event = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_event.setFont(font)
        self.label_event.setObjectName("label_event")
        self.gridLayout.addWidget(self.label_event, 0, 0, 1, 1)
        self.Slider_pedstrain = QtWidgets.QSlider(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Slider_pedstrain.setFont(font)
        self.Slider_pedstrain.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_pedstrain.setObjectName("Slider_pedstrain")
        self.gridLayout.addWidget(self.Slider_pedstrain, 6, 1, 1, 1)
        self.Slider_fog = QtWidgets.QSlider(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Slider_fog.setFont(font)
        self.Slider_fog.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_fog.setObjectName("Slider_fog")
        self.gridLayout.addWidget(self.Slider_fog, 4, 1, 1, 1)
        self.comboBox_Speed = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox_Speed.setFont(font)
        self.comboBox_Speed.setObjectName("comboBox_Speed")
        self.comboBox_Speed.addItem("")
        self.comboBox_Speed.addItem("")
        self.comboBox_Speed.addItem("")
        self.gridLayout.addWidget(self.comboBox_Speed, 1, 1, 1, 1)
        self.comboBox_event = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox_event.setFont(font)
        self.comboBox_event.setObjectName("comboBox_event")
        self.comboBox_event.addItem("")
        self.comboBox_event.addItem("")
        self.comboBox_event.addItem("")
        self.comboBox_event.addItem("")
        self.comboBox_event.addItem("")
        self.gridLayout.addWidget(self.comboBox_event, 0, 1, 1, 1)
        self.Slider_rain = QtWidgets.QSlider(self.layoutWidget)
        self.comboBox_event.activated[str].connect(self.changeImage)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Slider_rain.setFont(font)
        self.Slider_rain.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_rain.setObjectName("Slider_rain")
        self.gridLayout.addWidget(self.Slider_rain, 3, 1, 1, 1)
        self.label_rain = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_rain.setFont(font)
        self.label_rain.setObjectName("label_rain")
        self.gridLayout.addWidget(self.label_rain, 3, 0, 1, 1)
        self.label_wetness = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_wetness.setFont(font)
        self.label_wetness.setObjectName("label_wetness")
        self.gridLayout.addWidget(self.label_wetness, 5, 0, 1, 1)
        self.label_time = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.gridLayout.addWidget(self.label_time, 2, 0, 1, 1)
        self.checkBox_video = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_video.setObjectName("checkBox_video")
        self.gridLayout.addWidget(self.checkBox_video, 8, 0, 1, 1)
        self.label_pedstrain = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_pedstrain.setFont(font)
        self.label_pedstrain.setObjectName("label_pedstrain")
        self.gridLayout.addWidget(self.label_pedstrain, 6, 0, 1, 1)
        self.checkBox_json = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_json.setObjectName("checkBox_json")
        self.gridLayout.addWidget(self.checkBox_json, 8, 1, 1, 1)
        self.Slider_wetness = QtWidgets.QSlider(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Slider_wetness.setFont(font)
        self.Slider_wetness.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_wetness.setObjectName("Slider_wetness")
        self.gridLayout.addWidget(self.Slider_wetness, 5, 1, 1, 1)
        self.timeEdit_time = QtWidgets.QTimeEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.timeEdit_time.setFont(font)
        self.timeEdit_time.setObjectName("timeEdit_time")
        self.gridLayout.addWidget(self.timeEdit_time, 2, 1, 1, 1)
        self.label_fog = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_fog.setFont(font)
        self.label_fog.setObjectName("label_fog")
        self.gridLayout.addWidget(self.label_fog, 4, 0, 1, 1)
        self.label_speed = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_speed.setFont(font)
        self.label_speed.setObjectName("label_speed")
        self.gridLayout.addWidget(self.label_speed, 1, 0, 1, 1)
        self.label_vehicle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_vehicle.setFont(font)
        self.label_vehicle.setObjectName("label_vehicle")
        self.gridLayout.addWidget(self.label_vehicle, 7, 0, 1, 1)
        self.Slider_vehicle = QtWidgets.QSlider(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Slider_vehicle.setFont(font)
        self.Slider_vehicle.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_vehicle.setObjectName("Slider_vehicle")
        self.gridLayout.addWidget(self.Slider_vehicle, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show_popup()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_play.setText(_translate("MainWindow", "Play"))
        self.label_title.setText(_translate(
            "MainWindow", "LGSVL SIMULATOR TEST"))
        self.label_event.setText(_translate(
            "MainWindow", "Scenarios Choose :"))
        self.comboBox_Speed.setItemText(0, _translate("MainWindow", "40 km/h"))
        self.comboBox_Speed.setItemText(1, _translate("MainWindow", "60 km/h"))
        self.comboBox_Speed.setItemText(2, _translate("MainWindow", "80 km/h"))
        self.comboBox_event.setItemText(0, _translate("MainWindow", "SCP"))
        self.comboBox_event.setItemText(1, _translate("MainWindow", "LTIP"))
        self.comboBox_event.setItemText(2, _translate("MainWindow", "RTIP"))
        self.comboBox_event.setItemText(3, _translate("MainWindow", "OD"))
        self.comboBox_event.setItemText(4, _translate("MainWindow", "LD"))
        self.label_rain.setText(_translate("MainWindow", "Rain Level :"))
        self.label_wetness.setText(_translate("MainWindow", "Wetness Level :"))
        self.label_time.setText(_translate("MainWindow", "Time Choose :"))
        self.checkBox_video.setText(_translate("MainWindow", "Save Vidoe?"))
        self.label_pedstrain.setText(_translate(
            "MainWindow", "Random pedstrian :"))
        self.checkBox_json.setText(_translate("MainWindow", "Save josn?"))
        self.label_fog.setText(_translate("MainWindow", "Fog Level :"))
        self.label_speed.setText(_translate("MainWindow", "Speed Choose :"))
        self.label_vehicle.setText(_translate("MainWindow", "Random vehicle:"))

    def changeImage(self, text):
        self.image.setPixmap(QtGui.QPixmap("./image/"+text+".png"))

    def auto(self, cmd):
        MyDialog.test(self, 'launch rosbridge ...')
        roslaunch_proc = subprocess.Popen([
            'roslaunch',
            'rosbridge_server',
            'rosbridge_websocket.launch'
        ])
        time.sleep(1.5)

        MyDialog.test(self, 'record rosbag ...')
        record_proc = subprocess.Popen([
            'rosbag',
            'record',
            '-O',
            'tmp',
            '/simulator/camera_node/image/compressed',
            '/points_raw',
            '__name:=RRRRRRRRRR'
        ])
        # record_proc.communicate()
        MyDialog.test(self, 'run lgsvl ...')
        lgsvl_proc = subprocess.Popen(cmd)
        lgsvl_proc.communicate()

        MyDialog.test(self, 'stop record rosbag ...')
        kill_record_proc = subprocess.Popen([
            'rosnode',
            'kill',
            '/RRRRRRRRRR',
        ])
        # kill_record_proc.communicate()
        time.sleep(1)

        MyDialog.test(self, 'export images ...')
        export_proc = subprocess.Popen([
            'rosrun',
            'image_view',
            'extract_images',
            'compressed',
            '_sec_per_frame:=0.02',
            'image:=/simulator/camera_node/image',
            '__name:=IIIIIIIIII'

        ])
        # export_proc.communicate()
        time.sleep(1)

        MyDialog.test(self, 'play rosbag ...')
        play_proc = subprocess.Popen([
            'rosbag',
            'play',
            'tmp.bag'
        ])
        play_proc.communicate()

        MyDialog.test(self, 'stop export ...')
        kill_export_proc = subprocess.Popen([
            'rosnode',
            'kill',
            '/IIIIIIIIII',
        ])
        # kill_export_proc.communicate()
        time.sleep(1)

        MyDialog.test(self, 'stop rosbridge ...')
        roslaunch_proc.send_signal(subprocess.signal.SIGINT)

        os.remove('tmp.bag')

        MyDialog.test(self, 'export video ...')
        proc = subprocess.Popen([
            'ffmpeg',
            '-r', '50',
            '-i', 'frame%04d.jpg',
            '-c:v', 'libx264',
            '-preset', 'slow',
            '-profile:v', 'high',
            '-crf', '18',
            '-coder', '1',
            '-pix_fmt', 'yuv420p',
            '-movflags', '+faststart',
            '-g', '30',
            '-bf', '2',
            '-c:a', 'aac',
            '-b:a', '384k',
            '-profile:a', 'aac_low',
            'output_'+time.strftime("%m%d_%H%M%S", time.localtime())+'.mp4'
        ])

        proc.communicate()

        for f in glob.glob("*.jpg"):
            os.remove(f)
        return 0

    def runBtn(self):
        config.read('config.ini')
        config.set('main', 'speed', str(self.comboBox_Speed.currentText()).split(' ')[0])
        config.set('main', 'rain_level', str(self.Slider_rain.value()))
        config.set('main', 'fog_level', str(self.Slider_fog.value()))
        config.set('main', 'wetness_level', str(self.Slider_wetness.value()))
        config.set('main', 'set_time', str(self.timeEdit_time.time().hour()))
        config.set('main', 'save_video', str(self.checkBox_video.isChecked()))
        config.set('main', 'save_json', str(self.checkBox_json.isChecked()))
        config.set('main', 'pedstrain', str(self.Slider_pedstrain.value()))
        config.set('main', 'vehicle', str(self.Slider_vehicle.value()))
        with open('config.ini', 'w') as f:
            config.write(f)
        text = str(self.comboBox_event.currentText())
        # speed = str(self.comboBox_Speed.currentText()).split(' ')[0]
        # rain_level = str(self.Slider_rain.value())
        # fog_level = str(self.Slider_fog.value())
        # wetness_level = str(self.Slider_wetness.value())
        # set_time = str(self.timeEdit_time.time().hour())
        # save_video = str(self.checkBox_video.isChecked())
        # save_json = str(self.checkBox_json.isChecked())
        # pedstrain = str(self.Slider_pedstrain.value())
        # vehicle = str(self.Slider_vehicle.value())
        # print(speed, rain_level, fog_level, wetness_level,
        #       set_time, save_video, save_json)
        path = './script/'+text+'.py'
        # print(os.path.exists(path))

        cmd = ['python3', path]
        # cmd = ['python3', path, speed, rain_level, fog_level, wetness_level,
        #        set_time, save_video, save_json, pedstrain, vehicle]

        # print('cmd: ', cmd)

        if os.path.exists(path):
            if self.checkBox_video.isChecked():
                p_status = self.auto(cmd)
                if (p_status == 0):
                    self.show_succ()
                else:
                    self.show_error()
            else:
                lgsvl_proc = subprocess.Popen(cmd)
                lgsvl_proc.communicate()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle('readme')
        msg.setText(' 1. launch the simulator \n 2. Click the Open Browser \n 3. check the API Only option and click the "Play" button in the bottom right.')
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def show_succ(self):
        msg = QMessageBox()
        msg.setWindowTitle('Done')
        msg.setText('Execution Succeed')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def show_error(self):
        msg = QMessageBox()
        msg.setWindowTitle('Error')
        msg.setText('Execution Failed')
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()


class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QtWidgets.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


class MyDialog(QtWidgets.QDialog, QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        logTextBox = QTextEditLogger(self)
        logTextBox.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.DEBUG)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(logTextBox.widget)
        self.setLayout(layout)

    def test(self, msg):
        logging.info(msg)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    dlg = MyDialog()
    dlg.show()
    dlg.raise_()
    sys.exit(app.exec_())
