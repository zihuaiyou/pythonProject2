# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin_2_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(423, 240)
        Form.setMinimumSize(QtCore.QSize(423, 240))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_yes = QtWidgets.QPushButton(Form)
        self.pushButton_yes.setGeometry(QtCore.QRect(60, 150, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_yes.setFont(font)
        self.pushButton_yes.setObjectName("pushButton_yes")
        self.pushButton_no = QtWidgets.QPushButton(Form)
        self.pushButton_no.setGeometry(QtCore.QRect(240, 150, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_no.setFont(font)
        self.pushButton_no.setObjectName("pushButton_no")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "石炭系安全加砂优化软件"))
        self.label.setText(_translate("Form", "石炭系安全加砂优化软件"))
        self.label_2.setText(_translate("Form", "裂缝是否发育："))
        self.pushButton_yes.setText(_translate("Form", "是"))
        self.pushButton_no.setText(_translate("Form", "否"))
