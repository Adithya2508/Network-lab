#Adithya Krishna
#20221093
#LZW Client

import socket

def lzw_compress(input_string):
    # Initialize the dictionary with single-character strings
    dictionary = {chr(i): i for i in range(256)}
    dict_size = 256
    
    w = ""
    compressed = ""
    
    for c in input_string:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed += str(dictionary[w]) + "#"
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    
    if w:
        compressed += str(dictionary[w]) + "#"
    
    return compressed[:-1]

def client_program():
    host = '127.0.0.1'
    port = 65433

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
            
        while True:
            data = input("Enter plain text to compress: ")
            encrypted = lzw_compress(data)
            print("Compressed string: "+ encrypted)
            client_socket.sendall(encrypted.encode())

    finally:
        client_socket.close()

if __name__ == '__main__':
    client_program()
    

