

import socket

def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

    host = 'localhost'
    port = 60014
    
 
    client_socket.connect((host, port))
    print("Connected to the server")
    
  
    key = input("Enter a key : ")
    key = key.encode('utf-8')
    client_socket.send(key)
    
    
    message = input("Enter a message : ")
    message = message.encode('utf-8')
    client_socket.send(message)
    

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Response from server: {response}")
    

    client_socket.close()



start_client()

#Connected to the server
#Enter a key : monarchy
#Enter a message : instruments
#Response from server: gatlmzclrqxa

                     
           
            
           
        
        
        


