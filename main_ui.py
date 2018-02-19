# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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
        Form.resize(400, 286)
        self.btn_exit = QtGui.QPushButton(Form)
        self.btn_exit.setGeometry(QtCore.QRect(150, 250, 90, 28))
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.txt_passwd = QtGui.QLineEdit(Form)
        self.txt_passwd.setGeometry(QtCore.QRect(110, 130, 191, 32))
        self.txt_passwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.txt_passwd.setEchoMode(QtGui.QLineEdit.Password)
        self.txt_passwd.setObjectName(_fromUtf8("txt_passwd"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 50, 62, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 110, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btn_login = QtGui.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(150, 190, 90, 28))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.txt_user = QtGui.QLineEdit(Form)
        self.txt_user.setGeometry(QtCore.QRect(110, 70, 191, 32))
        self.txt_user.setObjectName(_fromUtf8("txt_user"))
        self.btn_new_user = QtGui.QPushButton(Form)
        self.btn_new_user.setGeometry(QtCore.QRect(150, 220, 90, 28))
        self.btn_new_user.setObjectName(_fromUtf8("btn_new_user"))
        self.lbl_error = QtGui.QLabel(Form)
        self.lbl_error.setGeometry(QtCore.QRect(110, 160, 191, 20))
        self.lbl_error.setObjectName(_fromUtf8("lbl_error"))
        self.lbl_title_2 = QtGui.QLabel(Form)
        self.lbl_title_2.setGeometry(QtCore.QRect(10, 10, 401, 31))
        self.lbl_title_2.setObjectName(_fromUtf8("lbl_title_2"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.txt_user, self.txt_passwd)
        Form.setTabOrder(self.txt_passwd, self.btn_login)
        Form.setTabOrder(self.btn_login, self.btn_new_user)
        Form.setTabOrder(self.btn_new_user, self.btn_exit)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_exit.setText(_translate("Form", "Exit", None))
        self.label.setText(_translate("Form", "User:", None))
        self.label_2.setText(_translate("Form", "Password:", None))
        self.btn_login.setText(_translate("Form", "Login", None))
        self.btn_new_user.setText(_translate("Form", "New User", None))
        self.lbl_error.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">Wrong user or password</span></p></body></html>", None))
        self.lbl_title_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Enter Username and Password</span></p></body></html>", None))

