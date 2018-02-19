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
        Form.resize(403, 391)
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
        self.btn_show.setGeometry(QtCore.QRect(10, 240, 381, 28))
        self.btn_show.setObjectName(_fromUtf8("btn_show"))
        self.btn_erase = QtGui.QPushButton(Form)
        self.btn_erase.setGeometry(QtCore.QRect(10, 300, 381, 28))
        self.btn_erase.setObjectName(_fromUtf8("btn_erase"))
        self.btn_save_new_service = QtGui.QPushButton(Form)
        self.btn_save_new_service.setEnabled(False)
        self.btn_save_new_service.setGeometry(QtCore.QRect(10, 270, 381, 28))
        self.btn_save_new_service.setObjectName(_fromUtf8("btn_save_new_service"))
        self.txt_new_service = QtGui.QLineEdit(Form)
        self.txt_new_service.setEnabled(False)
        self.txt_new_service.setGeometry(QtCore.QRect(10, 80, 381, 32))
        self.txt_new_service.setObjectName(_fromUtf8("txt_new_service"))
        self.lbl_title_new_srv = QtGui.QLabel(Form)
        self.lbl_title_new_srv.setGeometry(QtCore.QRect(0, 10, 401, 31))
        self.lbl_title_new_srv.setObjectName(_fromUtf8("lbl_title_new_srv"))
        self.btn_add_new_service = QtGui.QPushButton(Form)
        self.btn_add_new_service.setGeometry(QtCore.QRect(300, 50, 90, 28))
        self.btn_add_new_service.setObjectName(_fromUtf8("btn_add_new_service"))
        self.btn_cancel_new_service = QtGui.QPushButton(Form)
        self.btn_cancel_new_service.setGeometry(QtCore.QRect(250, 50, 141, 28))
        self.btn_cancel_new_service.setObjectName(_fromUtf8("btn_cancel_new_service"))
        self.btn_gen_passwd = QtGui.QPushButton(Form)
        self.btn_gen_passwd.setEnabled(True)
        self.btn_gen_passwd.setGeometry(QtCore.QRect(189, 170, 201, 28))
        self.btn_gen_passwd.setObjectName(_fromUtf8("btn_gen_passwd"))
        self.lbl_new_srv_error = QtGui.QLabel(Form)
        self.lbl_new_srv_error.setGeometry(QtCore.QRect(70, 60, 141, 20))
        self.lbl_new_srv_error.setObjectName(_fromUtf8("lbl_new_srv_error"))
        self.btn_erase_yes = QtGui.QPushButton(Form)
        self.btn_erase_yes.setGeometry(QtCore.QRect(40, 350, 101, 28))
        self.btn_erase_yes.setObjectName(_fromUtf8("btn_erase_yes"))
        self.btn_erase_no = QtGui.QPushButton(Form)
        self.btn_erase_no.setGeometry(QtCore.QRect(259, 350, 101, 28))
        self.btn_erase_no.setObjectName(_fromUtf8("btn_erase_no"))
        self.lbl_erase_sure = QtGui.QLabel(Form)
        self.lbl_erase_sure.setGeometry(QtCore.QRect(120, 330, 171, 20))
        self.lbl_erase_sure.setObjectName(_fromUtf8("lbl_erase_sure"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.cbox_service, self.txt_new_service)
        Form.setTabOrder(self.txt_new_service, self.txt_username)
        Form.setTabOrder(self.txt_username, self.btn_gen_passwd)
        Form.setTabOrder(self.btn_gen_passwd, self.txt_passwd)
        Form.setTabOrder(self.txt_passwd, self.btn_save_new_service)
        Form.setTabOrder(self.btn_save_new_service, self.btn_show)
        Form.setTabOrder(self.btn_show, self.btn_erase)
        Form.setTabOrder(self.btn_erase, self.btn_add_new_service)
        Form.setTabOrder(self.btn_add_new_service, self.btn_cancel_new_service)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lbl_title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Usernames and Passwords Saved</span></p></body></html>", None))
        self.lbl_service.setText(_translate("Form", "Service:", None))
        self.lbl_username.setText(_translate("Form", "Username:", None))
        self.lbl_passwd.setText(_translate("Form", "Password:", None))
        self.btn_show.setText(_translate("Form", "Show", None))
        self.btn_erase.setText(_translate("Form", "Erase", None))
        self.btn_save_new_service.setText(_translate("Form", "Save Service", None))
        self.lbl_title_new_srv.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Add New Service</span></p></body></html>", None))
        self.btn_add_new_service.setText(_translate("Form", "New Service", None))
        self.btn_cancel_new_service.setText(_translate("Form", "Cancel New Service", None))
        self.btn_gen_passwd.setText(_translate("Form", "Generate Random Password", None))
        self.lbl_new_srv_error.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">Service already exist</span></p></body></html>", None))
        self.btn_erase_yes.setText(_translate("Form", "Erase Service!", None))
        self.btn_erase_no.setText(_translate("Form", "Dont Erase!", None))
        self.lbl_erase_sure.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ff5500;\">Sure To Erease Service?</span></p></body></html>", None))

