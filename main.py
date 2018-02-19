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
import new_user_ui as new_user_gui
import delete_user_ui as del_user_gui
import new_srv_ui as new_srv_gui

class new_service_window(QDialog):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		self.ui = new_srv_gui.Ui_Form()
		self.ui.setupUi(self)

class del_user_window(QDialog):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		self.ui = del_user_gui.Ui_Form()
		self.ui.setupUi(self)
		self.ui.lbl_pass_error.hide()
		self.ui.lbl_username_error.hide()
		self.ui.btn_delete.clicked.connect(self.btn_delete_clicked)

	def btn_delete_clicked(self):
		user_to_del = str(self.ui.txt_username.text())
		pass_to_del = str(self.ui.txt_password_1.text())

		if df.user_name_exist(user_to_del):
			self.ui.lbl_username_error.hide()
			if df.valid_password(user_to_del, pass_to_del):
				self.ui.lbl_pass_error.hide()
				res = QMessageBox.question(self, "Sure?", "Delete " + user_to_del + "? \n (This action cannot be undo)", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
				if res == QMessageBox.Yes:
					df.delete_user(user_to_del)
				self.hide()
				
			else:
				self.ui.lbl_pass_error.show()
		else:
			self.ui.lbl_username_error.show()

		
class new_user_window(QDialog):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		self.ui = new_user_gui.Ui_Form()
		self.ui.setupUi(self)
		self.ui.lbl_pass_error.hide()
		self.ui.lbl_pass_error_len.hide()
		self.ui.lbl_username_error.hide()
		self.ui.btn_save.clicked.connect(self.btn_save_clicked)

	def btn_save_clicked(self):
		new_user   = str(self.ui.txt_username.text())
		new_pass_1 = str(self.ui.txt_password_1.text())
		new_pass_2 = str(self.ui.txt_password_2.text())
		data_correct = True
		# print len(str(new_pass_1)) 
		if len(new_pass_1) > 9:
			self.ui.lbl_pass_error_len.hide()
		else:
			data_correct = False
			self.ui.lbl_pass_error_len.show()

		if new_pass_1 == new_pass_2 :
			self.ui.lbl_pass_error.hide()
		else:
			data_correct = False
			self.ui.lbl_pass_error.show()

		if df.user_name_exist(new_user):
			data_correct = False
			self.ui.lbl_username_error.show()
		else:
			self.ui.lbl_username_error.hide()

		print data_correct
		if data_correct:
			df.add_new_user(new_user, new_pass_1)
			QMessageBox.about(self, "New user created", "New user created")
			self.hide()
			# msg = QMessageBox()
			# msg.setText("New user created")
			# msg.setStandardButtons(QMessageBox.Ok)
			# msg.show()


class logged_in_window(QDialog):
	user_file = ""
	user_passwd = ""
	cipher = None
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		self.ui = logged_in_gui.Ui_Form()
		self.ui.setupUi(self)
		self.ui.btn_show.clicked.connect(self.btn_show_clicked)
		self.ui.btn_new.clicked.connect(self.btn_new_clicked)
		
	def create_user_cipher(self):
		self.cipher = df.create_cypher_fn(self.user_passwd)

	def fill_services(self):
		services = df.get_user_services(self.user_file, self.cipher)

		self.ui.cbox_service.clear()
		self.ui.cbox_service.addItems(services)

	def btn_new_clicked(self):
		print "btn_clicked"
		# self.new_srv_w = new_service_window(self) 
		# self.new_srv_w.show()
		

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
		self.ui.btn_new_user.clicked.connect(self.btn_new_user_clicked)
		self.ui.btn_del_user.clicked.connect(self.btn_del_user_clicked)


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

	def btn_new_user_clicked(self, parent):
		self.new_user_w = new_user_window(self) 
		self.new_user_w.show()

	def btn_del_user_clicked(self, parent):
		self.del_user_w = del_user_window(self)
		self.del_user_w.show()
			

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myapp = Main_window()
	myapp.show()
	sys.exit(app.exec_())

