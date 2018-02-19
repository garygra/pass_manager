# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_service.ui'
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
        Form.resize(400, 300)
        self.lbl_title_2 = QtGui.QLabel(Form)
        self.lbl_title_2.setGeometry(QtCore.QRect(0, 0, 401, 31))
        self.lbl_title_2.setObjectName(_fromUtf8("lbl_title_2"))
        self.lbl_service_2 = QtGui.QLabel(Form)
        self.lbl_service_2.setGeometry(QtCore.QRect(20, 50, 62, 20))
        self.lbl_service_2.setObjectName(_fromUtf8("lbl_service_2"))
        self.btn_gen_passwd = QtGui.QPushButton(Form)
        self.btn_gen_passwd.setGeometry(QtCore.QRect(20, 220, 361, 28))
        self.btn_gen_passwd.setObjectName(_fromUtf8("btn_gen_passwd"))
        self.btn_save_srv = QtGui.QPushButton(Form)
        self.btn_save_srv.setGeometry(QtCore.QRect(80, 260, 90, 28))
        self.btn_save_srv.setObjectName(_fromUtf8("btn_save_srv"))
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(220, 260, 90, 28))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 361, 32))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 110, 101, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 130, 361, 32))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 111, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txt_new_passwd = QtGui.QLineEdit(Form)
        self.txt_new_passwd.setGeometry(QtCore.QRect(20, 190, 361, 32))
        self.txt_new_passwd.setObjectName(_fromUtf8("txt_new_passwd"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.txt_new_passwd)
        Form.setTabOrder(self.txt_new_passwd, self.btn_gen_passwd)
        Form.setTabOrder(self.btn_gen_passwd, self.btn_save_srv)
        Form.setTabOrder(self.btn_save_srv, self.btn_cancel)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_title_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Add New Service</span></p></body></html>", None))
        self.lbl_service_2.setText(_translate("Form", "Service:", None))
        self.btn_gen_passwd.setText(_translate("Form", "Generate Random Password", None))
        self.btn_save_srv.setText(_translate("Form", "Save", None))
        self.btn_cancel.setText(_translate("Form", "Cancel", None))
        self.label.setText(_translate("Form", "Username:", None))
        self.label_2.setText(_translate("Form", "Password:", None))

