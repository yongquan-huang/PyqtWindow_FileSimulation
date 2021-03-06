# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from ftplib import FTP
from graph import files, Table

class File_UpLoad(QWidget):

    def __init__(self):
        super(File_UpLoad, self).__init__()
        self.setupUi(self)

    def setupUi(self, File_UpLoad):
        File_UpLoad.setObjectName("file upload")
        File_UpLoad.resize(1400, 756)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        File_UpLoad.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(File_UpLoad)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 532, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(File_UpLoad)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 50, 100, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.clicked.connect(self.file_upload)  # ???????????????ftp?????????????????????
        self.pushButton_5.clicked.connect(self.msg)
        # ????????????
        self.pushButton_6 = QtWidgets.QPushButton(File_UpLoad)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 50, 100, 30))
        self.pushButton_6.setObjectName("pushButton_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.clicked.connect(self.msg2)

        # self.checkBox = QtWidgets.QCheckBox(File_UpLoad)
        # self.checkBox.setGeometry(QtCore.QRect(20, 90, 160, 30))
        # self.checkBox.setObjectName("checkBox")
        # font = QtGui.QFont()
        # font.setFamily("Arial")
        # font.setPointSize(15)
        # self.checkBox.setFont(font)
        # self.checkBox_2 = QtWidgets.QCheckBox(File_UpLoad)
        # self.checkBox_2.setGeometry(QtCore.QRect(20, 130, 160, 30))
        # self.checkBox_2.setObjectName("checkBox_2")
        # font = QtGui.QFont()
        # font.setFamily("Arial")
        # font.setPointSize(15)
        # self.checkBox_2.setFont(font)
        # self.checkBox_3 = QtWidgets.QCheckBox(File_UpLoad)
        # self.checkBox_3.setGeometry(QtCore.QRect(20, 150, 71, 16))
        # self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(File_UpLoad)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 50, 71, 30))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.clicked.connect(self.setcheck)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.checkBox_4.setFont(font)
        # ??????????????????
        self.gridLayoutWidget = QtWidgets.QWidget(File_UpLoad)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(12, 80, 660, 500))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        self.table = Table()
        self.MaingridLayout.addWidget(self.table)
        self.table.show()
        # ?????????????????????
        self.table.row_num = self.table.tableWidget.rowCount()

        self.retranslateUi(File_UpLoad)
        QtCore.QMetaObject.connectSlotsByName(File_UpLoad)

    def retranslateUi(self, File_UpLoad):
        _translate = QtCore.QCoreApplication.translate
        File_UpLoad.setWindowTitle(_translate("File_UpLoad", "????????????"))
        self.pushButton.setText(_translate("File_UpLoad", "????????????"))
        self.pushButton_2.setText(_translate("File_UpLoad", "????????????????????????"))
        self.pushButton_3.setText(_translate("File_UpLoad", "????????????"))
        self.pushButton_4.setText(_translate("File_UpLoad", "????????????"))
        self.pushButton_5.setText(_translate("File_UpLoad", "????????????"))
        self.pushButton_6.setText(_translate("File_UpLoad", "????????????"))
        # self.checkBox.setText(_translate("File_UpLoad", "torque_data.txt"))
        # self.checkBox_2.setText(_translate("File_UpLoad", "ins_data.txt"))
        # self.checkBox_3.setText(_translate("File_UpLoad", "CheckBox"))
        self.checkBox_4.setText(_translate("File_UpLoad", "??????"))

    def file_upload(self):
        '''FTP????????????'''
        ftp = FTP()
        # ??????????????????2, ??????????????????
        ftp.set_debuglevel(2)

        # ??????ftp?????????
        # ?????????iP?????????port
        ftp.connect('47.102.99.195', 21)
        # ????????????????????????
        ftp.login('vsftpd', 'ftp123456')

        # ????????????
        # path = r'E:\???????????????\cane11.6\run\run2020\env2019\env'
        for row in range(self.table.row_num):
            if self.table.tableWidget.cellWidget(row,0).isChecked():
                fname = self.table.tableWidget.item(row,1).text()
                file_path = files[row][0] + '\\' + fname   # ???linux??????'/'??????window?????????'\\'
                print(file_path)
                f = open(file_path, 'rb')
                ftp.storbinary("STOR " + fname, f, 1024)   # ??????STOP?????????????????????
                f.close()
        # ins_data_path = r'E:\???????????????\cane11.6\run\run2020\env2019\env\ins_data.txt'
        # torque_data_path = r'E:\???????????????\cane11.6\run\run2020\env2019\env\torque_data.txt'
        # if self.checkBox.isChecked():
        #     f = open(torque_data_path, 'rb')
        #     ftp.storbinary("STOR torque_data.txt", f, 1024)
        #     f.close()
        # if self.checkBox_2.isChecked():
        #     f = open(ins_data_path, 'rb')
        #     ftp.storbinary("STOR ins_data.txt", f, 1024)
        #     f.close()
        # ???????????????????????????FTP??????
        ftp.set_debuglevel(0)
        ftp.quit()

    def setcheck(self):
        for row in range(self.table.row_num):
            if  self.checkBox_4.isChecked():
                self.table.tableWidget.cellWidget(row,0).setCheckState(Qt.Checked)
            else:
                self.table.tableWidget.cellWidget(row,0).setCheckState(Qt.Unchecked)

    def msg(self):
        '''??????????????????????????????'''
        QMessageBox.information(self, '??????', '????????????')

    def msg2(self):
        '''??????????????????????????????'''
        QMessageBox.information(self, '??????', '????????????')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = File_UpLoad()
    w.show()
    sys.exit(app.exec_())