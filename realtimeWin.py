from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QSizePolicy
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
# from run.run2020.env2019.env.app.CloudConn.cane_harvester import torque_real_data_dict,ins_real_data_dict

class realtime_data(QWidget):
    def __init__(self):
        super(realtime_data,self).__init__()
        self.time_x = []
        self.time_x2 = []
        self.shuiwen_y = []
        self.youya_y = []
        self.fadongji_y = []
        self.genqieqiyouya_y = []
        self.genqieqiliuliang_y = []
        self.shusonggunyouya_y = []
        self.shusonggunliuliang_y = []
        self.qieduandaoyouya_y = []
        self.qieduandaoliuliang_y = []
        self.paifengjiyouya_y = []
        self.paifengjiliuliang_y = []
        self.erjishusongyouya_y = []
        self.erjishusongliuliang_y = []
        self.setupUi(self)
        self.MatplotlibWidget()


    def setupUi(self, realtime_data):
        realtime_data.setObjectName("history_data")
        realtime_data.resize(1400, 756)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        realtime_data.setFont(font)
        self.label = QtWidgets.QLabel(realtime_data)
        self.label.setGeometry(QtCore.QRect(20, 60, 91, 21))
        self.groupBox = QtWidgets.QGroupBox(realtime_data)
        self.groupBox.setGeometry(QtCore.QRect(-10, 90, 1400, 511))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 341, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(360, 20, 341, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 250, 341, 201))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(1060, 20, 341, 201))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(710, 250, 341, 201))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_5")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(1060, 250, 341, 201))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(140, 226, 51, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(500, 220, 51, 31))
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(710, 20, 341, 201))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_8")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(840, 220, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(1160, 225, 221, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(90, 450, 211, 20))
        self.label_6.setObjectName("label_6")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(360, 250, 341, 201))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_9")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(450, 450, 211, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(800, 450, 201, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(1160, 450, 171, 21))
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(realtime_data)
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

        self.retranslateUi(realtime_data)
        QtCore.QMetaObject.connectSlotsByName(realtime_data)

    def retranslateUi(self, realtime_data):
        _translate = QtCore.QCoreApplication.translate
        realtime_data.setWindowTitle(_translate("realtime_data", "实时数据波形显示"))
        self.label_2.setText(_translate("realtime_data", "水温"))
        self.label_3.setText(_translate("realtime_data", "油压"))
        self.label_4.setText(_translate("realtime_data", "发动机转速"))
        self.label_5.setText(_translate("realtime_data", "根切器马达(油压      流量      )"))
        self.label_6.setText(_translate("realtime_data", "输送辊马达(油压      流量      )"))
        self.label_7.setText(_translate("realtime_data", "切断刀马达(油压      流量      )"))
        self.label_8.setText(_translate("realtime_data", "排风机马达(油压      流量      )"))
        self.label_9.setText(_translate("realtime_data", "二级输送通道(油压      流量      )"))
        self.pushButton.setText(_translate("realtime_data", "实时数据"))
        self.pushButton_2.setText(_translate("realtime_data", "实时数据波形显示"))
        self.pushButton_3.setText(_translate("realtime_data", "历史数据"))
        self.pushButton_4.setText(_translate("realtime_data", "文件管理"))

    def paintEvent(self, e):  #绘制曲线图各文字所对应的线
        qp = QPainter()
        qp.begin(self)
        # 水温红色
        pen = QPen(Qt.red, 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(170,326,184,326)
        # 油压橙色
        pen.setColor(QColor(245, 154,35))
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(530, 326, 544, 326)
        # 发动机转速黄色
        pen = QPen(Qt.yellow, 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(910, 326, 924, 326)
        # # 根切器马达黑色
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(1247, 326, 1261, 326)
        pen = QPen(Qt.gray, 1, Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(1290, 326, 1304, 326)
        # 输送辊马达蓝色
        pen = QPen(Qt.blue, 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(177, 550, 191, 550)
        pen = QPen(QColor(129,211,248), 1, Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(220, 550, 234, 550)
        # 切断刀马达绿色
        pen = QPen(QColor(75, 121, 2), 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(536, 550, 550, 550)
        pen = QPen(QColor(202, 249, 130), 1, Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(580, 550, 594, 550)
        # 排风机马达粉色
        pen = QPen(QColor(240, 12, 203), 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(887, 550, 901, 550)
        pen = QPen(QColor(255, 192, 203), 1, Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(930, 550, 944, 550)
        # 二级输送通道马达棕色
        pen = QPen(QColor(165, 42, 42), 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(1259, 550, 1273, 550)
        pen = QPen(QColor(205, 133, 63), 1, Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(1303, 550, 1317, 550)

        qp.end()

    def MatplotlibWidget(self):
        # 水温图
        self.shuiwen = Shuiwen_Canvas(self.shuiwen_y)
        self.gridLayout.addWidget(self.shuiwen)
        # 油压图
        self.youya = Youya_Canvas(self.youya_y)
        self.gridLayout_2.addWidget(self.youya)
        # 发动机图
        self.fadongji = Fadongji_Canvas(self.fadongji_y)
        self.gridLayout_3.addWidget(self.fadongji)
        # 根切器图
        self.genqieqi = Genqieqi_Canvas(self.genqieqiyouya_y)
        self.gridLayout_4.addWidget(self.genqieqi)
        # 输送辊图
        self.shusongun = Shusonggun_Canvas(self.shusonggunyouya_y)
        self.gridLayout_5.addWidget(self.shusongun)
        # 切断刀图
        self.qieduandao = Qieduandao_Canvas(self.qieduandaoyouya_y)
        self.gridLayout_6.addWidget(self.qieduandao)
        # 排风机图
        self.paifengji = Paifengji_Canvas(self.paifengjiyouya_y)
        self.gridLayout_7.addWidget(self.paifengji)
        # 二级输送图
        self.erjishusong = Erjishusong_Canvas(self.erjishusongyouya_y)
        self.gridLayout_8.addWidget(self.erjishusong)

class Shuiwen_Canvas(FigureCanvas):
    '''水温图类'''

    def __init__(self, data_y, width=8.56, height=3.83, dpi=100):
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        # 新建一个绘图对象
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.data_y = data_y
        super(Shuiwen_Canvas, self).__init__(self.fig)
        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.timer = QtCore.QTimer(self)   # 窗口重绘定时器
        self.timer.timeout.connect(self.line)
        self.timer.start(1000)

    def line(self):
        from run.run2020.env2019.env.app.CloudConn.cane_harvester import ins_real_data_dict
        self.data_y.append(float(ins_real_data_dict.get('water_temperature', 0)))
        self.axes.plot(self.data_y, color='red')
        self.axes.grid(True)
        self.draw()
        if len(self.data_y) > 5:  # 当大于100时，绘图都不保留上一次绘图的结果，实现左移
            self.data_y = self.data_y[1:]
            self.axes.cla()

class Youya_Canvas(Shuiwen_Canvas):
    '''油压图类'''

    def __init__(self, data_y, width=8.56, height=3.83, dpi=100):
        super(Youya_Canvas, self).__init__(data_y, width, height, dpi)

    def line(self):
        from run.run2020.env2019.env.app.CloudConn.cane_harvester import ins_real_data_dict
        self.data_y.append(float(ins_real_data_dict.get('oil_pressure', 0)))
        self.axes.plot(self.data_y, color='orange')
        self.axes.grid(True)
        self.draw()
        if len(self.data_y) > 5:  # 当大于100时，绘图都不保留上一次绘图的结果，实现左移
            self.data_y = self.data_y[1:]
            self.axes.cla()

class Fadongji_Canvas(Shuiwen_Canvas):
    '''发动机图类'''

    def __init__(self, data_y, width=8.56, height=3.83, dpi=100):
        super(Fadongji_Canvas, self).__init__(data_y, width, height, dpi)

    def line(self):
        from run.run2020.env2019.env.app.CloudConn.cane_harvester import ins_real_data_dict
        self.data_y.append(float(ins_real_data_dict.get('engine_speed', 0)))
        self.axes.plot(self.data_y, color='yellow')
        self.axes.grid(True)
        self.draw()
        if len(self.data_y) > 5:  # 当大于100时，绘图都不保留上一次绘图的结果，实现左移
            self.data_y = self.data_y[1:]
            self.axes.cla()  # 画布清空

class Genqieqi_Canvas(Shuiwen_Canvas):
    '''根切器图类'''

    def __init__(self, data_y, width=8.56, height=3.83, dpi=100):
        super(Genqieqi_Canvas, self).__init__(data_y, width, height, dpi)

    def line(self):
        from run.run2020.env2019.env.app.CloudConn.cane_harvester import torque_real_data_dict
        self.data_y.append(torque_real_data_dict.get('1_torque_ch', 0))
        self.axes.plot(self.data_y, color='black')
        self.axes.grid(True)
        self.draw()
        if len(self.data_y) > 5:  # 当大于100时，绘图都不保留上一次绘图的结果，实现左移
            self.data_y = self.data_y[1:]
            self.axes.cla()  # 画布清空

class Shusonggun_Canvas(Shuiwen_Canvas):
    '''输送辊图类'''
    def __init__(self, data_y, width=8.56, height=3.83, dpi=100):
        super(Shusonggun_Canvas, self).__init__(data_y, width, height, dpi)

    def line(self):
        from run.run2020.env2019.env.app.CloudConn.cane_harvester import torque_real_data_dict
        self.data_y.append(torque_real_data_dict.get('2_torque_ch', 0))
        self.axes.plot(self.data_y, color='blue')
        self.axes.grid(True)
        self.draw()
        if len(self.data_y) > 5:  # 当大于100时，绘图都不保留上一次绘图的结果，实现左移
            self.data_y = self.data_y[1:]
            self.axes.cla()  # 画布清空

class Qieduandao_Canvas(Shuiwen_Canvas):
    '''切断刀图类'''

    def __init__(self, data_y, width=8.56, height=3.83, dpi=100):
        super(Qieduandao_Canvas, self).__init__(data_y, width, height, dpi)

    def line(self):
        from run.run2020.env2019.env.app.CloudConn.cane_harvester import torque_real_data_dict
        self.data_y.append(torque_real_data_dict.get('3_torque_ch', 0))
        self.axes.plot(self.data_y, color='#4B7902')
        self.axes.grid(True)
        self.draw()
        if len(self.data_y) > 5:  # 当大于100时，绘图都不保留上一次绘图的结果，实现左移
            self.data_y = self.data_y[1:]
            self.axes.cla()  # 画布清空

class Paifengji_Canvas(Shuiwen_Canvas):
    '''排风机图类'''

    def __init__(self, data_y, width=8.56, height=3.83, dpi=100):
        super(Paifengji_Canvas, self).__init__(data_y, width, height, dpi)

    def line(self):
        from run.run2020.env2019.env.app.CloudConn.cane_harvester import torque_real_data_dict
        self.data_y.append(torque_real_data_dict.get('4_torque_ch', 0))
        self.axes.plot(self.data_y, color='#F00CCB')
        self.axes.grid(True)
        self.draw()
        if len(self.data_y) > 5:  # 当大于100时，绘图都不保留上一次绘图的结果，实现左移
            self.data_y = self.data_y[1:]
            self.axes.cla()  # 画布清空

class Erjishusong_Canvas(Shuiwen_Canvas):
    '''二级输送图类'''

    def __init__(self, data_y, width=8.56, height=3.83, dpi=100):
        super(Erjishusong_Canvas, self).__init__(data_y, width, height, dpi)

    def line(self):
        from run.run2020.env2019.env.app.CloudConn.cane_harvester import torque_real_data_dict
        self.data_y.append(torque_real_data_dict.get('5_torque_ch', 0))
        self.axes.plot(self.data_y, color='#A52A2A')
        self.axes.grid(True)
        self.draw()
        if len(self.data_y) > 5:  # 当大于100时，绘图都不保留上一次绘图的结果，实现左移
            self.data_y = self.data_y[1:]
            self.axes.cla()  # 画布清空

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = realtime_data()
    w.show()
    sys.exit(app.exec_())