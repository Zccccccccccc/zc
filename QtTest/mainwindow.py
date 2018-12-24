# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 700)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
#~
        #~~~~~~~~~~~~~~

        #!!!!!!
        self.horizontalLayout_up = QtWidgets.QHBoxLayout()
        self.horizontalLayout_up.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_up.setContentsMargins(2, 8, 2, 0)
        self.horizontalLayout_up.setSpacing(6)
        self.horizontalLayout_up.setObjectName("horizontalLayout_up")
        self.label_up = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_up.sizePolicy().hasHeightForWidth())
        self.label_up.setSizePolicy(sizePolicy)
        self.label_up.setObjectName("label_up")
        self.horizontalLayout_up.addWidget(self.label_up)
        spacerItem4 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_up.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_up, 0, 0, 1, 1)
        #下位机接受数据窗口
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(20, 40))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        # 设置背景图片，固定，上下左右居中
        # self.textEdit.setStyleSheet("background-image:url(:/water.png);\n"
        #                             "background-attachment:fixed;\n"
        #                             "background-repeat:none;\n"
        #                             "background-position:center")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)


        self.horizontalLayout = QtWidgets.QHBoxLayout()
        #设置每行之间的间距
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(2, 8, 2, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        # self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        # self.comboBox.setSizePolicy(sizePolicy)
        # self.comboBox.setMinimumSize(QtCore.QSize(60, 20))
        # self.comboBox.setMaximumSize(QtCore.QSize(60, 20))
        # self.comboBox.setObjectName("comboBox")
        # self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit_com = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_com.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_com.sizePolicy().hasHeightForWidth())
        self.lineEdit_com.setSizePolicy(sizePolicy)
        self.lineEdit_com.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_com.setMaximumSize(QtCore.QSize(40, 20))
        self.lineEdit_com.setObjectName("lineEdit_com")
        self.horizontalLayout.addWidget(self.lineEdit_com)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 255);\n"
"border-top-color: rgb(0, 170, 0);\n"
"alternate-background-color: rgb(255, 0, 0);\n"
"hover: rgb(85, 255, 127);")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        # self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        # self.pushButton_4.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        # self.pushButton_4.setSizePolicy(sizePolicy)
        # self.pushButton_4.setMinimumSize(QtCore.QSize(80, 20))
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.horizontalLayout.addWidget(self.pushButton_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)



        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)





        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        #QTcreator中设置MARGINS为0，但是生成的MARGINS成不为0,需要手动修改一下才行
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QtCore.QSize(60, 20))
        self.comboBox_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        # self.checkBox_4 = QtWidgets.QCheckBox(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        # self.checkBox_4.setSizePolicy(sizePolicy)
        # self.checkBox_4.setObjectName("checkBox_4")
        # self.horizontalLayout_2.addWidget(self.checkBox_4)
        # self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        # self.lineEdit_2.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        # self.lineEdit_2.setSizePolicy(sizePolicy)
        # self.lineEdit_2.setMinimumSize(QtCore.QSize(20, 20))
        # self.lineEdit_2.setMaximumSize(QtCore.QSize(40, 20))
        # self.lineEdit_2.setObjectName("lineEdit_2")
        # self.horizontalLayout_2.addWidget(self.lineEdit_2)
        # self.label_7 = QtWidgets.QLabel(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        # self.label_7.setSizePolicy(sizePolicy)
        # self.label_7.setObjectName("label_7")
        # self.horizontalLayout_2.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QtCore.QSize(60, 20))
        self.comboBox_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        # self.label_3 = QtWidgets.QLabel(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        # self.label_3.setSizePolicy(sizePolicy)
        # self.label_3.setObjectName("label_3")
        # self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setMinimumSize(QtCore.QSize(60, 20))
        self.comboBox_4.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        # self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        # self.lineEdit.setSizePolicy(sizePolicy)
        # self.lineEdit.setMinimumSize(QtCore.QSize(30, 20))
        # self.lineEdit.setObjectName("lineEdit")
        # self.horizontalLayout_4.addWidget(self.lineEdit)
        # self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        # self.pushButton.setSizePolicy(sizePolicy)
        # self.pushButton.setObjectName("pushButton")
        # self.horizontalLayout_4.addWidget(self.pushButton)
#~~~~~
        # self.pushButtonsave = QtWidgets.QPushButton(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButtonsave.sizePolicy().hasHeightForWidth())
        # self.pushButtonsave.setSizePolicy(sizePolicy)
        # self.pushButtonsave.setObjectName("pushButton")
        # self.horizontalLayout_4.addWidget(self.pushButtonsave)
#!!!!
        spacerItem3 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setMinimumSize(QtCore.QSize(60, 20))
        self.comboBox_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_5.addWidget(self.comboBox_5)
        # self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        # self.checkBox.setSizePolicy(sizePolicy)
        # self.checkBox.setObjectName("checkBox")
        # self.horizontalLayout_5.addWidget(self.checkBox)
        # self.checkBox_2 = QtWidgets.QCheckBox(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        # self.checkBox_2.setSizePolicy(sizePolicy)
        # self.checkBox_2.setObjectName("checkBox_2")
        # self.horizontalLayout_5.addWidget(self.checkBox_2)
        spacerItem4 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.horizontalLayout_show = QtWidgets.QHBoxLayout()
        self.horizontalLayout_show.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_show.setContentsMargins(2, 8, 2, 0)
        self.horizontalLayout_show.setSpacing(6)
        self.horizontalLayout_show.setObjectName("horizontalLayout_show")
        #!!!!!!!
        #!!!!!!
        self.horizontalLayout_in_out = QtWidgets.QHBoxLayout()
        self.horizontalLayout_in_out.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_in_out.setSpacing(6)
        self.horizontalLayout_in_out.setObjectName("horizontalLayout_in_out")
        self.pushButton_in = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_in.sizePolicy().hasHeightForWidth())
        self.pushButton_in.setSizePolicy(sizePolicy)
        self.pushButton_in.setObjectName("pushButton_in")
        self.horizontalLayout_in_out.addWidget(self.pushButton_in)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_in_out.addWidget(self.pushButton)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_in_out.addWidget(self.checkBox_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(40, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_in_out.addWidget(self.lineEdit_2)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_in_out.addWidget(self.label_7)
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_in_out.addWidget(self.checkBox)

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_in_out.addWidget(self.checkBox_5)

        spacerItem4 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_in_out.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_in_out, 7, 0, 1, 1)
        #####
        # self.horizontalLayout_show = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_show.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        # self.horizontalLayout_show.setContentsMargins(2, 8, 2, 0)
        # self.horizontalLayout_show.setSpacing(6)
        # self.lineEditSS = QtWidgets.QLineEdit(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # self.lineEditSS.setSizePolicy(sizePolicy)
        # self.lineEditSS.setMinimumSize(QtCore.QSize(30, 20))
        # self.lineEditSS.setObjectName("lineEdit")
        # self.horizontalLayout_show.addWidget(self.lineEditSS)
        # self.checkBox_show = QtWidgets.QCheckBox(self.centralWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.checkBox_show.sizePolicy().hasHeightForWidth())
        # self.checkBox_show.setSizePolicy(sizePolicy)
        # self.checkBox_show.setObjectName("checkBox_show")
        # self.horizontalLayout_show.addWidget(self.checkBox_show)
        # spacerItem4 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_show.addItem(spacerItem4)
        # self.gridLayout.addLayout(self.horizontalLayout_show, 8, 0, 1, 1)
        ####


        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 447, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "仿下位机发送接受数据软件"))
        self.label_up.setText(_translate("MainWindow", "上位机 > 下位机"))
        # self.label_down.setText(_translate("MainWindow", "下位机 > 上位机"))
        self.label.setText(_translate("MainWindow", "串口号"))
        self.pushButton_in.setText(_translate("MainWindow", "导入文件"))
        # self.pushButton_out.setText(_translate("MainWindow", "导出文件"))
        self.pushButton_2.setText(_translate("MainWindow", "打开串口"))
        # self.pushButton_4.setText(_translate("MainWindow", "刷新串口设备"))
        self.checkBox_3.setText(_translate("MainWindow", "HEX显示"))
        self.pushButton_3.setText(_translate("MainWindow", "清除窗口"))
        self.label_2.setText(_translate("MainWindow", "波特率"))
        self.checkBox_4.setText(_translate("MainWindow", "定时发送"))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.lineEdit_com.setText(_translate("MainWindow", "COM1"))
        self.label_7.setText(_translate("MainWindow", "ms/次"))
        self.label_4.setText(_translate("MainWindow", "数据位"))
        # self.label_3.setText(_translate("MainWindow", "字符串输入框："))
        self.label_5.setText(_translate("MainWindow", "停止位"))
        # self.lineEdit.setText(_translate("MainWindow", "123"))
        self.pushButton.setText(_translate("MainWindow", "单次发送"))
        # self.pushButtonsave.setText(_translate("MainWindow", "保存"))
        self.label_6.setText(_translate("MainWindow", "校验位"))
        self.checkBox.setText(_translate("MainWindow", "HEX发送"))
        self.checkBox_5.setText(_translate('MainWindow','crc权限校验'))
        # self.checkBox_2.setText(_translate("MainWindow", "发送新行"))


