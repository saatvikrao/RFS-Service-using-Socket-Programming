import socket 
import os  
import os.path

import crypto1 

# creating a socket and connecting it to the same port as sever 
s_obj = socket.socket()        
port = 12345              

s_obj.connect(('10.7.55.35', port)) 

# print to check if connected 
print("Connected to the server")
 
while (True):
    # taking input from the user 
    cmd = input().split(' ')
    # get command 
    getcmd = cmd[0]

    # command (1): CWD
    if (getcmd == "CWD"):
        s_obj.send(cmd[0].encode())
        print(s_obj.recv(1024).decode())

    # command (2): LS 
    elif (getcmd == "LS"):
        s_obj.send(cmd[0].encode())
        directory_list = s_obj.recv(1024).decode().split("$")
        print(directory_list)

    # command (3): CD 
    elif (getcmd == "CD"):
        s_obj.send(cmd[0].encode())
        s_obj.send(cmd[1].encode())
        print(s_obj.recv(1024).decode())
    
    # comand (4): DWD
    elif (getcmd == "DWD"):
        # current directory is the download directory 
        download_directory = os.getcwd()

        file_name = cmd[1]

        s_obj.send(getcmd.encode())
        s_obj.send(file_name.encode())
        x = s_obj.recv(1024).decode()

        if (x == 'NOK'):
            print('NOK')
            continue
        elif (x == 'OK'):
            with open(os.path.join(download_directory, file_name), 'wb') as file_to_write:
                msg = s_obj.recv(1024)
                if not msg: break
                file_to_write.write(msg)
            
            file_to_write.close()

            # decode 
            crypto1.substitute_decode(file_name)

            print('OK')
    
    # command (5): UPD 
    elif (getcmd == "UPD"):
        file_name = cmd[1]
        does_file_exist = os.path.exists(file_name) # bool 

        if (does_file_exist == False):
            print('NOK')
            continue
        
        # encode 
        crypto1.substitute_encode(file_name)

        s_obj.send(cmd[0].encode())
        s_obj.send(file_name.encode())

        with open(file_name, 'rb') as file_to_send:
            for msg in file_to_send: s_obj.sendall(msg)
        
        # decode 
        crypto1.substitute_decode(file_name)

        print('OK')

    # if invalid command, display error 
    else:
        print("Invalid command\n")
        print('error')
        break

s_obj.close() 
