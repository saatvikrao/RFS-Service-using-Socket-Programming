import socket  
import os   
import os.path     

import crypto2

# creating a socket object 
s_obj = socket.socket()        
print ("Socket created successfully")

# allocate a port 
port = 12345               

# bind to the port 
s_obj.bind(('10.7.55.35', port))        
print ("socket binded to %s" %(port))

# put the socket into listening mode 
s_obj.listen(5)    
print ("socket is listening")  

# accept the connection request from the client 
c, address = s_obj.accept()
print ('Got connection from', address )

current_directory = os.getcwd()

while (True):
    cmd = c.recv(1024).decode()

    # command (1): CWD 
    if (cmd == 'CWD'):
        c.send(current_directory.encode())
    
    # command (2): LS 
    elif (cmd == 'LS'):
        str = ""
        directory_list = os.listdir(current_directory)

        for file in directory_list:
            str += file
            str += "$"
        
        str = str[:-1]
        c.send(str.encode())
    
    # command (3): CD 
    elif (cmd == 'CD'):
        # get path 
        getpath = c.recv(1024).decode()
        # try and except 
        try:
            os.chdir(getpath)
            current_directory = os.getcwd()
            c.send('OK'.encode())
        except:
            c.send('NOK'.encode())

    # command (4): DWD
    elif (cmd == "DWD"):
        request_file = c.recv(1024).decode() 
        does_file_exist = os.path.exists(request_file) # bool 

        if (does_file_exist == False):
            c.send('NOK'.encode())
            continue
        else:
            c.send('OK'. encode())
        
        # encode 
        crypto2.substitute_encode(request_file)

        with open(request_file, 'rb') as file_to_send:
            for data in file_to_send: c.sendall(data)

        crypto2.substitute_decode(request_file)


    # command (5): UPD 
    elif (cmd == "UPD"):
        # cuurent directory is the upload directory 
        download_directory = os.getcwd()

        file_name = c.recv(1024).decode()

        with open(os.path.join(download_directory, file_name), 'wb') as file_to_write:
            msg = c.recv(1024)
            if not msg: 
                break 
            file_to_write.write(msg) 
        file_to_write.close()

        # decode 
        crypto2.substitute_decode(file_name) 

    # if invalid command, close 
    else:
        # diplay error 
        print("Invalid command\n")
        c.send('error'.encode())
        c.close()

s_obj.close()
