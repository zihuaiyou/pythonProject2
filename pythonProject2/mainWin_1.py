#
# -*- coding: utf-8 -*-
# # Created by: PyQt5 version 5.15.1 Author:zihuaiyou
#
import sys
from PyQt5.QtWidgets import *
import mainWin_1_UI
import mainWin_1_UI_child
from func import *

# # 断裂韧性
# toughness = ""
# # 储层应力
# res_stress = ""
# # 隔层应力
# inter_stress = ""
# # 液体压力
# liq_stress = ""
# # 储层厚度
# res_thick = ""
# # 期望控底高度比
# height_ratio = ""
# # 裂缝长度
# frac_len = ""
# # 粒径 & 粘度
# size_viscosity = ""

str_list = []


# 主界面 厚层控底加砂优化软件
class myMainWindow(QMainWindow, mainWin_1_UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def modify(self):
        # global toughness, res_stress, inter_stress, liq_stress, res_thick, \
        #     height_ratio, frac_len, size_viscosity
        global str_list

        # 读取输入参数(字符串)
        toughness = self.lineEdit_toughness.text()
        res_stress = self.lineEdit_res_stress.text()
        inter_stress = self.lineEdit_inter_stress.text()
        liq_stress = self.lineEdit_liq_stress.text()
        res_thick = self.lineEdit_res_thick.text()
        height_ratio = self.lineEdit_height_ratio.text()
        frac_len = self.lineEdit_frac_len.text()
        size_viscosity = self.comboBox.currentText()
        # 输入参数列表
        str_list = [toughness, res_stress, inter_stress, liq_stress, res_thick, height_ratio,
                    frac_len]
        # 默认值列表
        default_list = [1, 80, 84, 83.2, 10, 0.2, 100]
        # 设置默认值
        for index, value in enumerate(str_list):
            if value == "":
                str_list[index] = default_list[index]
        # 添加size_viscosity
        str_list.append(size_viscosity)



# 子界面 输出隔板设计参数
class myChildWindow(QWidget, mainWin_1_UI_child.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print(self)


    def showData(self):
        # self.lineEdit_gradient.setText("")
        # 1.计算压降梯度
        list_size_viscosity = ['40/70目、30cp', '40/70-70/140、30cp', '70/140目、30cp',
                               '40/70目、200cp', '40/70-70/140、200cp', '70/140目、200cp']
        list_gradient = [1.2, 2.65, 3, 3.3, 7.1, 10]
        dic_gradient = dict(zip(list_size_viscosity, list_gradient))
        # 压降梯度
        str_gradient = str(dic_gradient[str_list[-1]])
        self.lineEdit_gradient.setText(str_gradient)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w1 = myMainWindow()
    w1_1 = myChildWindow()
    # 显示主界面1
    w1.show()


    # 显示子界面1
    def show_w1_1():
        w1_1.show()
        w1_1.lineEdit_gradient.setText("")


    # 绑定pushbutton
    w1.pushButton.clicked.connect(show_w1_1)

    app.exec_()
