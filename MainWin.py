from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *
import sys
# from SerialCommunication import WorkThread
# from SerialCommunication import genqieqiyouya_y, genqieqiliuliang_y, shusonggunyouya_y, shusonggunliuliang_y,qieduandaoyouya_y, \
# qieduandaoliuliang_y, paifengjiyouya_y, paifengjiliuliang_y, erjishusongyouya_y, erjishusongliuliang_y, shuiwen_y, youya_y, fadongji_y
from run.run2020.env2019.env.app.CloudConn.cane_harvester import torque_real_data_dict, ins_real_data_dict
import apprcc_rc

# 界面图片、文字以及5个扭矩，转速数据
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 756)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        # self.label.setText("")
        # self.label.setFixedWidth(1400)
        # self.label.setFixedHeight(26)
        #
        # img = QImage(":/pic/首页字体.png")
        # result = img.scaled(self.label.width(), self.label.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # self.label.setPixmap(QPixmap.fromImage(result))
        # self.label.setObjectName("label")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(556, 26, 838, 161))
        # self.label_2.setText("")
        # self.label_2.setFixedWidth(838)
        # self.label_2.setFixedHeight(161)
        # img2 = QImage(":/pic/首页工况机.png")
        # result2 = img2.scaled(self.label_2.width(), self.label_2.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # self.label_2.setPixmap(QPixmap.fromImage(result2))
        # self.label_2.setObjectName("label_2")

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 37, 555, 26))
        # 设置字体及其大小
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText('发动机工况参数')
        self.label.setAlignment(Qt.AlignCenter)

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(555, 37, 845, 26))
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setText('关键作业部件工况参数')
        self.label_2.setAlignment(Qt.AlignCenter)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 180, 830, 431))
        self.label_3.setText("")
        self.label_3.setFixedWidth(831)
        self.label_3.setFixedHeight(431)
        img3 = QImage(":/pic/首页机器图片.png")
        result3 = img3.scaled(self.label_3.width(), self.label_3.height(), Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        self.label_3.setPixmap(QPixmap.fromImage(result3))
        self.label_3.setObjectName("label_3")

        # 关键作业部件工况参数马达字体textlabel建立和设置
        # 根切器马达
        self.label1 = QLabel(self)
        self.label1.setGeometry(QtCore.QRect(555, 70, 169, 30))
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setText('根切器马达')
        self.label1.setAlignment(Qt.AlignCenter)
        # 输送辊马达
        self.label2 = QLabel(self)
        self.label2.setGeometry(QtCore.QRect(724, 70, 169, 30))
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setText('输送辊马达')
        self.label2.setAlignment(Qt.AlignCenter)
        # 切段刀辊马达
        self.label3 = QLabel(self)
        self.label3.setGeometry(QtCore.QRect(893, 70, 169, 30))
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label3.setFont(font)
        self.label3.setText('切段刀辊马达')
        self.label3.setAlignment(Qt.AlignCenter)
        # 排风机马达
        self.label4 = QLabel(self)
        self.label4.setGeometry(QtCore.QRect(1062, 70, 169, 30))
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label4.setFont(font)
        self.label4.setText('排风机马达')
        self.label4.setAlignment(Qt.AlignCenter)
        # 二级输送通道马达
        self.label5 = QLabel(self)
        self.label5.setGeometry(QtCore.QRect(1231, 70, 169, 30))
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label5.setFont(font)
        self.label5.setText('二级输送通道马达')
        self.label5.setAlignment(Qt.AlignCenter)

        # 扭矩，转速及其对应数字建立和设置
        # 根切器扭矩
        self.label6 = QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(555, 100, 84, 25))
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label6.setFont(font)
        self.label6.setText('扭矩：')
        self.label6.setAlignment(Qt.AlignCenter)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(623, 100, 100, 25))  # 坐标x、y,长宽
        self.label_4.setObjectName("label_4")
        font.setFamily("Arial")  # 字体的大小
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        # 根切器转速
        self.label7 = QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(555, 125, 84, 25))
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label7.setFont(font)
        self.label7.setText('转速：')
        self.label7.setAlignment(Qt.AlignCenter)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(623, 125, 100, 25))
        self.label_5.setObjectName("label_5")
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        # 输送辊马达扭矩
        self.label8 = QLabel(self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(724, 100, 84, 25))
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label8.setFont(font)
        self.label8.setText('扭矩：')
        self.label8.setAlignment(Qt.AlignCenter)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(792, 100, 100, 25))
        self.label_6.setObjectName("label_6")
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
        # 输送辊马达转速
        self.label9 = QLabel(self.centralwidget)
        self.label9.setGeometry(QtCore.QRect(724, 125, 84, 25))
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label9.setFont(font)
        self.label9.setText('转速：')
        self.label9.setAlignment(Qt.AlignCenter)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(792, 125, 100, 25))
        self.label_7.setObjectName("label_7")
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)
        # 切段刀辊马达扭矩
        self.label10 = QLabel(self.centralwidget)
        self.label10.setGeometry(QtCore.QRect(893, 100, 84, 25))
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label10.setFont(font)
        self.label10.setText('扭矩：')
        self.label10.setAlignment(Qt.AlignCenter)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(961, 100, 100, 25))
        self.label_8.setObjectName("label_8")
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)
        # 切段刀辊马达转速
        self.label11 = QLabel(self.centralwidget)
        self.label11.setGeometry(QtCore.QRect(893, 125, 84, 25))
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label11.setFont(font)
        self.label11.setText('转速：')
        self.label11.setAlignment(Qt.AlignCenter)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(971, 125, 100, 25))
        self.label_9.setObjectName("label_9")
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)
        # 排风机马达扭矩
        self.label12 = QLabel(self.centralwidget)
        self.label12.setGeometry(QtCore.QRect(1062, 100, 84, 25))
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label12.setFont(font)
        self.label12.setText('扭矩：')
        self.label12.setAlignment(Qt.AlignCenter)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1130, 100, 100, 25))
        self.label_10.setObjectName("label_10")
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)
        # 排风机马达转速
        self.label13 = QLabel(self.centralwidget)
        self.label13.setGeometry(QtCore.QRect(1062, 125, 84, 25))
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label13.setFont(font)
        self.label13.setText('转速：')
        self.label13.setAlignment(Qt.AlignCenter)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1130, 125, 100, 25))
        self.label_11.setObjectName("label_9")
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)
        # 二级输送通道马达扭矩
        self.label14 = QLabel(self.centralwidget)
        self.label14.setGeometry(QtCore.QRect(1231, 100, 84, 25))
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label14.setFont(font)
        self.label14.setText('扭矩：')
        self.label14.setAlignment(Qt.AlignCenter)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1299, 100, 100, 25))
        self.label_12.setObjectName("label_10")
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)
        # 二级输送通道马达转速
        self.label15 = QLabel(self.centralwidget)
        self.label15.setGeometry(QtCore.QRect(1231, 125, 84, 25))
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label15.setFont(font)
        self.label15.setText('转速：')
        self.label15.setAlignment(Qt.AlignCenter)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1299, 125, 100, 25))
        self.label_13.setObjectName("label_9")
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 77, 400, 300))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 387, 180, 180))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.MaingridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.MaingridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout_2.setObjectName("MaingridLayout_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(180, 387, 180, 180))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.MaingridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.MaingridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout_3.setObjectName("MaingridLayout_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(360, 387, 180, 180))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.MaingridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.MaingridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout_4.setObjectName("MaingridLayout_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setObjectName("addWinAction")
        self.toolBar.addAction(self.addWinAction)
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 3, 532, 37))
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
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QTimer()  # 窗口重绘定时器，负责每次刷新窗口
        self.timer.timeout.connect(self.update)
        self.timer.start(100)  # 单位为毫秒

        self.testTimer = QTimer()  # 数据定时器，负责每次刷新数据
        self.testTimer.timeout.connect(self.testTimer_timeout_handle)
        self.testTimer.start(10)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "实时数据"))
        # self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        # self.addWinAction.setText(_translate("MainWindow", "显示仪表盘"))
        # self.addWinAction.setToolTip(_translate("MainWindow", "显示仪表盘"))
        self.pushButton.setText(_translate("history_data", "实时数据"))
        self.pushButton_2.setText(_translate("history_data", "实时数据波形显示"))
        self.pushButton_3.setText(_translate("history_data", "历史数据"))
        self.pushButton_4.setText(_translate("history_data", "文件管理"))

    def testTimer_timeout_handle(self):
        genqieqiyouya = torque_real_data_dict.get('1_torque_ch', 0)
        shusonggunyouya = torque_real_data_dict.get('2_torque_ch', 0)
        qieduandaoyouya = torque_real_data_dict.get('3_torque_ch', 0)
        paifengjiyouya = torque_real_data_dict.get('4_torque_ch', 0)
        erjishusongyouya = torque_real_data_dict.get('5_torque_ch', 0)
        self.label_4.setText(str(genqieqiyouya))
        self.label_5.setText( "TextLabel")
        self.label_6.setText(str(shusonggunyouya))
        self.label_7.setText("TextLabel")
        self.label_8.setText(str(qieduandaoyouya))
        self.label_9.setText("TextLabel")
        self.label_10.setText(str(paifengjiyouya))
        self.label_11.setText("TextLabel")
        self.label_12.setText(str(erjishusongyouya))
        self.label_13.setText("TextLabel")

# 仪表盘数据——发动机转速
class GaugePanel(QWidget):
    def __init__(self):
        super(GaugePanel, self).__init__()
        self.setWindowTitle("GaugePanel")
        self.setMinimumWidth(250)
        self.setMinimumHeight(250)

        self.timer = QTimer()  # 窗口重绘定时器，负责每次刷新窗口
        self.timer.timeout.connect(self.update)
        self.timer.start(100) #单位为毫秒

        self.testTimer = QTimer()  #数据定时器，负责每次刷新数据
        self.testTimer.timeout.connect(self.testTimer_timeout_handle)
        self.testTimer.start(10)

        self.lcdDisplay = QLCDNumber(self) #数据显示框
        self.lcdDisplay.setDigitCount(3)
        self.lcdDisplay.setMode(QLCDNumber.Dec)
        self.lcdDisplay.setSegmentStyle(QLCDNumber.Flat)
        self.lcdDisplay.setStyleSheet('border:2px solid green;color:green;background:silver')

        self.startAngle = 120# 以QPainter坐标方向为准,时钟的3点钟方向为0，然后以顺时针增加。建议画个草图看看
        self.endAngle = 60  # 以以QPainter坐标方向为准
        self.scaleMainNum = 10  # 主刻度数
        self.scaleSubNum = 10  # 主刻度被分割份数
        self.minValue = 0
        self.maxValue = 200  #200
        self.title = '转速×1000r/min'
        self.value = 0
        self.minRadio = 1  # 缩小比例,用于计算刻度数字，表示一小格代表多少
        self.decimals = 1  # 小数位数

    @pyqtSlot()
    def testTimer_timeout_handle(self):
        self.value = ins_real_data_dict.get('engine_speed', 0)
        # self.value = self.value + 1
        # if self.value > self.maxValue:
        #     self.value = self.minValue

    def setScaleMainNUm(self, scalemainnum):  #设置数据值的个数方法
        self.scaleMainNum = scalemainnum

    def setScaleSubNum(self, scalesubnum):  #设置主刻度被分割份数方法
        self.scaleSubNum = scalesubnum

    def setMinMaxValue(self, min, max):  #设置表盘最大值最小值的方法
        self.minValue = min
        self.maxValue = max

    def setTitle(self, title):  #设置表盘名字的方法
        self._title = title

    def setValue(self, value):  #设置表盘开始值的方法
        self.value = value

    def setMinRadio(self, minRadio):  #设置表盘一小格代表多少
        self.minRadio = minRadio

    def setDecimals(self, decimals):  #设置小数位数
        self.decimals = decimals

    def paintEvent(self, event):
        side = min(self.width(), self.height())

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)  # painter坐标系原点移至widget中央
        # 缩放painterwidget坐标系，使绘制的时钟位于widge中央,即钟表支持缩放，这里200是设定仪表盘的原始大小
        painter.scale(side / 200, side / 200)

        self.drawPanel(painter)  # 画外框表盘
        self.drawScaleNum(painter)  # 画刻度数字
        self.drawScaleLine(painter)  # 画刻度线
        self.drawTitle(painter)  # 画标题备注
        self.drawValue(painter)  # 画数显
        self.drawIndicator(painter)  # 画指针

    def drawPanel(self, p):
        p.save()
        radius = 100
        lg = QLinearGradient(-radius, -radius, radius, radius)
        # 渐变函数，参数：,y1,x2,y2；x1-x2:从左到右渐变，y1-y2:从上到下渐变
        lg.setColorAt(0, Qt.white)
        lg.setColorAt(1, Qt.black)
        p.setBrush(lg)    #设置画刷
        p.setPen(Qt.NoPen)  #设置没有边界线
        p.drawEllipse(-radius, -radius, radius * 2, radius * 2) #以该画刷填充外圆
        # 绘制椭圆，参数含义：左下角横坐标，左下角纵坐标，椭圆宽度（横向），椭圆高度（纵向）。

        p.setBrush(Qt.black)
        p.drawEllipse(-92, -92, 92 * 2, 92 * 2)  #以黑色画刷填充内圆
        p.restore()

    def drawScaleNum(self, p):
        p.save()
        p.setPen(Qt.white)
        startRad = self.startAngle * (3.14 / 180)
        stepRad = (360-(self.startAngle-self.endAngle)) * (3.14 / 180) / self.scaleMainNum

        fm = QFontMetricsF(p.font())
        for i in range(0, self.scaleMainNum + 1):
            sina = sin(startRad + i * stepRad)
            cosa = cos(startRad + i * stepRad)
            # scaleMainNum表示的是大的刻度分割
            tmpVal = i * ((self.maxValue - self.minValue) / self.scaleMainNum) + self.minValue
            tmpVal = tmpVal / self.minRadio  #数值/比例
            s = '{:.0f}'.format(tmpVal)
            w = fm.size(Qt.TextSingleLine, s).width()
            h = fm.size(Qt.TextSingleLine, s).height()
            x = 80 * cosa - w / 2
            y = 80 * sina - h / 2
            p.drawText(QRectF(x, y, w, h), s)

        p.restore()

    def drawScaleLine(self, p):
        p.save()
        p.rotate(self.startAngle)
        scaleNums = self.scaleMainNum * self.scaleSubNum  #总刻度数
        angleStep = (360-(self.startAngle-self.endAngle)) / scaleNums
        p.setPen(Qt.white)

        pen = QPen(Qt.white)
        for i in range(0, scaleNums + 1):
            if i > 0.8*scaleNums:
                pen.setColor(Qt.red)

            if i % self.scaleMainNum == 0:
                pen.setWidth(2)
                p.setPen(pen)
                p.drawLine(64, 0, 72, 0)
            else:
                pen.setWidth(1)
                p.setPen(pen)
                p.drawLine(67, 0, 72, 0)
            p.rotate(angleStep)

        p.restore()

    def drawTitle(self, p):
        p.save()
        p.setPen(Qt.white)
        fm = QFontMetrics(p.font())
        w = fm.size(Qt.TextSingleLine, self.title).width()
        p.drawText(-int(w/2), -45, self.title)
        p.restore()

    def drawValue(self, p):
        side = min(self.width(), self.height())
        w, h = side / 2 * 0.5, side / 2 * 0.25
        x, y = self.width() / 2 - w / 2, self.height() / 2 + side / 2 * 0.5
        self.lcdDisplay.setGeometry(int(x), int(y), int(w), int(h))

        ss = '{:.' + str(self.decimals) + 'f}'
        self.lcdDisplay.display(ss.format(self.value))

    def drawIndicator(self, p):
        p.save()
        polygon = QPolygon([QPoint(0, -2), QPoint(0, 2), QPoint(60, 0)])   # 画三角形
        degRotate = self.startAngle + (360-(self.startAngle-self.endAngle)) / (
                self.maxValue - self.minValue) * (self.value - self.minValue)
        # 画指针
        p.rotate(degRotate)
        halogd = QRadialGradient(0, 0, 60, 0, 0)  # 辐射渐变
        halogd.setColorAt(0, QColor(60, 60, 60))
        halogd.setColorAt(1, QColor(160, 160, 160))
        p.setPen(Qt.white)
        p.setBrush(halogd)
        p.drawConvexPolygon(polygon)
        p.restore()

        # 画中心点
        p.save()
        radGradient = QRadialGradient(0, 0, 10)  # 辐射渐变
        radGradient = QConicalGradient(0, 0, -90)  # 角度渐变
        radGradient.setColorAt(0.0, Qt.darkGray)
        radGradient.setColorAt(0.5, Qt.white)
        radGradient.setColorAt(1.0, Qt.darkGray)
        p.setPen(Qt.NoPen)
        p.setBrush(radGradient)
        p.drawEllipse(-5, -5, 10, 10)
        p.restore()


# 仪表盘数据——油压
class GaugePanel2(GaugePanel):
    def __init__(self):
        super(GaugePanel2, self).__init__()  # 继承父类的方法
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)
        self.startAngle = 210
        self.endAngle = 330
        self.scaleMainNum = 2
        self.scaleSubNum = 5
        self.maxValue = 10
        self.title = '油压×100KPa'

    @pyqtSlot()
    def testTimer_timeout_handle(self):
        self.value = ins_real_data_dict.get('oil_pressure', 0)

    def drawValue(self, p):
        side = min(self.width(), self.height())
        w, h = side / 2 * 0.7, side / 2 * 0.35
        x, y = self.width() / 2 - w / 2, self.height() / 2 + side / 2 * 0.2
        self.lcdDisplay.setGeometry(int(x), int(y), int(w), int(h))

        ss = '{:.' + str(self.decimals) + 'f}'
        self.lcdDisplay.display(ss.format(self.value))

    def paintEvent(self, event):
        side = min(self.width(), self.height())

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)  # painter坐标系原点移至widget中央
        # 缩放painterwidget坐标系，使绘制的时钟位于widge中央,即钟表支持缩放，这里200是设定仪表盘的原始大小
        painter.scale(side / 200, side / 200)

        self.drawPanel(painter)  # 画外框表盘
        self.drawScaleNum(painter)  # 画刻度数字
        self.drawScaleLine(painter)  # 画刻度线
        self.drawTitle(painter)  # 画标题备注
        self.drawValue(painter)  # 画数显
        self.drawIndicator(painter)  # 画指针

    def drawPanel(self, p):
        p.save()
        p.setBrush(Qt.black)
        p.drawRect(-92, -92, 92 * 2, 92 * 2)  # 以黑色画刷填充矩形
        p.restore()

    def drawScaleNum(self, p):
        p.save()
        p.setPen(Qt.green)
        startRad = self.startAngle * (3.14 / 180)
        stepRad = (self.endAngle - self.startAngle) * (3.14 / 180) / self.scaleMainNum

        fm = QFontMetricsF(p.font())
        for i in range(0, self.scaleMainNum + 1):
            sina = sin(startRad + i * stepRad)
            cosa = cos(startRad + i * stepRad)
            # scaleMainNum表示的是大的刻度分割
            tmpVal = i * ((self.maxValue - self.minValue) / self.scaleMainNum) + self.minValue
            tmpVal = tmpVal / self.minRadio  # 数值/比例
            s = '{:.0f}'.format(tmpVal)
            w = fm.size(Qt.TextSingleLine, s).width()
            h = fm.size(Qt.TextSingleLine, s).height()
            x = 80 * cosa - w / 2
            y = 80 * sina - h / 2
            if tmpVal >= 0.9 * self.maxValue:
                p.setPen(Qt.red)
            elif tmpVal >= 0.5 * self.maxValue:
                p.setPen(Qt.blue)
            p.drawText(QRectF(x, y, w, h), s)

        p.restore()

    def drawScaleLine(self, p):
        p.save()
        p.rotate(self.startAngle)
        scaleNums = self.scaleMainNum * self.scaleSubNum  # 总刻度数
        angleStep = (self.endAngle - self.startAngle) / scaleNums
        p.setPen(Qt.green)

        pen = QPen(Qt.green)
        for i in range(0, scaleNums + 1):
            if i > 0.8 * scaleNums:
                pen.setColor(Qt.red)
            elif i > 0.5 * scaleNums:
                pen.setColor(Qt.blue)

            if i % self.scaleMainNum == 0:
                pen.setWidth(2)
                p.setPen(pen)
                p.drawLine(64, 0, 72, 0)
            else:
                pen.setWidth(1)
                p.setPen(pen)
                p.drawLine(67, 0, 72, 0)
            p.rotate(angleStep)

        p.restore()

    def drawIndicator(self, p):
        p.save()
        polygon = QPolygon([QPoint(0, -2), QPoint(0, 2), QPoint(60, 0)])  # 画三角形
        degRotate = self.startAngle + (self.endAngle - self.startAngle) / (
                self.maxValue - self.minValue) * (self.value - self.minValue)
        # 画指针
        p.rotate(degRotate)
        halogd = QRadialGradient(0, 0, 60, 0, 0)  # 辐射渐变
        halogd.setColorAt(0, QColor(60, 60, 60))
        halogd.setColorAt(1, QColor(160, 160, 160))
        p.setPen(Qt.green)
        p.setBrush(halogd)
        p.drawConvexPolygon(polygon)
        p.restore()

        # 画中心点
        p.save()
        radGradient = QRadialGradient(0, 0, 10)  # 辐射渐变
        radGradient = QConicalGradient(0, 0, -90)  # 角度渐变
        radGradient.setColorAt(0.0, Qt.darkGray)
        radGradient.setColorAt(0.5, Qt.green)
        radGradient.setColorAt(1.0, Qt.darkGray)
        p.setPen(Qt.NoPen)
        p.setBrush(radGradient)
        p.drawEllipse(-5, -5, 10, 10)
        p.restore()

# 仪表盘数据——水温
class GaugePanel3(GaugePanel2):
    def __init__(self):
        super(GaugePanel3,self).__init__()
        self.scaleMainNum = 6  # 主刻度数
        self.scaleSubNum = 5  # 主刻度被分割份数
        self.maxValue = 120
        self.title = '水温℃'

    @pyqtSlot()
    def testTimer_timeout_handle(self):
        self.value = ins_real_data_dict.get('water_temperature', 0)

# 仪表盘数据——电池电压
class GaugePanel4(GaugePanel2):
    def __init__(self):
        super(GaugePanel4,self).__init__()
        self.scaleMainNum = 6  # 主刻度数
        self.scaleSubNum = 5  # 主刻度被分割份数
        self.maxValue = 32000
        self.minRadio = 1000
        self.title = '电压V'

    @pyqtSlot()
    def testTimer_timeout_handle(self):
        self.value = ins_real_data_dict.get('battery_voltage', 0)

# 完整界面展示
class MainForm(MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        self.child = GaugePanel()  #会在下面定义子窗口类childrenForm转速表
        self.child2 = GaugePanel2()
        self.child3= GaugePanel3()
        self.child4 = GaugePanel4()
        # 单击actionTst, 子窗口就会显示在主窗口的MaingridLayout中
        self.MaingridLayout.addWidget(self.child)
        self.child.show()
        self.MaingridLayout_2.addWidget(self.child2)
        self.child2.show()
        self.MaingridLayout_3.addWidget(self.child3)
        self.child3.show()
        self.MaingridLayout_4.addWidget(self.child4)
        self.child4.show()
        # self.work()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self,qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(0,40,555,605)
        brush = QBrush(Qt.white)
        qp.setBrush(brush)
        qp.drawRect(0, 37, 1400, 26)
        # 绘制马达5个矩形框
        pen = QPen(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRect(555, 63, 169, 150)
        qp.drawRect(724, 63, 169, 150)
        qp.drawRect(893, 63, 169, 150)
        qp.drawRect(1062, 63, 169, 150)
        qp.drawRect(1231, 63, 169, 150)
    # def work(self):   # 串口模拟采集数据的线程
    #     workthread = WorkThread()
    #     workthread.setDaemon(True)   #守护线程。当主进程结束后，子线程也会随之结束。
    #     workthread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

