#!/usr/bin/env python3
#Author: Ryan Aquila

# RYAN AQUILA
# OPS445
#A2
# COMPRESS_TYPE FUNCTION

# Moduals that will be used inside the function
import gzip
import bz2
import os


def compress_type():
########################
#    The compress_type function will ask the user to type in a compress option between gzip or bz2  
#    A while loop will be used to make sure that the correct option has been selected.
#    if not the while loop will continue and will ask for the user input again.
#    If user has selected the right option then the while loop will end and will print a message saying what the user picked.
########################

#   This will print the options the user can choose from for their compress type
    print('Commpress options are gzip or bz2')

#   Will ask the user for their input    
    c_type = input('Select an option: ')

#   The while loop will run if c_type does not equal gzip or bz2
#   It will end if c_type equals one of the compress options
    while c_type != 'gzip' and c_type != 'bz2':
#       Will print the options again for the user
        print("Options are gzip or bz2")
#       Wil ask again for the user input
        c_type=input("Try again: ")
#   Will print what the user picked
    print('You picked ' + c_type)

#   Will ask the user is it is a file or directory
    dir_file = input("dir or file?: ")

#   if dir_file = file then it will run the code block to compress a file
   if dir_file == 'file':
#       file will equal the name of the file that will be compress
        file = input("enter file name: ")
        if c_type == 'gzip':
#           c_file will add .gz at the end of the name of the file
            c_file = file + '.gz'
#           f_in will equal the open file
            f_in = open(file, 'rb')
#           f_out will equal a open gzip file that we can write to
            f_out = gzip.open(c_file, 'wb')
#           will write the line from f_in to f_out
            f_out.writelines(f_in)
#           Will close both files
            f_out.close()
            f_in.close()
#           print out c_file
            print(c_file)

        if c_type == 'bz2':
#           c_file will add .gz at the end of the name of the file
            c_file = file + '.bz2'
#           f_in will equal the open file
            f_in = open(file, 'rb')
#           f_out will equal a open gzip file that we can write to
            f_out = bz2.open(c_file, 'wb')
#           will write the line from f_in to f_out
            f_out.writelines(f_in)
#           Will close both files
            f_out.close()
            f_in.close()
#           print out c_file
            print(c_file)

    if dir_file == 'dir':
#       folder will equal the directory that will be compressed
        folder = input('enter dir you want to compress: ')
        if c_type == 'gzip':
#           c_folder will add .tar.gz at the end of the name
            c_folder = folder + '.tar.gz'
#           will run the command to compress the directory in gzip format
            os.system('tar -zcvf' + c_folder + folder)
#           command to see the what files are in the compressed directory
            view_c = os.system('tar -tf' + c_folder)
#           will print os.system command above
            print(view_c)

        if c_type == 'bz2':
#           c_folder will add .tar.bz2 at the end of the name
            c_folder = folder + '.tar.bz2'
#           will run the command to compress the directory in bz2 format
            os.system('tar -cjvf' + c_folder + folder)
#           command to see the what files are in the compressed directory
            view_c = os.system('tar -tf' + c_folder)
#           will print os.system command above
            print(view_c)


    return str(c_type)

