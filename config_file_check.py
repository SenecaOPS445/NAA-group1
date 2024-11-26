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
            #quit

    #Creates a configuration file if no argument is provided
    elif len(sys.argv) == 1:
        #print('call backup_setup()')
        return 'backup_setup'
    
    #Instructs user on how to use the correct syntax for the script.
    else:
        print('This program can only accept 1, or no arguments. \n' + 'Execute without an argument to create a configuration file.\n' + 'Execute with 1 argument with the location of your configuration file.')


def run_backup():
    #Creates a list of parameters from the configuration file.
    f = open(sys.argv[1], 'r')
    read_config = f.read()
    config_parameter_list = read_config.split('\n')
    f.close()
    print (config_parameter_list)

    backup_src = config_parameter_list[0]
    dest_dir = config_parameter_list[1]

    #For a single file
    if os.path.isfile(backup_src):
        #source_file = config_parameter_list[0]
        cp_command = f"cp {config_parameter_list[0]} {dest_dir}"
        print('Backing up file')
        os.popen(cp_command)
        print('File has been backed up')

    #For an entire directory
    if os.path.isdir(backup_src):
        #source_dir = config_parameter_list[0]
        cp_command = f"cp -r {config_parameter_list[0]} {dest_dir}"
        print('Backing up directory')
        os.popen(cp_command)
        print('Directory has been backed up')


if __name__ == '__main__':
    x = config_file_check()
    if x == 'good_config_file':
        run_backup()
    
    if x == 'backup_setup':
        print('call backup_setup()')