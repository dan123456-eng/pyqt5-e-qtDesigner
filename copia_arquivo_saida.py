# ESSE É O CODIGO CONVERTIDO  LA DA GUI NO QtDesigner
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:03:13 2020

@author: Danilo Silva Correia
"""


# ESSE ARQUIVO NÃO PODE SER EDITADO
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PROTETO_01(object):
    def setupUi(self, PROTETO_01):
        PROTETO_01.setObjectName("PROTETO_01")
        PROTETO_01.resize(453, 419)
        self.gridLayout_2 = QtWidgets.QGridLayout(PROTETO_01)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(PROTETO_01)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(PROTETO_01)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(PROTETO_01)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(PROTETO_01)
        QtCore.QMetaObject.connectSlotsByName(PROTETO_01)

    def retranslateUi(self, PROTETO_01):
        _translate = QtCore.QCoreApplication.translate
        PROJETO_01.setWindowTitle(_translate("PROTETO_01", "Form"))
        self.pushButton.setText(_translate("PROTETO_01", "FAZ ALGO"))


