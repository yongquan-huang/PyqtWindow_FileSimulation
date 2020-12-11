import sys
from PyQt5.QtWidgets import QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import datetime

# 列出E:\甘蔗机网关\cane11.6\run\run2020\env2019\env目录下所有扩展名为txt的文件（文件名）
files = [fname for fname in os.listdir(r'E:\甘蔗机网关\cane11.6\run\run2020\env2019\env') if fname.endswith('.txt')]
# print(files)
class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(664, 500)
        conLayout = QHBoxLayout()
        # conLayout.setGeometry(QtCore.QRect(60, 77, 400, 300))

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(files))
        self.tableWidget.setColumnCount(4)
        conLayout.addWidget(self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(['', '文件名', '修改日期', '文件大小'])
        # 将列宽锁死
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        path = r'E:\甘蔗机网关\cane11.6\run\run2020\env2019\env'
        for row in range(len(files)):
            file_path = path + '\\' + files[row]

            # 获取文件大小
            fsize = int(os.path.getsize(file_path)) // 1000
            fsize = str(fsize) + 'KB'
            # print(str(fsize) + 'KB')

            # 获取文件最近的修改日期
            ftime = os.path.getmtime(r'E:\甘蔗机网关\cane11.6\run\run2020\env2019\env' + '\\' + files[0])
            date = datetime.datetime.fromtimestamp(ftime)
            ftime = date.strftime('%Y-%m-%d %H:%M:%S')
            # print(date.strftime('%Y-%m-%d %H:%M:%S'))

            # 填写表格信息 0复选框， 1文件名， 2修改日期， 3文件大小
            checkBox = QCheckBox()

            self.tableWidget.setCellWidget(row, 0, checkBox)
            fname_item = QTableWidgetItem(files[row])
            ftime_item = QTableWidgetItem(ftime)
            fsize_item = QTableWidgetItem(fsize)
            # 设置文本居中
            fname_item.setTextAlignment(Qt.AlignCenter)
            ftime_item.setTextAlignment(Qt.AlignCenter)
            fsize_item.setTextAlignment(Qt.AlignCenter)
            # 设置字体--"雅黑"
            fname_item.setFont(QFont("Arial"))
            ftime_item.setFont(QFont("Arial"))
            fsize_item.setFont(QFont("Arial"))
            self.tableWidget.setItem(row, 1, fname_item)
            self.tableWidget.setItem(row, 2, ftime_item)
            self.tableWidget.setItem(row, 3, fsize_item)
        # 将（0，0）的复选框勾选
        # self.tableWidget.cellWidget(0,0).setCheckState(Qt.Checked)
        # 判断（0，0）的复选框状态
        # if self.tableWidget.cellWidget(0,0).isChecked():
        #     print(True)
        # 打印（0，1）的文本
        # print(self.tableWidget.item(0,1).text())

        # 获取表格的行数
        # row_num = self.tableWidget.rowCount()
        # print(row_num)

        # 将表格变为禁止编辑
        # tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 设置表格为整行选择
        # tableWidget.setSelectionBehavior( QAbstractItemView.SelectRows)

        # 设置表格列宽
        self.tableWidget.setColumnWidth(0, 20)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 200)

        # 将行和列的大小设为与内容相匹配
        # self.tableWidget.resizeColumnsToContents()
        # self.tableWidget.resizeRowsToContents()

        # 表格表头的显示与隐藏
        # tableWidget.verticalHeader().setVisible(False)
        # tableWidget.horizontalHeader().setVisible(False)

        # 不显示表格单元格的分割线
        # tableWidget.setShowGrid(False)
        # 不显示垂直表头
        # tableWidget.verticalHeader().setVisible(False)

        # # 将第1行的单元格，设置成120的高度
        # tableWidget.setRowHeight(0, 120)

        self.setLayout(conLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
