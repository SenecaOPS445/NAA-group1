#!/usr/bin/env python3
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
                print('call config_reader()')
                #run_backup()
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
    print ('We noticed that you did not provide a configuration file, We are going to create one! \n  The configuration file will be saved in the current directory. ')
    config_name = input('What would you like the name of your configuration file to be?\n')
    config_name = (config_name + '.txt')
    src_path = input('Please enter the source file/directory path that you would like to back up starting from root:\n')
    dest_dir = input('Please enter the file path for where you would like to save the file starting from root:\n')
    #compression = compress_type() #ryan
    comp_type, src_type = compress_type()
    ####### Need log file destination -jonathon
    
    list1 = [src_path, dest_dir, comp_type, src_type]
    f = open(config_name, 'w')
    for item in list1:
        f.write(str(item) + '\n')
    f.close()
    sys.argv.append(config_name)
    run_backup()



def compress_type():
########################
#    The compress_type function will ask the user to type in a compress option between gzip or bz2  
#    A while loop will be used to make sure that the correct option has been selected.
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
    '''new code from jonathon'''
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
#           will write the line from f_in to f_out
            f_out.writelines(f_in)
#           Will close both files
            f_out.close()
            f_in.close()
#           print out c_file
            print(c_file)
            '''new code added by jon'''
            return c_file

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
            '''new code added by jon'''
            return c_file

    if src_type == 'dir':
#       file will equal the directory that will be compressed
        #This list isolates the file name from the file path
        isolate_name = file.split('/')
        folder_name = isolate_name[-1]
        if c_type == 'gzip':
#           c_folder will add .tar.gz at the end of the name
            c_folder = file + '.tar.gz'
#           will run the command to compress the directory in gzip format
            os.system('tar -zcvf' + c_folder + file)
#           command to see the what files are in the compressed directory
            view_c = os.system('tar -tf' + c_folder)
#           will print os.system command above
            print(view_c)
            '''new code by jon'''
            return c_folder

        if c_type == 'bz2':
#           c_folder will add .tar.bz2 at the end of the name
            c_folder = file + '.tar.bz2'
#           will run the command to compress the directory in bz2 format
            os.system('tar -cjvf' + c_folder + file)
#           command to see the what files are in the compressed directory
            view_c = os.system('tar -tf' + c_folder)
#           will print os.system command above
            print(view_c)
            '''new code by jon'''
            return c_folder



    #return str(c_type) -jonathon



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


    #For a single file
    if os.path.isfile(backup_src):
        #source_file = config_parameter_list[0]
        new_name = compression(comp_type, src_type, backup_src)
        cp_command = f"cp {new_name} {dest_dir}"
        print('Backing up file')
        
        os.popen(cp_command)
        print('File has been backed up')

    #For an entire directory
    if os.path.isdir(backup_src):
        #source_dir = config_parameter_list[0]
        new_name = compression(comp_type, src_type, backup_src)
        cp_command = f"cp -r {new_name} {dest_dir}"
        print('Backing up directory')
        
        os.popen(cp_command)
        print('Directory has been backed up')

if __name__ == '__main__':
    x = config_file_check()
    if x == 'good_config_file':
        run_backup()
    
    if x == 'backup_setup':
        backup_setup()
    
    