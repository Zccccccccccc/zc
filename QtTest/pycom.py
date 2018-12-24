from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
#from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from mainwindow import Ui_MainWindow
import sys
#from datetime import datetime
import serial
import serial.tools.list_ports
import time
from crc import getCRC
import PyQt5.sip
#from pyico import *



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.dic_show = {}

        
        # # 设置应用程序的窗口图标
        # self.setWindowIcon(QIcon(":/a.png"))

        
            
        #串口无效
        self.ser = None
        self.send_num = 0
        self.receive_num = 0
        #记录最后发送的回车字符的变量
        self.rcv_enter = ''
        

        #显示发送与接收的字符数量
        dis = '发送：'+ '{:d}'.format(self.send_num) + '  接收:' + '{:d}'.format(self.receive_num)
        # print(dis)
        self.statusBar.showMessage(dis)

        #刷新一下串口的列表
        # self.refresh()
        #串口号
        # self.comboBox.addItem('COM1')

        #波特率
        self.comboBox_2.addItem('115200')
        self.comboBox_2.addItem('57600')
        self.comboBox_2.addItem('56000')
        self.comboBox_2.addItem('38400')
        self.comboBox_2.addItem('19200')
        self.comboBox_2.addItem('14400')
        self.comboBox_2.addItem('9600')
        self.comboBox_2.addItem('4800')
        self.comboBox_2.addItem('2400')
        self.comboBox_2.addItem('1200')

        #数据位
        self.comboBox_3.addItem('8')
        self.comboBox_3.addItem('7')
        self.comboBox_3.addItem('6')
        self.comboBox_3.addItem('5')

        #停止位
        self.comboBox_4.addItem('1')
        self.comboBox_4.addItem('1.5')
        self.comboBox_4.addItem('2')

        #校验位
        self.comboBox_5.addItem('NONE')
        self.comboBox_5.addItem('ODD')
        self.comboBox_5.addItem('EVEN')

        #对testEdit进行事件过滤
        self.textEdit.installEventFilter(self)

        #实例化一个定时器
        self.timer = QTimer(self)

        self.timer_send= QTimer(self)
        #定时器调用读取串口接收数据
        self.timer.timeout.connect(self.recv)

        #定时发送
        self.timer_send.timeout.connect(self.send)

        #导入文件
        self.pushButton_in.clicked.connect(self.read)
        
        #发送数据按钮
        self.pushButton.clicked.connect(self.send)
        #打开关闭串口按钮
        self.pushButton_2.clicked.connect(self.open_close)

        #刷新串口外设按钮
        # self.pushButton_4.clicked.connect(self.refresh)

        #清除窗口
        self.pushButton_3.clicked.connect(self.clear)

        #定时发送
        self.checkBox_4.clicked.connect(self.send_timer_box)

        #波特率修改
        self.comboBox_2.activated.connect(self.baud_modify)

        #串口号修改
        # self.comboBox.activated.connect(self.com_modify)

        #执行一下打开串口
        self.open_close(True)
        self.pushButton_2.setChecked(True)

        # crc权限校验

    def read(self):
        file_name, ok = QFileDialog.getOpenFileName(self, '读取', "./")
        if ok:
            with open(file_name, 'r') as f:
                data = f.readlines()
                j = 8
                for i in data:
                    print(i)
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
                    self.gridLayout.addLayout(self.horizontalLayout_show, j, 0, 1, 1)
                    self.lineEditSS.setText(i)
                    j +=1
                    self.dic_show[self.lineEditSS] = self.checkBox_show





    #刷新一下串口
    # def refresh(self):
    #     #查询可用的串口
    #     plist=list(serial.tools.list_ports.comports())
    #
    #     if len(plist) <= 0:
    #         print("No used com!");
    #         self.statusBar.showMessage('没有可用的串口')
    #
    #
    #     else:
    #         #把所有的可用的串口输出到comboBox中去
    #         self.comboBox.clear()
    #
    #         for i in range(0, len(plist)):
    #             plist_0 = list(plist[i])
    #             self.comboBox.addItem(str(plist_0[0]))

            
    #事件过滤
    def eventFilter(self, obj, event):
        #处理textEdit的键盘按下事件
        if event.type() == event.KeyPress:
            
            if self.ser != None:
                if event.key() == QtCore.Qt.Key_Up:
                    
                    #up 0x1b5b41 向上箭头
                    send_list = []
                    send_list.append(0x1b)
                    send_list.append(0x5b)
                    send_list.append(0x41)
                    input_s = bytes(send_list)

                    num = self.ser.write(input_s)
                elif event.key() == QtCore.Qt.Key_Down:
                    #down 0x1b5b42 向下箭头
                    send_list = []
                    send_list.append(0x1b)
                    send_list.append(0x5b)
                    send_list.append(0x42)
                    input_s = bytes(send_list)

                    num = self.ser.write(input_s)
                else:    
                    #获取按键对应的字符
                    char = event.text()
                    num = self.ser.write(char.encode('utf-8'))
                self.send_num = self.send_num + num
                dis = '发送：'+ '{:d}'.format(self.send_num) + '  接收:' + '{:d}'.format(self.receive_num)
                self.statusBar.showMessage(dis)
            else:
                pass
            return True
        else:
            
            return False
        
        
    #重载窗口关闭事件
    def closeEvent(self,e):

        #关闭定时器，停止读取接收数据
        self.timer_send.stop()
        self.timer.stop()

        #关闭串口
        if self.ser != None:
            self.ser.close()

    #定时发送数据
    def send_timer_box(self):
        if self.checkBox_4.checkState():
            time = self.lineEdit_2.text()
            print(time)

            try:
                time_val = int(time, 10)
                print(time_val)
            except ValueError:
                QMessageBox.critical(self, 'pycom','请输入有效的定时时间!')
                return None

            if time_val <= 0:
                QMessageBox.critical(self, 'pycom','定时时间必须大于零!')
                return None
            #定时间隔发送
            self.timer_send.start(time_val)
            
        else:
            self.timer_send.stop()
            

    #清除窗口操作
    def clear(self):
        self.textEdit.clear()
        self.send_num = 0
        self.receive_num = 0
        dis = '发送：'+ '{:d}'.format(self.send_num) + '  接收:' + '{:d}'.format(self.receive_num)
        self.statusBar.showMessage(dis)
        

    #串口接收数据处理
    def recv(self):
        
        try:
            num = self.ser.inWaiting()
        except:

            self.timer_send.stop()
            self.timer.stop()
            #串口拔出错误，关闭定时器
            self.ser.close()
            self.ser = None

            
            #设置为打开按钮状态
            self.pushButton_2.setChecked(False)
            self.pushButton_2.setText("打开串口")
            print('serial error!')
            return None
        if(num > 0):
            #有时间会出现少读到一个字符的情况，还得进行读取第二次，所以多读一个
            data = self.ser.read(num)
            
            #调试打印输出数据
            #print(data)
            num = len(data)
            #十六进制显示
            if self.checkBox_3.checkState():
                out_s=''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                
                
                  
            else:    	
                #串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                out_s = data.decode('iso-8859-1')
                
                if self.rcv_enter == '\r':
                    #上次有回车未显示，与本次一起显示
                    out_s = '\r' + out_s
                    self.rcv_enter =''
                
                if out_s[-1] == '\r':
                    #如果末尾有回车，留下与下次可能出现的换行一起显示，解决textEdit控件分开2次输入回车与换行出现2次换行的问题
                    out_s = out_s[0:-1]
                    self.rcv_enter = '\r'
                    
            #先把光标移到到最后
            cursor = self.textEdit.textCursor()
            if(cursor != cursor.End):
                cursor.movePosition(cursor.End)
                self.textEdit.setTextCursor(cursor)
            
            #把字符串显示到窗口中去    
            self.textEdit.insertPlainText(out_s)    
                
            
            #统计接收字符的数量
            self.receive_num = self.receive_num + num
            dis = '发送：'+ '{:d}'.format(self.send_num) + '  接收:' + '{:d}'.format(self.receive_num)
            self.statusBar.showMessage(dis)
            
            #获取到text光标
            textCursor = self.textEdit.textCursor()
            #滚动到底部
            textCursor.movePosition(textCursor.End)
            #设置光标到text中去
            self.textEdit.setTextCursor(textCursor)
        else:
            #此时回车后面没有收到换行，就把回车发出去
            if self.rcv_enter == '\r':
                #先把光标移到到最后
                cursor = self.textEdit.textCursor()
                if(cursor != cursor.End):
                    cursor.movePosition(cursor.End)
                    self.textEdit.setTextCursor(cursor)
                self.textEdit.insertPlainText('\r')
                self.rcv_enter =''
               
        
    #串口发送数据处理
    def send(self):
        if self.ser != None:
            if self.checkBox.checkState() == False and self.checkBox_5.checkState() == False :
                print('00000')
                for i in self.dic_show:
                    if i.text() != "" and self.dic_show[i].checkState() != 0:
                        print(i.text())
                        input_s = bytes(i.text().encode('utf-8')).strip()
                        num = self.ser.write(input_s)
                        print(num)
                        self.send_num = self.send_num + num
                        dis = '发送：' + '{:d}'.format(self.send_num) + '  接收:' + '{:d}'.format(self.receive_num)
                        self.statusBar.showMessage(dis)
                        time.sleep(0.1)
                        print(input_s)
            elif self.checkBox_5.checkState() == True or self.checkBox.checkState() == False :
                print('11111')
                for i in self.dic_show:
                    if i.text() != "" and self.dic_show[i].checkState() != 0:
                        print(i.text())
                        input_s = bytes(i.text().encode('utf-8')).strip()
                        hex_crc = getCRC(input_s, len(input_s))
                        num = self.ser.write(hex_crc)
                        input_s = self.ser.write(input_s)
                        print(num)
                        print(input_s)
                        self.send_num = self.send_num + input_s
                        dis = '发送：' + '{:d}'.format(self.send_num) + '  接收:' + '{:d}'.format(self.receive_num)
                        self.statusBar.showMessage(dis)
                        time.sleep(0.1)
                        print(hex_crc)

            elif self.checkBox.checkState() == True or self.checkBox_5.checkState() == False:
                print('22222')
                for i in self.dic_show:
                    send_list = []
                    if i.text() != "" and self.dic_show[i].checkState() != 0:
                        input_s = i.text().strip()
                        while input_s != '':
                            try:
                                num = int(input_s[0:2], 16)
                            except ValueError:
                                QMessageBox.critical(self, 'pycom', '请输入十六进制数据，以空格分开!')
                                return None

                            input_s = input_s[2:].strip()
                            send_list.append(num)
                        input_s = bytes(send_list)
                        num1 = self.ser.write(input_s)
                        self.send_num = self.send_num + num1
                        dis = '发送：' + '{:d}'.format(self.send_num) + '  接收:' + '{:d}'.format(self.receive_num)
                        self.statusBar.showMessage(dis)
                        time.sleep(0.1)
                        print(input_s)

            else:
                print('33333')
                for i in self.dic_show:
                    send_list = []
                    if i.text() != "" and self.dic_show[i].checkState() != 0:
                        input_s = i.text().strip()
                        while input_s != '':
                            try:
                                num = int(input_s[0:2], 16)
                            except ValueError:
                                QMessageBox.critical(self, 'pycom', '请输入十六进制数据，以空格分开!')
                                return None

                            input_s = input_s[2:].strip()
                            send_list.append(num)
                        input_s = bytes(send_list)
                        hex_crc = getCRC(input_s,len(input_s))
                        num1 = self.ser.write(input_s)
                        numl_crc = self.ser.write(hex_crc)
                        self.send_num = self.send_num + num1
                        self.send_num_crc = self.send_num + numl_crc
                        dis = '发送：' + '{:d}'.format(self.send_num) + '  接收:' + '{:d}'.format(self.receive_num)
                        # dis_crc = '发送：' + '{:d}'.format(self.send_num_crc) + '  接收:' + '{:d}'.format(self.receive_num)
                        self.statusBar.showMessage(dis)
                        # self.statusBar.showMessage(dis_crc)
                        time.sleep(0.1)
                        print(input_s)
                        print(numl_crc)

        else:
            #停止发送定时器
            self.timer_send.stop()
            QMessageBox.critical(self, 'pycom','请打开串口')
        # if self.ser != None:
        #     input_s = self.lineEdit.text()
        #     if input_s != "":
        #
        #         # 发送字符
        #         if (self.checkBox.checkState() == False):
        #             if self.checkBox_2.checkState():
        #                 # 发送新行
        #                 input_s = input_s + '\r\n'
        #             input_s = input_s.encode('utf-8')
        #
        #         else:
        #             # 发送十六进制数据
        #             input_s = input_s.strip()  # 删除前后的空格
        #             send_list = []
        #             while input_s != '':
        #                 try:
        #                     num = int(input_s[0:2], 16)
        #
        #                 except ValueError:
        #                     print('input hex data!')
        #                     QMessageBox.critical(self, 'pycom', '请输入十六进制数据，以空格分开!')
        #                     return None
        #
        #                 input_s = input_s[2:]
        #                 input_s = input_s.strip()
        #
        #                 # 添加到发送列表中
        #                 send_list.append(num)
        #             input_s = bytes(send_list)
        #         print(input_s)
        #         # 发送数据
        #         try:
        #             num = self.ser.write(input_s)
        #         except:
        #
        #             self.timer_send.stop()
        #             self.timer.stop()
        #             # 串口拔出错误，关闭定时器
        #             self.ser.close()
        #             self.ser = None
        #
        #             # 设置为打开按钮状态
        #             self.pushButton_2.setChecked(False)
        #             self.pushButton_2.setText("打开串口")
        #             print('serial error send!')
        #             return None
        #
                # self.send_num = self.send_num + num
                # dis = '发送：' + '{:d}'.format(self.send_num) + '  接收:' + '{:d}'.format(self.receive_num)
                # self.statusBar.showMessage(dis)
        #         # print('send!')
        #     else:
        #         print('none data input!')
        #
        # else:
        #     # 停止发送定时器
        #     self.timer_send.stop()
        #     QMessageBox.critical(self, 'pycom', '请打开串口')

    #波特率修改
    def baud_modify(self):
        if self.ser != None:
            self.ser.baudrate = int(self.comboBox_2.currentText())
            
    #串口号修改
    # def com_modify(self):
    #     if self.ser != None:
    #         self.ser.port = self.comboBox.currentText()

        
    #打开关闭串口        
    def open_close(self, btn_sta):
        if btn_sta == True:
            try:
                #输入参数'COM13',115200
                
                self.ser = serial.Serial(self.lineEdit_com.text(), int(self.comboBox_2.currentText()), timeout=0.2)
            except:
                QMessageBox.critical(self, 'pycom','没有可用的串口或当前串口被占用')
                return None
            #字符间隔超时时间设置
            self.ser.interCharTimeout = 0.001    
            #1ms的测试周期
            self.timer.start(2)
            self.pushButton_2.setText("关闭串口")
            print('open')
        else:
            #关闭定时器，停止读取接收数据
            self.timer_send.stop()
            self.timer.stop()
            
            try:
                #关闭串口
                self.ser.close()
            except:
                QMessageBox.critical(self, 'pycom','关闭串口失败')
                return None
                
            self.ser = None
            self.pushButton_2.setText("打开串口")
            print('close!')





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    print(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

