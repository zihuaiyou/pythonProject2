#
# -*- coding: utf-8 -*-
# # Created by: PyQt5 version 5.15.1 Author:zihuaiyou
# 石炭系安全加砂优化软件
import sys
from PyQt5.QtWidgets import *
import mainWin_2_UI
import mainWin_2_UI_input_1
import mainWin_2_UI_input_2
import mainWin_2_UI_child_1
import mainWin_2_UI_child_2

str_list = []


# 主界面 判断裂缝是否发育
class myMainWindow(QWidget, mainWin_2_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# 输入界面1 主界面选择否时弹出
class myInputWindow1(QMainWindow, mainWin_2_UI_input_1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# 输入界面2 主界面选择是时弹出
class myInputWindow2(QMainWindow, mainWin_2_UI_input_2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# 子界面1 对应输入界面1,输出风险等级
class myChildWindow1(QWidget, mainWin_2_UI_child_1.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# 子界面2 对应输入界面2,输出风险等级
class myChildWindow2(QWidget, mainWin_2_UI_child_2.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w1 = myMainWindow()
    w1_1 = myInputWindow1()
    w1_2 = myInputWindow2()
    w1_1_1 = myChildWindow1()
    w1_1_2 = myChildWindow2()

    # 显示主界面1
    w1.show()


    # 显示输入界面1
    def show_w1_1():
        w1_1.show()

        # 显示子界面1
        def show_w1_1_1():
            w1_1_1.show()

        # 绑定pushbutton
        w1_1.pushButton.clicked.connect(show_w1_1_1)


    # 显示输入界面2
    def show_w1_2():
        w1_2.show()

        # 显示子界面2
        def show_w1_1_2():
            w1_1_1.show()

        # 绑定pushbutton
        w1_2.pushButton.clicked.connect(show_w1_1_2)


    # 绑定pushbutton
    w1.pushButton_yes.clicked.connect(show_w1_2)
    w1.pushButton_no.clicked.connect(show_w1_1)

    app.exec_()
