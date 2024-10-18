

import socket

def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j

def encrypt(key,message):
 
 plain_text = message.replace(" ","x")
 new_text = ""

 for i in range(len(plain_text)):
        if i<len(plain_text)-1 and plain_text[i]==plain_text[i+1]:
            new_text += plain_text[i]
            new_text += 'x'
            new_text += plain_text[i+1]
            new_text += 'x'
            i+=1
        else:
            new_text += plain_text[i]
 
 print(len(new_text)%2)
 if (len(new_text)%2) > 0:
 	new_text += 'x'
 	
 plain_text = new_text


 list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
 digraph = []
 group = 0
 matrix = []

 for i in range (2,len(plain_text),2):
        digraph.append(plain_text[group:i])
        group = i
        
 digraph.append(plain_text[group:])

 key_letters = []

 for i in range (0,len(key)):
        if key[i] not in key_letters:
             key_letters.append(key[i])
        
 print (f"plain text = {plain_text} and key letters = {key_letters}")
 print (f"digraph is {digraph}")

 count = 0
 row_list = []

 for letter in key_letters:
        if count<5:
           row_list.append(letter)
           count+=1
        if count == 5:
           matrix.append(row_list)
           row_list = []
           count = 0
 for letter in list1:
         if letter not in key_letters:
           if count<5:
               row_list.append(letter)
               count+=1
           if count==5:
               matrix.append(row_list)
               row_list = []
               count = 0

 print(f"matrix is {matrix}")

 row_count = 0
 col_count = 0
 i = 0
 ciphertext = ""
 
 #print (f"digraph elements are {digraph[0][0]} {digraph[0][1]}")
 for i in range (len(digraph)):
       if len(digraph[i])==0:
             break
       if len(digraph[i])!=0:
             row1,col1 = search(matrix,digraph[i][0])
       if len(digraph[i])==2:
             row2,col2 = search(matrix,digraph[i][1])
       
       
       if row1==row2 :
            #print(f"{digraph[i][0]} and {digraph[i][1]} are in same row")
            if col1!=4  and col2 != 4:
                ciphertext += matrix[row1][col1+1]
                ciphertext += matrix[row2][col2+1]
            else :
                if col1==4:
                     ciphertext += matrix[row1][0]
                     ciphertext += matrix[row2][col2+1]
                else:
                     ciphertext += matrix[row1][col1+1]
                     ciphertext += matrix[row2][0]                   
       elif col1==col2 :
            #print(f"{digraph[i][0]} and {digraph[i][1]} are in same col")
            if row1!=4  and row2 != 4:
                ciphertext += matrix[row1+1][col1]
                ciphertext += matrix[row2+1][col2]
            else :
                if row1==4:
                     ciphertext += matrix[0][col1]
                     ciphertext += matrix[row2+1][col2]
                else:
                     ciphertext += matrix[row1+1][col1]
                     ciphertext += matrix[0][col2]
       else:
               #print(f"{digraph[i][0]} and {digraph[i][1]} are diagonals")
               ciphertext += matrix[row1][col2]
               ciphertext += matrix[row2][col1]
               
 print(f"Cipher text = {ciphertext}")
 return(ciphertext)



def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

    host = 'localhost'
    port = 60014
    

    server_socket.bind((host, port))
    

    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    while True:
 
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        

        key = client_socket.recv(1024).decode('utf-8')
        print(f"Received key: {key}")
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received message: {message}")
        ciphertext = encrypt(key,message)
        

        response = ciphertext.encode('utf-8')
        client_socket.send(response)
        

        client_socket.close()
                     
                
if __name__ == "__main__":
  start_server()
  
#o/p:
#Received key: monarchy
#Received message: instruments
#plain text = instrumentsx and key letters = ['m', 'o', 'n', 'a', 'r', 'c', 'h', 'y']
#digraph is ['in', 'st', 'ru', 'me', 'nt', 'sx']
#matrix is [['m', 'o', 'n', 'a', 'r'], ['c', 'h', 'y', 'b', 'd'], ['e', 'f', 'g', 'i', 'k'], ['l', 'p', 'q', 's', 't'], ['u', 'v', 'w', 'x', 'z']]
#Cipher text = gatlmzclrqxa

  
