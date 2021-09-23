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
import math
from scipy.optimize import fsolve

# 输入界面1参数
# resh 储层高度
# Q 排量
# E 弹性模量
# v 泊松比
# visc 粘度
# filt 滤失系数
# size 支撑剂粒径
# time 压裂时间

# 输入界面2参数
# pres_diff 主应力差
# appro_ang 逼近角
# net_pres 净压力
# pres_drop 缝内压降
# tens_stre 抗拉强度

flag = ""
level = ""


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

    def confirm(self):
        global flag
        # 读取输入参数(字符串)
        resh = self.lineEdit_resh.text() or 10
        Q = self.lineEdit_Q.text() or 7
        E = self.lineEdit_E.text() or 31
        v = self.lineEdit_v.text() or 0.2
        filt = self.lineEdit_filt.text() or 3.45
        size = self.comboBox_size.currentText()
        time = self.comboBox_time.currentText()

        if size == "40/70":
            size = 0.0004
        elif size == "70/140":
            size = 0.0002
        elif size == "40/70-70/140":
            size = 0.0003

        resh = float(resh)
        Q = float(Q)
        E = float(E) * (10 ** 9)
        v = float(v)
        filt = float(filt) * (10 ** -3)
        time = float(time[0:2])

        #  输入参数列表
        # list_input1 = [resh, Q, E, v, visc, filt, size]
        # print(list_input1, time)

        # list_input1 = [float(x) for x in list_input1]
        # list_input1.append(float(time[0:2]))

        def func1(L):
            return (Q * time / 2 - 2 * filt * math.sqrt(time) * resh * L - 0.449873187318 * resh * L * (
                    ((L * v * math.pi * Q) / (2 * E)) ** 0.25))

        L = fsolve(func1, [0])[0]
        print(L)

        w = size * 6
        # def func2(x):
        #     w = size * 6
        #     return ((math.fabs((math.pi * Q * v * (L-x)) / (2 * E))) ** 0.25) * 1000 - w
        # x = fsolve(func2, [0])
        x = L - 2 * E * (w ** 4) / ((0.4498 ** 4) * 3.14 * Q * v)
        print(x)

        temp = (L - x) / L
        print(temp)
        if temp < 0.086:
            flag = "等级Ⅲ"
        elif temp < 0.14 and temp > 0.086:
            flag = "等级Ⅱ"
        elif temp > 0.14:
            flag = "等级Ⅰ"


# 输入界面2 主界面选择是时弹出
class myInputWindow2(QMainWindow, mainWin_2_UI_input_2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def confirm(self):
        global level
        # 读取输入参数(字符串)
        pres_diff = float(self.lineEdit_pres_diff.text())
        appro_ang = float(self.lineEdit_appro_ang.text())
        net_pres = float(self.lineEdit_net_pres.text())
        pres_drop = float(self.lineEdit_pres_drop.text())
        tens_stre = float(self.lineEdit_tens_stre.text())

        appro_ang = (appro_ang / 180) * math.pi
        press1 = 2 * (net_pres - tens_stre - pres_drop) / (1 + math.cos(2 * appro_ang))
        press2 = 2 * (net_pres - tens_stre) / (1 + math.cos(2 * appro_ang))
        if pres_diff < press1 and pres_diff < press2:
            level = "低风险"
        else:
            level = "高风险"


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
            w1_1_1.lineEdit.setText(flag)

        # 绑定pushbutton
        w1_1.pushButton.clicked.connect(show_w1_1_1)


    # 显示输入界面2
    def show_w1_2():
        w1_2.show()

        # 显示子界面2
        def show_w1_1_2():
            w1_1_2.show()
            w1_1_2.lineEdit.setText(level)

        # 绑定pushbutton
        w1_2.pushButton.clicked.connect(show_w1_1_2)


    # 绑定pushbutton
    w1.pushButton_yes.clicked.connect(show_w1_2)
    w1.pushButton_no.clicked.connect(show_w1_1)

    app.exec_()
