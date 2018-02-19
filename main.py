#!/usr/bin/python
import sys
import data_functions as df
# from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore
# , QtGui

# from main_ui import Ui_Form
import main_ui as main_gui
import logged_in_ui as logged_in_gui

class logged_in_window(QDialog):
	user_file = ""
	user_passwd = ""
	cipher = None
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		self.ui = logged_in_gui.Ui_Form()
		self.ui.setupUi(self)
		self.ui.btn_show.clicked.connect(self.btn_show_clicked)
		
		
	def create_user_cipher(self):
		self.cipher = df.create_cypher_fn(self.user_passwd)

	def fill_services(self):
		services = df.get_user_services(self.user_file, self.cipher)

		self.ui.cbox_service.clear()
		self.ui.cbox_service.addItems(services)
		

	def btn_show_clicked(self, parent):
		srv_index = self.ui.cbox_service.currentIndex() 
		username_srv_index, passwd_srv_index = df.get_username_and_passwd(self.user_file, srv_index, self.cipher)
		self.ui.txt_username.setText(username_srv_index)
		self.ui.txt_passwd.setText(passwd_srv_index)

		# print passwd_srv_index


class Main_window(QDialog):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		self.ui = main_gui.Ui_Form()
		self.ui.setupUi(self)
		self.ui.lbl_error.hide()
		# df.open_users_file()

		# self.btn_login = QPushButton("btn_login")
		self.ui.btn_login.clicked.connect(self.btn_login_clicked)
	def btn_login_clicked(self, parent):
		file, user_passwd = df.user_login(str(self.ui.txt_user.text()), str(self.ui.txt_passwd.text()))
		if file == None:
			self.ui.lbl_error.show()
		else:
			self.ui.lbl_error.hide()
			print "Open other window..."
			self.logged_in_w = logged_in_window(self)
			self.logged_in_w.user_file = file
			self.logged_in_w.user_passwd = user_passwd
			self.logged_in_w.create_user_cipher();
			self.logged_in_w.fill_services()
			self.logged_in_w.show()
			self.hide()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myapp = Main_window()
	myapp.show()
	sys.exit(app.exec_())

