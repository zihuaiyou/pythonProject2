# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin_2_UI_input_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 353)
        MainWindow.setMinimumSize(QtCore.QSize(703, 353))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_toughness = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_toughness.setObjectName("lineEdit_toughness")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_toughness)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_res_stress = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_res_stress.setObjectName("lineEdit_res_stress")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_res_stress)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_inter_stress = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_inter_stress.setObjectName("lineEdit_inter_stress")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inter_stress)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_liq_stress = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_liq_stress.setObjectName("lineEdit_liq_stress")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_liq_stress)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lineEdit_res_thick = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_res_thick.setObjectName("lineEdit_res_thick")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_res_thick)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_height_ratio = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_height_ratio.setObjectName("lineEdit_height_ratio")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_height_ratio)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_frac_len = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_frac_len.setObjectName("lineEdit_frac_len")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_frac_len)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_13)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "石炭系安全加砂优化软件"))
        self.label.setText(_translate("MainWindow", "请输入参数："))
        self.label_10.setText(_translate("MainWindow", "储层高度"))
        self.label_6.setText(_translate("MainWindow", "排量"))
        self.label_7.setText(_translate("MainWindow", "弹性模量"))
        self.label_8.setText(_translate("MainWindow", "泊松比"))
        self.label_11.setText(_translate("MainWindow", "滤失系数"))
        self.label_12.setText(_translate("MainWindow", "支撑剂粒径"))
        self.label_13.setText(_translate("MainWindow", "压裂时间"))
        self.comboBox.setItemText(0, _translate("MainWindow", "20min"))
        self.comboBox.setItemText(1, _translate("MainWindow", "40min"))
        self.comboBox.setItemText(2, _translate("MainWindow", "60min"))
        self.label_14.setText(_translate("MainWindow", "压裂液粘度"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
