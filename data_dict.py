ins_real_data_dict = []
flow_real_data_dict = []
oilPressure_real_data_dict = []

path1_flow_data = r'.\txt文件\firstFile5\5flow_data.txt'
path1_ins_data = r'.\txt文件\firstFile5\5ins_data.txt'
path1_oilPressure_data = r'.\txt文件\firstFile5\5oilPressure_data.txt'

path2_flow_data = r'.\txt文件\third10\10flow_data.txt'
path2_ins_data = r'.\txt文件\third10\10ins_data.txt'
path2_oilPressure_data = r'.\txt文件\third10\10oilPressure_data.txt'

path3_flow_data = r'.\txt文件\second15\15flow_data.txt'
path3_ins_data = r'.\txt文件\second15\15ins_data.txt'
path3_oilPressure_data = r'.\txt文件\second15\15oilPressure_data.txt'

path4_flow_data = r'.\txt文件\four20\20flow_data.txt'
path4_ins_data = r'.\txt文件\four20\20ins_data.txt'
path4_oilPressure_data = r'.\txt文件\four20\20oilPressure_data.txt'

def read_data(path_flow_data, path_ins_data, path_oilPressure_data):
    with open(path_flow_data, 'r') as f1, open(path_ins_data, 'r') as f2,\
         open(path_oilPressure_data, 'r') as f3:
        line1 = f1.readline()
        line2 = f2.readline()
        line3 = f3.readline()
        while line1 and line2:
            flow_data = eval(line1)
            ins_data = eval(line2)
            oilPressure_data = eval(line3)
            ins_real_data_dict.append(ins_data)
            flow_real_data_dict.append(flow_data)
            oilPressure_real_data_dict.append(oilPressure_data)
            line1 = f1.readline()
            line2 = f2.readline()
            line3 = f3.readline()

# 读取firstFile5文件夹数据
read_data(path1_flow_data, path1_ins_data, path1_oilPressure_data)

# 读取third10文件夹数据
# read_data(path2_flow_data, path2_ins_data, path2_oilPressure_data)

# 读取second15文件夹数据
# read_data(path3_flow_data, path3_ins_data, path3_oilPressure_data)

# 读取four20文件夹数据
# read_data(path4_flow_data, path4_ins_data, path4_oilPressure_data)

# 数据刷新以及界面刷新时间都是1秒（1000ms）
'''
self.timer = QTimer()  # 窗口重绘定时器，负责每次刷新窗口
self.timer.timeout.connect(self.update)
self.timer.start(1000)  # 单位为毫秒

self.testTimer = QTimer()  # 数据定时器，负责每次刷新数据
self.testTimer.timeout.connect(self.testTimer_timeout_handle)
self.testTimer.start(1000)
'''
