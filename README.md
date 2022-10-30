# RFS-Service-using-Socket-Programming
Network Application using Socket Programming 

## Goal: 
Develop a simple remote file system service (RFS) and understand the principles of layered network architecture. The application supports the following 5 commands that the client can perform: 
1. CWD : Retrieve the path of the current working directory for the user 
2. LS : List the files/folders present in the current working directory 
3. CD <dir> : Change the directory to <dir> as specified by the client 
4. DWD <file> : Download the <file> specified by the user on server to client 
5. UPD <file> : Upload the <file> on client to the remote server in CWD 

## A Template Layer N model of the RFS client and server;
### Top most layer: File Service will ensure to exercise the requested RFS command and take use of the associated OS API’s on the client/server for file operations and rely on the underlying Crypto service to encode/encrypt and decode/decrypt the contents at either ends of the client.

### Crypto Layer: This will facilitate 3 options (Plain Text, Substitute, Transpose modes) to mangle the data before transmitting to the networking layer.
1. Plain text → No change to the input; (No encryption or decryption)
2. Substitute → Only alphanumeric characters will be substituted with fixed offset,
say Caesar cipher with offset 2. Example ARTZ will be substituted with CTVB
3. Transpose → Revere the contents in a word by word manner. Example ARTZ will
be substituted with ZTRA.
