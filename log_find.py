#!/usr/bin/env python
#from sys import argv
import os
import sys
import re
import fnmatch 

words = list(sys.argv)
path = "/Users/aditya/.logfind"
testpath =  "/Users/aditya/Desktop/Aditya/VMfiles/share/projects/Logfind/tests/Testingfiles/"

'''This fucntions lists all the files in the .logfind file by regular expressions''' 
def list_all_lines(logfind_path):
	for pattern in open(logfind_path, 'r').read().split('\n'):
		split_pattern = pattern.split('/')
		cut_first_element_in_pattern = split_pattern[len(split_pattern)-1:] 
		#print cut_first_element_in_patternx
		for File in os.listdir(testpath):
			for pattern in  cut_first_element_in_pattern:
				if re.match(pattern, File):
					newpattern = testpath + '/' +  File
					print newpattern
					print File
#list_all_lines("/Users/aditya/.logfind")

def check_file_content(pattern, dir):
	for file in dir:
		if re.match(pattern, file):
			print file
		#print pattern
check_file_content('[a-z0-9_]*.txt$', os.listdir(testpath))
'''
def check_file_content(pattern, filename):
	#logfind_file = open(list_all_lines(path), 'r').read().split()
	test_directory = os.listdir(testpath)
	print "this is a pattern:", pattern
	print "this is a the file name:", filename
	#print list_all_lines("/Users/aditya/.logfind")
	#for each_file in filename:
	if re.search(pattern, filename):
		print filename
		return True
	else:
		print "Not a correct format or file doesnt exsist in here", fil	
		return False
check_file_content(".py", "water.txt")
'''
'''def go_through_direc(path):
	dirs = os.listdir(path)
	files = []
	for logfiles in dirs:
		if os.path.isfile(path + '//' + logfiles):
			files.append(logfiles)
	return files

def open_file_logfind(files):# change te function name
	newfiles = []
	for pattern in open(path + '//' + ".logfind", 'r').read().split('\n'):
		for oldfile in files:
			if re.match(pattern, oldfile):
				newfiles.append(oldfile)	
	return newfiles

#open_file_logfind(go_through_direc(path))


def go_through_logfind(filelines):# change te function name
	newfilelines = []
	for newpattern in open(path + '/' + ".logfind", 'r').read().split('\n'):
		newfilelines.append(newpattern)
	return newfilelines

#go_through_logfind(open_file_logfind(go_through_direc(path)))	
	
def check_word_in_file(line):
	#for testfiles in testpath:
	#	print testpath
	pattern = open(path + '/' + ".logfind", 'r').read().split('\n')
	#print pattern
	for old_content in pattern:	
		content = open(testpath + '/' + old_content, 'r').read().split('\n')
		
		#print content
		#print content
		#if re.match (pattern, content):
			#print old_content
		counter = []
		for word in words[1:]: # comment this line
			for sentence in content:
				if word in sentence:
					counter.append(True)
				else:
					counter.append(False)					
		if False not in counter:	 					
	 		print old_content
		elif words[1] == '-o' and True in counter:
 			print old_content	

check_word_in_file(go_through_logfind(open_file_logfind(go_through_direc(path))))
'''
'''def regex(line):
	for content in open(path + '/' + ".logfind", 'r').read().split('\n'):
		if content
#regex()
for logfiles in dirs:
	if fnmatch.fnmatch(logfiles, '.logfind'):
		
		openlogfile = open(os.path.join(path,logfiles), 'r')

		for line in openlogfile.read().split('\n'):
			#print line
			if fnmatch.fnmatch(line, '*.txt'):
				#print line
				content = open(line, 'r').read()
				counter = []
				for word in words[1:]:
					if word in content:
						counter.append(True)	
					else:
						counter.append(False)
				if False not in counter:
	 				#print files
	 				print line	
 				elif words[1] == '-o' and True in counter:
 					#print files
					print line
			elif fnmatch.fnmatch(line, '*.py'):

				content = open(line, 'r').read()
				counter = []
				for word in words[1:]:
					if word in content:
						counter.append(True)	
					else:
						counter.append(False)
				if False not in counter:
	 				#print files
	 				print line	
 				elif words[1] == '-o' and True in counter:
 					#print files
					print line

			elif fnmatch.fnmatch(line, '*.doc'):

				content = open(line, 'r').read()
				counter = []
				for word in words[1:]:
					if word in content:
						counter.append(True)	
					else:
						counter.append(False)
				if False not in counter:
	 				#print files
	 				print line	
 				elif words[1] == '-o' and True in counter:
 					#print files
					print line		
	'''	


