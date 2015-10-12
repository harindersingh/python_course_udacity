import os
import string

def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir(r"H:\WORKSPACE\Udacity-Programming_Foundations_with_Python\prank")
	#print(file_list)
	saved_path = os.getcwd()
	#print(saved_path)
	os.chdir(r"H:\WORKSPACE\Udacity-Programming_Foundations_with_Python\prank")

	#(2) for each file, rename filename
	for file_name in file_list:
		print("Old Name - " + file_name)
		os.rename(file_name, file_name.translate(None, "0123456789"))
		print("New Name - " + file_name)

rename_files()