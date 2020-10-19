# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vision.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# QtCore:包含了核心的非GUI功能。此模块用于处理时间、文件和目录、各种数据类型、流、URL、MIME类型、线程或进程。
# QtGui包含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本。
# qtwidgets模块包含创造经典桌面风格的用户界面提供了一套UI元素的类。


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):  # MainWindow，提供一个主应用程序窗口
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 990) # 调整大窗口
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AI = QtWidgets.QPushButton(self.centralwidget)
        #  格式为  a,b,c,d   a:离左轴间距 b：离上轴间距  c：矩形宽  d：矩形高
        self.AI.setGeometry(QtCore.QRect(1000, 275, 171, 51))  # AI还原框
        self.AI.setObjectName("AI")
        self.saveProgress = QtWidgets.QPushButton(self.centralwidget)
        self.saveProgress.setGeometry(QtCore.QRect(1000, 372, 171, 51))  # 保存进度框
        self.saveProgress.setObjectName("saveProgress")
        self.readProgress = QtWidgets.QPushButton(self.centralwidget)
        self.readProgress.setGeometry(QtCore.QRect(1000, 465, 171, 51))  # 读取进度框
        self.readProgress.setObjectName("readProgress")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(1000, 555, 171, 51))  # 重置框
        self.reset.setObjectName("reset")
        self.pictureChoose = QtWidgets.QPushButton(self.centralwidget)
        self.pictureChoose.setGeometry(QtCore.QRect(1000, 48, 171, 51))  # 选择图片框
        self.pictureChoose.setObjectName("pictureChoose")
        self.upset = QtWidgets.QPushButton(self.centralwidget)
        self.upset.setGeometry(QtCore.QRect(1000, 175, 171, 51))  # 打乱框
        self.upset.setObjectName("upset")
        self.showView = QtWidgets.QGraphicsView(self.centralwidget)
        self.showView.setGeometry(QtCore.QRect(60, 50, 902, 902))  # 操作视窗
        self.showView.setObjectName("showView")
        self.selectHard = QtWidgets.QSpinBox(self.centralwidget)
        self.selectHard.setGeometry(QtCore.QRect(1100, 123, 61, 31))  # 阶数栏
        self.selectHard.setObjectName("selectHard")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1000, 125, 91, 21))  # “选择阶数”汉字
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)   #MenuBar创建一个菜单栏
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "拼图小游戏"))    # 设置窗口的标题
        self.AI.setText(_translate("MainWindow", "AI还原"))
        self.saveProgress.setText(_translate("MainWindow", "保存进度"))
        self.readProgress.setText(_translate("MainWindow", "读取进度"))
        self.reset.setText(_translate("MainWindow", "重置"))
        self.pictureChoose.setText(_translate("MainWindow", "选择图片"))
        self.upset.setText(_translate("MainWindow", "打乱"))
        self.label.setText(_translate("MainWindow", "选择阶数："))

