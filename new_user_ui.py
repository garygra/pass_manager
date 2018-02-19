# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_user.ui'
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
        Form.resize(401, 267)
        self.lbl_title_2 = QtGui.QLabel(Form)
        self.lbl_title_2.setGeometry(QtCore.QRect(0, 0, 401, 31))
        self.lbl_title_2.setObjectName(_fromUtf8("lbl_title_2"))
        self.btn_save = QtGui.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(40, 230, 90, 28))
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.lbl_username = QtGui.QLabel(Form)
        self.lbl_username.setGeometry(QtCore.QRect(10, 40, 111, 20))
        self.lbl_username.setObjectName(_fromUtf8("lbl_username"))
        self.lbl_password_1 = QtGui.QLabel(Form)
        self.lbl_password_1.setGeometry(QtCore.QRect(10, 100, 121, 20))
        self.lbl_password_1.setObjectName(_fromUtf8("lbl_password_1"))
        self.lbl_password_2 = QtGui.QLabel(Form)
        self.lbl_password_2.setGeometry(QtCore.QRect(10, 160, 161, 20))
        self.lbl_password_2.setObjectName(_fromUtf8("lbl_password_2"))
        self.txt_username = QtGui.QLineEdit(Form)
        self.txt_username.setGeometry(QtCore.QRect(10, 60, 381, 32))
        self.txt_username.setObjectName(_fromUtf8("txt_username"))
        self.txt_password_1 = QtGui.QLineEdit(Form)
        self.txt_password_1.setGeometry(QtCore.QRect(10, 120, 381, 32))
        self.txt_password_1.setEchoMode(QtGui.QLineEdit.Password)
        self.txt_password_1.setObjectName(_fromUtf8("txt_password_1"))
        self.txt_password_2 = QtGui.QLineEdit(Form)
        self.txt_password_2.setGeometry(QtCore.QRect(10, 180, 381, 32))
        self.txt_password_2.setEchoMode(QtGui.QLineEdit.Password)
        self.txt_password_2.setObjectName(_fromUtf8("txt_password_2"))
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(270, 230, 90, 28))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lbl_pass_error = QtGui.QLabel(Form)
        self.lbl_pass_error.setGeometry(QtCore.QRect(10, 210, 191, 20))
        self.lbl_pass_error.setObjectName(_fromUtf8("lbl_pass_error"))
        self.lbl_username_error = QtGui.QLabel(Form)
        self.lbl_username_error.setGeometry(QtCore.QRect(80, 40, 191, 20))
        self.lbl_username_error.setObjectName(_fromUtf8("lbl_username_error"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.txt_username, self.txt_password_1)
        Form.setTabOrder(self.txt_password_1, self.txt_password_2)
        Form.setTabOrder(self.txt_password_2, self.btn_save)
        Form.setTabOrder(self.btn_save, self.btn_cancel)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_title_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">New User</span></p></body></html>", None))
        self.btn_save.setText(_translate("Form", "Save", None))
        self.lbl_username.setText(_translate("Form", "Username:", None))
        self.lbl_password_1.setText(_translate("Form", "Password:", None))
        self.lbl_password_2.setText(_translate("Form", "Repeat Password:", None))
        self.btn_cancel.setText(_translate("Form", "Cancel", None))
        self.lbl_pass_error.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">Password do not match</span></p></body></html>", None))
        self.lbl_username_error.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">Username exists</span></p></body></html>", None))

