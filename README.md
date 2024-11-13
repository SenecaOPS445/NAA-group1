# Fall 2024 Assignment 2

__________________________
Details

This is a program that allows a user to backup a file, or entire directories (with the option of choosing the backup destination). Users can save backup configurations to a .txt file, which can be used to simplify back ups. 
Also provides functionality such as use with a crontab in order to automate backup intervals. 

__________________________
How will your program gather required input? 

Command line arguments if there is a saved configuration 




--------------------------
User inputs 

How will your program accomplish its requirements? 

Os.system module commands 

Os.path.exists()           

Loops 

If conditaionals 

Try clauses 

Tar 

Input() 

Print() 

.txt/XML file 

List[] 

Tar/gzip/7zip/bzip2/xz 

Openssl/gpg/encrypt.sh/cryptsetup 

Mkdir 

Cp/mv (local/external storage) 

Open(), close() 

Readlines()/readline()/read() 





--------------------------
How will output be presented?
Print message "<Datetime>: File <path> <has been/has been encrypted and>, backed up to <dest path> succesfully. File size <Mb float>. Destination space remaining <Gb in float>. 

Print message if unsuccessful 






--------------------------
What arguments or options will be included?

One argument for a saved config file. 




--------------------------
What aspects of development do you think will present the most challenge?

Managing all the loops, testing encryption, writing/reading config file, displaying live progress of operations. 

 

 

 
--------------------------
Eric's advice: 

To get to minimum viabale product, leave the compression and encryption and stuff until later, get basics ready first 

To save config into file, look into a JSON 

See if we can write in /var/log directory 

Use myvmlabs 

Use an exteneral gpg command 

Modify input function to make it a password  
