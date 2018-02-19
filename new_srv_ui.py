# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_srv.ui'
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
        Form.resize(403, 315)
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
        self.txt_username.setEnabled(True)
        self.txt_username.setGeometry(QtCore.QRect(10, 140, 381, 32))
        self.txt_username.setObjectName(_fromUtf8("txt_username"))
        self.lbl_passwd = QtGui.QLabel(Form)
        self.lbl_passwd.setGeometry(QtCore.QRect(10, 180, 81, 20))
        self.lbl_passwd.setObjectName(_fromUtf8("lbl_passwd"))
        self.txt_passwd = QtGui.QLineEdit(Form)
        self.txt_passwd.setEnabled(True)
        self.txt_passwd.setGeometry(QtCore.QRect(10, 200, 381, 32))
        self.txt_passwd.setObjectName(_fromUtf8("txt_passwd"))
        self.btn_show = QtGui.QPushButton(Form)
        self.btn_show.setGeometry(QtCore.QRect(10, 230, 381, 28))
        self.btn_show.setObjectName(_fromUtf8("btn_show"))
        self.btn_save = QtGui.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(90, 270, 90, 28))
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(220, 270, 90, 28))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.txt_service = QtGui.QLineEdit(Form)
        self.txt_service.setGeometry(QtCore.QRect(10, 80, 381, 32))
        self.txt_service.setObjectName(_fromUtf8("txt_service"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.txt_service, self.txt_username)
        Form.setTabOrder(self.txt_username, self.txt_passwd)
        Form.setTabOrder(self.txt_passwd, self.btn_show)
        Form.setTabOrder(self.btn_show, self.btn_save)
        Form.setTabOrder(self.btn_save, self.btn_cancel)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">New Service</span></p></body></html>", None))
        self.lbl_service.setText(_translate("Form", "Service:", None))
        self.lbl_username.setText(_translate("Form", "Username:", None))
        self.lbl_passwd.setText(_translate("Form", "Password:", None))
        self.btn_show.setText(_translate("Form", "Generate Password", None))
        self.btn_save.setText(_translate("Form", "Save", None))
        self.btn_cancel.setText(_translate("Form", "Cancel", None))

