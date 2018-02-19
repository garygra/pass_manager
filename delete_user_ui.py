# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_user.ui'
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
        Form.resize(401, 208)
        self.lbl_title_2 = QtGui.QLabel(Form)
        self.lbl_title_2.setGeometry(QtCore.QRect(0, 0, 401, 31))
        self.lbl_title_2.setObjectName(_fromUtf8("lbl_title_2"))
        self.btn_delete = QtGui.QPushButton(Form)
        self.btn_delete.setGeometry(QtCore.QRect(40, 170, 90, 28))
        self.btn_delete.setObjectName(_fromUtf8("btn_delete"))
        self.lbl_username = QtGui.QLabel(Form)
        self.lbl_username.setGeometry(QtCore.QRect(10, 40, 111, 20))
        self.lbl_username.setObjectName(_fromUtf8("lbl_username"))
        self.lbl_password_1 = QtGui.QLabel(Form)
        self.lbl_password_1.setGeometry(QtCore.QRect(10, 100, 121, 20))
        self.lbl_password_1.setObjectName(_fromUtf8("lbl_password_1"))
        self.txt_username = QtGui.QLineEdit(Form)
        self.txt_username.setGeometry(QtCore.QRect(10, 60, 381, 32))
        self.txt_username.setObjectName(_fromUtf8("txt_username"))
        self.txt_password_1 = QtGui.QLineEdit(Form)
        self.txt_password_1.setGeometry(QtCore.QRect(10, 120, 381, 32))
        self.txt_password_1.setEchoMode(QtGui.QLineEdit.Password)
        self.txt_password_1.setObjectName(_fromUtf8("txt_password_1"))
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(260, 170, 90, 28))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lbl_username_error = QtGui.QLabel(Form)
        self.lbl_username_error.setGeometry(QtCore.QRect(80, 40, 191, 20))
        self.lbl_username_error.setObjectName(_fromUtf8("lbl_username_error"))
        self.lbl_pass_error = QtGui.QLabel(Form)
        self.lbl_pass_error.setGeometry(QtCore.QRect(80, 100, 191, 20))
        self.lbl_pass_error.setObjectName(_fromUtf8("lbl_pass_error"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.txt_username, self.txt_password_1)
        Form.setTabOrder(self.txt_password_1, self.btn_delete)
        Form.setTabOrder(self.btn_delete, self.btn_cancel)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_title_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Delete User</span></p></body></html>", None))
        self.btn_delete.setText(_translate("Form", "Delete", None))
        self.lbl_username.setText(_translate("Form", "Username:", None))
        self.lbl_password_1.setText(_translate("Form", "Password:", None))
        self.btn_cancel.setText(_translate("Form", "Cancel", None))
        self.lbl_username_error.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">Username does not exist</span></p></body></html>", None))
        self.lbl_pass_error.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">Invalid Password</span></p></body></html>", None))

