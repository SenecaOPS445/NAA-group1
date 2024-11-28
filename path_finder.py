#!/usr/bin/env python3

'''
Krishan Sivanathan
OPS445
Assignment 2
Code for path_finder function
'''

# imports library of OS related functions
import os

# Creates and defines path_finder function
def path_finder():
	'''
	This function prompts user for a file or file path, and verifies whether it can be found on the system.
	If it does not exist, the user will get prompted to re-enter the file or path they wish to backup.
	If the file or file path exists, the provided input will be set as the source for the backup.
	'''

	# While Loop used to prompt user until valid path or filename which exists on system, is provided
	# path_exist is a value of 0 when the input provided does not exist on the system
	while path_exist = 0:
		# Prompts user for file or file path input
		path_given = input("Provide the filename or path you would like to backup: "
		# If file or folder exists
		if os.path.exists(path_given):
			print("Thank you :)")
			# Stores the validated input into a variable
			backup_source = path_given
			# Sets path_exist to value of 1 which will stop the loop
			path_exist = 1
		# If file or folder does not exist
		else:
			# Warns user about the error
			print("The provided input does not exist. Please try again.")
			# Loop will continue as path_exist is set to 0
			path_exist = 0

# END OF CODE
