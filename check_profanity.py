import urllib

def read_text():
	quotes = open("H:\WORKSPACE\GitHub\python_course_udacity\movie_quotes.txt")
	contents_of_files = quotes.read()
	print(contents_of_files)
	quotes.close()
	check_profanity(contents_of_files)

def check_profanity(text_to_check):
	connection = urllib.urlopen(
		"http://www.wdyl.com/profanity?q=" + text_to_check)
	output = connection.read()
	#print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alert!!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Could not scan the document properly.")

read_text()