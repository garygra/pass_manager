# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logged_in.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(403, 292)
        self.cbox_service = QtGui.QComboBox(Form)
        self.cbox_service.setGeometry(QtCore.QRect(10, 80, 381, 30))
        self.cbox_service.setObjectName(_fromUtf8("cbox_service"))
        self.lbl_title = QtGui.QLabel(Form)
        self.lbl_title.setGeometry(QtCore.QRect(0, 10, 401, 31))
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.lbl_service = QtGui.QLabel(Form)
        self.lbl_service.setGeometry(QtCore.QRect(10, 60, 62, 20))
        self.lbl_service.setObjectName(_fromUtf8("lbl_service"))
        self.lbl_username = QtGui.QLabel(Form)
        self.lbl_username.setGeometry(QtCore.QRect(10, 120, 81, 20))
        self.lbl_username.setObjectName(_fromUtf8("lbl_username"))
        self.txt_username = QtGui.QLineEdit(Form)
        self.txt_username.setEnabled(False)
        self.txt_username.setGeometry(QtCore.QRect(10, 140, 381, 32))
        self.txt_username.setObjectName(_fromUtf8("txt_username"))
        self.lbl_passwd = QtGui.QLabel(Form)
        self.lbl_passwd.setGeometry(QtCore.QRect(10, 180, 81, 20))
        self.lbl_passwd.setObjectName(_fromUtf8("lbl_passwd"))
        self.txt_passwd = QtGui.QLineEdit(Form)
        self.txt_passwd.setEnabled(False)
        self.txt_passwd.setGeometry(QtCore.QRect(10, 200, 381, 32))
        self.txt_passwd.setObjectName(_fromUtf8("txt_passwd"))
        self.btn_show = QtGui.QPushButton(Form)
        self.btn_show.setGeometry(QtCore.QRect(10, 240, 90, 28))
        self.btn_show.setObjectName(_fromUtf8("btn_show"))
        self.btn_new = QtGui.QPushButton(Form)
        self.btn_new.setGeometry(QtCore.QRect(150, 240, 90, 28))
        self.btn_new.setObjectName(_fromUtf8("btn_new"))
        self.btn_erase = QtGui.QPushButton(Form)
        self.btn_erase.setGeometry(QtCore.QRect(300, 240, 90, 28))
        self.btn_erase.setObjectName(_fromUtf8("btn_erase"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Usernames and Passwords Saved:</span></p></body></html>", None))
        self.lbl_service.setText(_translate("Form", "Service:", None))
        self.lbl_username.setText(_translate("Form", "Username:", None))
        self.lbl_passwd.setText(_translate("Form", "Password:", None))
        self.btn_show.setText(_translate("Form", "Show", None))
        self.btn_new.setText(_translate("Form", "New", None))
        self.btn_erase.setText(_translate("Form", "Erase", None))

