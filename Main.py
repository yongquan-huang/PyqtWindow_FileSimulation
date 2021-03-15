import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainWin import MainForm
from historyWin import history_data
from realtimeWin import realtime_data
from fileWindow import File_UpLoad

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("loginWindow")
        self.setFixedSize(650, 400)
        self.setWindowTitle("登录")

        # 绘制顶部文字
        self.text = "甘蔗联合收割机运行工况监测平台"
        logo_lable = QtWidgets.QLabel(self)
        logo_lable.setGeometry(QtCore.QRect(0, 50, self.width(), 30))
        # 字体风格和大小
        logo_lable.setStyleSheet("QWidget{color:black;font-weight:600;background: transparent;font-size:30px;}")
        logo_lable.setFont(QFont("Microsoft YaHei"))
        logo_lable.setAlignment(Qt.AlignCenter)
        logo_lable.setText(self.text)

        # 登录表单内容部分
        login_widget = QWidget(self)
        # login_widget.move(0, 140)
        login_widget.setGeometry(20, 120, 650, 260)

        hbox = QHBoxLayout()
        # 添加左侧logo
        logolb = QLabel(self)
        logopix = QPixmap("logo.jpg")
        logopix_scared = logopix.scaled(150, 100)
        logolb.setPixmap(logopix_scared)
        logolb.setAlignment(Qt.AlignCenter)
        hbox.addWidget(logolb, 1)

        # 添加右侧表单
        fmlayout = QFormLayout()
        lbl_workerid = QLabel("用户名:")
        lbl_workerid.setFont(QFont("Microsoft YaHei"))
        # lbl_workerid.setStyleSheet("QLabel{font-size:16px;color:white;}")
        led_workerid = QLineEdit()
        led_workerid.setFixedWidth(270)
        led_workerid.setFixedHeight(38)

        lbl_pwd = QLabel("密码:")
        lbl_pwd.setFont(QFont("Microsoft YaHei"))
        # lbl_pwd.setStyleSheet("QLabel{font-size:16px;color:white;}")
        led_pwd = QLineEdit()
        led_pwd.setEchoMode(QLineEdit.Password)
        led_pwd.setFixedWidth(270)
        led_pwd.setFixedHeight(38)

        btn_login = QPushButton("登录")
        btn_login.setFixedWidth(270)
        btn_login.setFixedHeight(40)
        btn_login.setFont(QFont("Microsoft YaHei"))
        btn_login.setObjectName("login_btn")
        btn_login.setStyleSheet("#login_btn{background-color:black;color:white;border:none;border-radius:4px;}")

        fmlayout.addRow(lbl_workerid, led_workerid)
        fmlayout.addRow(lbl_pwd, led_pwd)
        fmlayout.addWidget(btn_login)
        hbox.setAlignment(Qt.AlignCenter)
        # 调整间距
        fmlayout.setHorizontalSpacing(20)
        fmlayout.setVerticalSpacing(12)

        hbox.addLayout(fmlayout, 2)

        login_widget.setLayout(hbox)

        # 实现登录界面到其他界面跳转
        self.controller = Controller()
        btn_login.clicked.connect(self.controller.show_main)
        btn_login.clicked.connect(self.close)

        self.center()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("screen.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)
        self.drawLines(painter)

    def drawLines(self,qp):
        brush = QBrush(Qt.white)
        qp.setBrush(brush)
        qp.drawRect(40, 140, 560, 210)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Controller():
    def __init__(self):
        pass

    def show_main(self):
        self.main = MainForm()
        self.main.show()
        self.main.pushButton_3.clicked.connect(self.main.close)
        self.main.pushButton_3.clicked.connect(self.show_history)
        self.main.pushButton_2.clicked.connect(self.main.close)
        self.main.pushButton_2.clicked.connect(self.show_realtime)
        self.main.pushButton_4.clicked.connect(self.main.close)
        self.main.pushButton_4.clicked.connect(self.show_file)

    def show_realtime(self):
        self.realtime = realtime_data()
        self.realtime.show()
        self.realtime.pushButton.clicked.connect(self.end_timer)
        self.realtime.pushButton_3.clicked.connect(self.end_timer)
        self.realtime.pushButton_4.clicked.connect(self.end_timer)
        self.realtime.pushButton.clicked.connect(self.realtime.close)
        self.realtime.pushButton.clicked.connect(self.show_main)
        self.realtime.pushButton_3.clicked.connect(self.realtime.close)
        self.realtime.pushButton_3.clicked.connect(self.show_history)
        self.realtime.pushButton_4.clicked.connect(self.realtime.close)
        self.realtime.pushButton_4.clicked.connect(self.show_file)

    def show_history(self):
        self.history = history_data()
        self.history.show()
        self.history.pushButton.clicked.connect(self.history.close)
        self.history.pushButton.clicked.connect(self.show_main)
        self.history.pushButton_2.clicked.connect(self.history.close)
        self.history.pushButton_2.clicked.connect(self.show_realtime)
        self.history.pushButton_4.clicked.connect(self.history.close)
        self.history.pushButton_4.clicked.connect(self.show_file)

    def show_file(self):
        self.file = File_UpLoad()
        self.file.show()
        self.file.pushButton.clicked.connect(self.file.close)
        self.file.pushButton.clicked.connect(self.show_main)
        self.file.pushButton_2.clicked.connect(self.file.close)
        self.file.pushButton_2.clicked.connect(self.show_realtime)
        self.file.pushButton_3.clicked.connect(self.file.close)
        self.file.pushButton_3.clicked.connect(self.show_history)

    def end_timer(self):
        self.realtime.qieduandao.timer.stop()
        self.realtime.paifengji.timer.stop()
        self.realtime.shuiwen.timer.stop()
        self.realtime.youya.timer.stop()
        self.realtime.fadongji.timer.stop()
        self.realtime.shusongun.timer.stop()

def run_qt():
    app = QApplication(sys.argv)
    login = LoginForm()
    login.show()
    sys.exit(app.exec_())

run_qt()
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     controller = Controller()
#     controller.show_main()
#     sys.exit(app.exec_())