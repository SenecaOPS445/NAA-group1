#!/usr/bin/env python3
#NAMES: Ryan Aquila, Jonathon Dimitrakopoulos, Umer Rizwan, Krishan Sivanathan and Dev Sudhirkumar Patel
#Assignment2 Final Version
#OPS445

import sys
import os

def config_file_check():
    '''This function determines if a backup configuration file exists, or if the user
    wants to create a new configuration file'''

    if len(sys.argv) == 2:
        #Checks if provided configuration file exists.
        try:
            f = open(sys.argv[1], 'r')
            read_config = f.read()
            f.close()
            #Prints error message if config file is empty
            if not read_config:
                print('ERROR: No contents in the configuration file. ')

            else:
                return 'good_config_file'


        except (FileExistsError, FileNotFoundError):
            print('ERROR: Unable to open or locate the configuration file.')
            sys.exit()
            #quit

    #Creates a configuration file if no argument is provided
    elif len(sys.argv) == 1:
        #print('call backup_setup()')
        return 'backup_setup'

    #Instructs user on how to use the correct syntax for the script.
    else:
        print('This program can only accept 1, or no arguments. \n' + 'Execute without an argument to create a configuration file.\n' + 'Execute with 1 argument with the location of your configuration file.')




def backup_setup():
 #  Prompting user for basic configuration so we can write it into config file
    print ('We noticed that you did not provide a configuration file, We are going to create one! \n  The configuration file will be saved in the current directory. ')
    config_name = input('What would you like the name of your configuration file to be?\n')
    config_name = (config_name + '.txt')
    src_path = input('Please enter the source file/directory path that you would like to back up starting from root:\n (HINT: DO NOT END DIRECTORY PATH WITH A BACKSLASH)')
    dest_dir = input('Please enter the file path for where you would like to save the file starting from root:\n')
    # prompts for compression type and src type by calling compress_type function
    comp_type, src_type = compress_type()

# create list of config parameters to split and write into config file
    list1 = [src_path, dest_dir, comp_type, src_type]
    f = open(config_name, 'w')
    for item in list1:
        f.write(str(item) + '\n')#writing to file line by line
    f.close()
    sys.argv.append(config_name)#append the newly created config file to cli agruments list so we dont have to make new function instead we can just call run_backup()
    run_backup()



def compress_type():
########################
#    The compress_type function will ask the user to type in a compress option between gzip or bz2 and a source type
#    A while loop will be used to make sure that the correct options have been selected.
#    if not the while loop will continue and will ask for the user input again.
#    If user has selected the right option then the while loop will end and will print a message saying what the user picked.
########################


#   This will print the options the user can choose from for their compress type
    print('Compression options are gzip or bz2')

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

#   Will ask the user if it is a file or directory
    src_type = input("dir or file?: ")

# If the src_type does not equal 'dir' or 'file' then it will go into a while loop
# it will end when src_type equals 'dir' or 'file'
    while src_type != 'dir' and src_type != 'file':
        print("Valid Source types are dir or file")
        src_type = input("Try again: ")
    print('You picked ' + src_type)

    return c_type, src_type



def compression(c_type, src_type, file):
    '''This function is responsible for the actual compression of the source file/directory'''
    import gzip
    import bz2
#   if src_type = file then it will run the code block to compress a file
    if src_type == 'file':
#       file will equal the name of the file that will be compress
        #file = input("enter file name: ")
        if c_type == 'gzip':
#           c_file will add .gz at the end of the name of the file
            c_file = file + '.gz'
#           f_in will equal the open file
            f_in = open(file, 'rb')
#           f_out will equal a open gzip file that we can write to
            f_out = gzip.open(c_file, 'wb')
#           will write each line from f_in to f_out
            f_out.writelines(f_in)
#           Will close both files
            f_out.close()
            f_in.close()
#           print out c_file
            print(c_file)
            return c_file

        if c_type == 'bz2':
#           c_file will add .gz at the end of the name of the file
            c_file = file + '.bz2'
#           f_in will equal the open file
            f_in = open(file, 'rb')
#           f_out will equal a open gzip file that we can write to
            f_out = bz2.open(c_file, 'wb')
#           will write each line from f_in to f_out
            f_out.writelines(f_in)
#           Will close both files
            f_out.close()
            f_in.close()
#           print out c_file
            print(c_file)
            return c_file

    if src_type == 'dir':
#       file will equal the directory that will be compressed
        #This list isolates the file name from the file path
        isolate_name = file.split('/')
#       Will take the last item in the list
        folder_name = isolate_name[-1]

        parent_directory_list = isolate_name[:-1]
#       Will make the list join as a file path
        parent_directory = '/'.join(parent_directory_list)


        if c_type == 'gzip':
#           c_folder will add .tar.gz at the end of the name
            c_folder = folder_name + '.tar.gz'
            print('This is what you are backing up:')
#           will run the command to compress the directory in gzip format
            os.system(f'cd {parent_directory} && tar -zcf {c_folder} {folder_name}')
            return c_folder

        if c_type == 'bz2':
#           c_folder will add .tar.bz2 at the end of the name
            c_folder = folder_name + '.tar.bz2'
#           will run the command to compress the directory in bz2 format
            print('This is what you are backing up:')
            os.system(f'cd {parent_directory} && tar -cjvf {c_folder} {folder_name}')
            #print('These are the files that have been backed up: \n' + str(view_c))
            return c_folder


def run_backup(): #made change here
    #Creates a list of parameters from the configuration file.
    f = open(sys.argv[1], 'r')
    read_config = f.read()
    config_parameter_list = read_config.split('\n')
    f.close()
    #print (config_parameter_list)

    backup_src = config_parameter_list[0]
    dest_dir = config_parameter_list[1]
    comp_type = config_parameter_list[2]
    src_type = config_parameter_list[3]

    import time
    #For a single file
    if os.path.isfile(backup_src):
        new_name = compression(comp_type, src_type, backup_src)
        cp_command = f"cp {new_name} {dest_dir}"
        print('Backing up file')
        time.sleep(2)
        os.popen(cp_command)
        print('File has been backed up')

    #For an entire directory
    if os.path.isdir(backup_src):
        new_name = compression(comp_type, src_type, backup_src)
        cp_command = f"cp -r {new_name} {dest_dir}"
        print('\nBacking up directory')
        time.sleep(2)
        os.popen(cp_command)
        print('Directory has been backed up')

if __name__ == '__main__':
    x = config_file_check()
    if x == 'good_config_file':
        run_backup()

    if x == 'backup_setup':
        backup_setup()