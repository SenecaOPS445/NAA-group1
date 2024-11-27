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


def run_backup(): #made change here
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
def backup_setup():
    print ('We noticed that you did not provide a config file, We are going to create one! \n')
    config_name = input('What would you like the name of your configuration to be?\n')
    config_name = (config_name + '.txt')
    src_path = input('Please enter the source file/directory path that you would like to back up starting from root:\n')
    dest_dir = input('Please enter the file path for where you would like to save the file starting from root:\n')
    compression = compress_type() #ryan
    list1 = [src_path, dest_dir, compression]
    f = open(config_name, 'w')
    for item in list1:
        f.write(str(item) + '\n')
    f.close()
    sys.argv.append(config_name)
    run_backup()
def compress_type():
    return 'bzip'
if __name__ == '__main__':
    x = config_file_check()
    if x == 'good_config_file':
        run_backup()
    
    if x == 'backup_setup':
        backup_setup()
    
    