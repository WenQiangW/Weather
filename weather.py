

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from weather_ui import Ui_MainWindow
import sys,time

import urllib.request
import gzip
import json

class mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_weather_data)

        self.lcdNumber.display(time.strftime("%X", time.localtime()))
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setMode(QLCDNumber.Dec)


        # 新建一个QTimer对象
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        # 信号连接到槽
        self.timer.timeout.connect(self.OntimeOut)

    def OntimeOut(self):
        self.lcdNumber.display(time.strftime("%X", time.localtime()))

    def get_weather_data(self):

        cityname = self.lineEdit.text()

        # 访问的url，其中urllib.parse.quote是将城市名转换为url的组件
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(cityname)
        # 发出请求并读取到weather_data
        weather_data = urllib.request.urlopen(url).read()
        # 以utf-8的编码方式解压数据
        weather_data = gzip.decompress(weather_data).decode('utf-8')
        # 将json数据转化为dict数据
        weather_dict = json.loads(weather_data)
        #print(weather_dict)
        if weather_dict.get('desc') == 'invilad-citykey':
            self.textEdit.setText("你输入的城市名有误，或者天气中心未收录你所在城市")
        elif weather_dict.get('desc') == 'OK':
            forecast = weather_dict.get('data').get('forecast')
            self.textEdit.setText(
                '城市：' + weather_dict.get('data').get('city') + '\n'
                '日期：' + forecast[0].get('date') + '\n' 
                '温度：' + weather_dict.get('data').get('wendu') + '℃\n' 
                '高温：' + forecast[0].get('high') + '\n'
                '低温: ' + forecast[0].get('low') + '\n'         
                '风向：' + forecast[0].get('fengxiang') + '\n' 
                '风力：' + forecast[0].get('fengli') + '\n' 
                '天气：' + forecast[0].get('type') + '\n' 
                '感冒：' + weather_dict.get('data').get('ganmao'))
            self.textEdit_2.setText(
                '日期：' + forecast[1].get('date') + '\n'
                '天气：' + forecast[1].get('type') + '\n'
                '高温：' + forecast[1].get('high') + '\n'
                '低温：' + forecast[1].get('low') + '\n'
                '风向：' + forecast[1].get('fengxiang') + '\n'
                '风力：' + forecast[1].get('fengli') + '\n'
                 '*************************\n'
                '日期：' + forecast[2].get('date') + '\n'
                '天气：' + forecast[2].get('type') + '\n'
                '高温：' + forecast[2].get('high') + '\n'
                '低温：' + forecast[2].get('low') + '\n'
                '风向：' + forecast[2].get('fengxiang') + '\n'
                '风力：' + forecast[2].get('fengli') + '\n'
                '*************************\n'
                '日期：' + forecast[3].get('date') + '\n'
                '天气：' + forecast[3].get('type') + '\n'
                '高温：' + forecast[3].get('high') + '\n'
                '低温：' + forecast[3].get('low') + '\n'
                '风向：' + forecast[3].get('fengxiang') + '\n'
                '风力：' + forecast[3].get('fengli') + '\n'
                '*************************\n'
                '日期：' + forecast[4].get('date') + '\n'
                '天气：' + forecast[4].get('type') + '\n'
                '高温：' + forecast[4].get('high') + '\n'
                '低温：' + forecast[4].get('low') + '\n'
                '风向：' + forecast[4].get('fengxiang') + '\n'
                '风力：' + forecast[4].get('fengli') + '\n')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mywindow()
    win.show()
    sys.exit(app.exec())
