#tcp server
#Adithya krishna

import socket
def server_program():
   
    host = 'localhost'
    port = 5000  

    server_socket = socket.socket()  
   
    server_socket.bind((host, port)) 

    
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:            
            break
        print("from client user: " + str(data))
        data = input('Enter message: ')
        conn.send(data.encode())  

    conn.close()  


if __name__ == '__main__':
    server_program()
    
    
'''OUTPUT
  ========
Connection from: ('192.168.10.108', 35654)
from client user: hello
Enter message: hai
'''
