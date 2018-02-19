import os.path
import hashlib
import inspect
import codecs
import linecache
import os
from Crypto.Cipher import AES


data_dir = "data/"
file_users = data_dir + "users"

debbug = True

# def open_users_file():
	# file_users = open("data/users", "r+")
	# file_users = 

def user_login(username, passwd):
	if debbug:
		print_current_fn()
	user_file, user_passwd = get_user_file(username, passwd)

	return user_file, user_passwd


def get_user_file(username, passwd):
	user_hash_t = hash_fn(username)
	passwd_hash_t = hash_fn(passwd)
	user_file = None
	user_passwd = None

	if debbug: 
		print_current_fn()
		print "\tFile is:", file_users
		print "\tusername:", username, "hashed:", user_hash_t
		print "\tpasswd:", passwd , "hashed:", passwd_hash_t

	
	with open(file_users) as f:
		line = f.readline()
		# print line
		user_not_found = True
		while user_not_found and line :
			user_info = line.split(",")
			if debbug:
				print "user_info[0]: ", user_info[0]
				print "user_info[1]: ", user_info[1]
				print "user_info[2]: ", user_info[2]
				print "user_hash_t == user_info[1]", user_hash_t == user_info[1]
				print "passwd_hash_t == user_info[2]", passwd_hash_t == user_info[2]
			if user_hash_t == user_info[1] and passwd_hash_t == user_info[2]:
				if debbug:
					print "User and passwd match"
				user_not_found = False
				line = None
				user_file = data_dir + user_hash_t
				user_passwd = user_info[2]
			else:
				line = f.readline()
		return user_file,  user_passwd

def hash_fn(value):
	return hashlib.md5(value.encode()).hexdigest()

def get_user_services(user_file, cipher):
	if debbug:
		print_current_fn()
		print "user_file",user_file
		# print "user_passwd", user_passwd

	services_list = []
	line_num = 2

	

	while(True):
		line_aux = linecache.getline(user_file, line_num).splitlines()
		if not line_aux:
			break;
		line = line_aux[0]
		if debbug:
			print line
		line_num += 4	

		service = decrypt_fn(cipher, line)
		services_list.append(service)
	return services_list

def create_cypher_fn(key):
	if debbug:
		print_current_fn()
		print key
	return AES.new(key.encode(), AES.MODE_ECB) # AES cipher

def decrypt_fn(cipher, data):
	data_dec = codecs.escape_decode(data)[0]
	if debbug:
		print_current_fn()
		print "data:", data
		print "data len:", len(data)
		print "data_dec:", data_dec
	dec_data = cipher.decrypt(data_dec) # AES decrypt
	serv = dec_data.split(">")[0]
	if debbug:
		print "data_dec:", data_dec
		print "dec_data:", dec_data
		print "serv:", serv
	return serv

def get_username_and_passwd(user_file, srv_index, cipher):
	line_username = linecache.getline(user_file, 2 + 4 * srv_index).splitlines()[0] #.split(",")
	line_passwd = linecache.getline(user_file, 3 + 4 * srv_index).splitlines()[0] #.split(",")
	if debbug:
		print_current_fn()
		print "srv_index:", srv_index
		print "line_username:", line_username
		print "line_passwd:", line_passwd
	username = decrypt_fn(cipher, line_username)
	passwd = decrypt_fn(cipher, line_passwd)

	return username, passwd

def user_name_exist(username):
	if debbug:
		print_current_fn()
		print username

	user_hash = hash_fn(username)
	with open(file_users) as f:
		line = f.readline()
		found = False
		while(True):
			if not line:
				break
			user_n = line.split(",")[1]
			if user_n == user_hash:
				found = True
				break
			line = f.readline()


	return found

def valid_password(username, passwd):
	if debbug:
		print_current_fn()
		print "username:", username
		print "passwd:", passwd

	user_hash = hash_fn(username)
	passwd_hash = hash_fn(passwd)
	with open(file_users) as f:
		line = f.readline()
		found = False
		while(True):
			if not line:
				break
			user_n = line.split(",")[1]
			pass_n = line.split(",")[2]
			if user_n == user_hash and passwd_hash == pass_n:
				found = True
				break
			line = f.readline()


	return found

def add_new_user(username, passwd):
	file = open(file_users, "r")
	linelist = file.readlines()
	file.close()
	num_new_user = int(linelist[-1].split(",")[0]) + 1
	username_hash = hash_fn(username)
	passwd_hash = hash_fn(passwd)
	new_line = "\n" + str(num_new_user) + "," + username_hash + "," + passwd_hash + ","
	file_append = open(file_users, 'a')
	file_append.write(new_line)
	file_append.close()
	new_file = open(data_dir + username_hash, "w+")
	new_file.close()

def delete_user(username):
	if debbug:
		print_current_fn()
		print "username:", username

	user_hash = hash_fn(username)
	file = open(file_users, "r")
	linelist = file.readlines()
	file.close()

	file_write = open(file_users, "w")
	for line in linelist:
		if line.split(",")[1] == user_hash:
			pass
		else:
			file_write.write(line)
	os.remove(data_dir + user_hash)
	# with open(file_users, 'r+') as f:
	# 	line = f.readline()
	# 	found = False
	# 	while(True):
	# 		if not line:
	# 			break
	# 		user_n = line.split(",")[1]
	# 		if user_n == user_hash:
	# 			found = True
	# 			break
	# 		line = f.readline()


def dummy():
	print "Dummy function called :)"

def print_current_fn():
	print "--------------------"
	print inspect.stack()[1][3]