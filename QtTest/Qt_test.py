# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 511, 725))
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_5.addWidget(self.plainTextEdit_2)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_5.addWidget(self.pushButton_7)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_2.addWidget(self.checkBox_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_3.addWidget(self.textEdit_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.comboBox_8 = QtWidgets.QComboBox(self.widget)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_8)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout.addWidget(self.checkBox_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_9 = QtWidgets.QComboBox(self.widget)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_9)
        self.comboBox_7 = QtWidgets.QComboBox(self.widget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_7)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_6)
        self.comboBox_10 = QtWidgets.QComboBox(self.widget)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(MainWindow.read)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_14.setText(_translate("MainWindow", "上位机>下位机"))
        self.pushButton_7.setText(_translate("MainWindow", "清除窗口信息"))
        self.label_11.setText(_translate("MainWindow", "文本发送框："))
        self.checkBox_4.setText(_translate("MainWindow", "循环发送"))
        self.checkBox_5.setText(_translate("MainWindow", "单次发送"))
        self.lineEdit_2.setText(_translate("MainWindow", "1000ms/次"))
        self.pushButton_4.setText(_translate("MainWindow", "读取文件"))
        self.pushButton_6.setText(_translate("MainWindow", "保存"))
        self.pushButton_8.setText(_translate("MainWindow", "发送"))
        self.label_18.setText(_translate("MainWindow", "串口号："))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "COM5"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "COM6"))
        self.comboBox_8.setItemText(6, _translate("MainWindow", "COM7"))
        self.comboBox_8.setItemText(7, _translate("MainWindow", "COM8"))
        self.comboBox_8.setItemText(8, _translate("MainWindow", "COM9"))
        self.comboBox_8.setItemText(9, _translate("MainWindow", "COM10"))
        self.radioButton_2.setText(_translate("MainWindow", "打开串口"))
        self.checkBox_6.setText(_translate("MainWindow", "HEX显示"))
        self.label_12.setText(_translate("MainWindow", "波特率："))
        self.label_13.setText(_translate("MainWindow", "数据位："))
        self.label_17.setText(_translate("MainWindow", "停止位："))
        self.label_16.setText(_translate("MainWindow", "校验位："))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "600"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "1200"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "2400"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "4800"))
        self.comboBox_9.setItemText(4, _translate("MainWindow", "9600"))
        self.comboBox_9.setItemText(5, _translate("MainWindow", "14400"))
        self.comboBox_9.setItemText(6, _translate("MainWindow", "19200"))
        self.comboBox_9.setItemText(7, _translate("MainWindow", "28800"))
        self.comboBox_9.setItemText(8, _translate("MainWindow", "38400"))
        self.comboBox_9.setItemText(9, _translate("MainWindow", "57600"))
        self.comboBox_9.setItemText(10, _translate("MainWindow", "115200"))
        self.comboBox_9.setItemText(11, _translate("MainWindow", "230400"))
        self.comboBox_9.setItemText(12, _translate("MainWindow", "460800"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "6"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "7"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "8"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "无效验"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "奇校验"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "偶校验"))

