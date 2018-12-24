# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QCheckBox
from Qt_test import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('仿下位机发送数据')
        self.dic_show = {}
        # number = 0
        #
        # for i in range(20):
        #     # data = f.readline()
        #     # datas.append(data + str(number))
        # self.datas = QCheckBox('check', self)  # 创建复选框
        #     print(self.datas)
        #     self.datas.setChecked(True)  # 将复选框选中
        #     self.datas.move(10, (number + 1) * 50)
        #     number += 1
        # self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        #         # self.gridLayout.setContentsMargins(0, 0, 0, 0)
        #         # self.gridLayout.setObjectName("gridLayout")
        #         # Translate = QtCore.QCoreApplication.translate
        #         # self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        #         # self.checkBox_8.setGeometry(QtCore.QRect(215, 435, 75, 25))
        #         # self.checkBox_8.setObjectName("checkBox_8")
        #         # self.checkBox_8.setText(Translate("MainWindow", '哔了狗'))




    def read(self):
        file_name, ok = QFileDialog.getOpenFileName(self, '读取', '\python_Code')
        if ok:
            with open(file_name, 'r') as f:
                data = f.readlines()
                j = 8
                for i in data:
                    self.horizontalLayout_show = QtWidgets.QHBoxLayout()
                    self.horizontalLayout_show.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
                    self.horizontalLayout_show.setContentsMargins(2, 8, 2, 0)
                    self.horizontalLayout_show.setSpacing(6)
                    self.lineEditSS = QtWidgets.QLineEdit(self.centralWidget)
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    self.lineEditSS.setSizePolicy(sizePolicy)
                    self.lineEditSS.setMinimumSize(QtCore.QSize(30, 20))
                    self.lineEditSS.setObjectName("lineEdit")
                    self.horizontalLayout_show.addWidget(self.lineEditSS)
                    self.checkBox_show = QtWidgets.QCheckBox(self.centralWidget)
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(self.checkBox_show.sizePolicy().hasHeightForWidth())
                    self.checkBox_show.setSizePolicy(sizePolicy)
                    self.checkBox_show.setObjectName("checkBox_show")
                    self.horizontalLayout_show.addWidget(self.checkBox_show)

                    spacerItem4 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_show.addItem(spacerItem4)
                    self.verticalLayout_6.addLayout(self.horizontalLayout_show)
                    self.lineEditSS.setText(i)





if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
