#Adithya Krishna
#20221093
#LZW Server

import socket

def lzw_decompress(compressed):
    compressed = [int(x) for x in compressed.split("#")]

    # Initialize the dictionary with single-character strings
    dictionary = {i: chr(i) for i in range(256)}
    dict_size = 256
    
    w = chr(compressed[0])
    decompressed = [w]
    
    for k in compressed[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: {}'.format(k))
        
        decompressed.append(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    
    return ''.join(decompressed)

        
def server_program():
    host = '127.0.0.1'
    port = 65433

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    try:
        while True:
            data = conn.recv(99).decode()
            if not data:
                break
            print(f"Recieved Compressed Data: {data}")
            answer = lzw_decompress(data)
            print("Decompressed plain text: "+answer)

    finally:
        conn.close()


if __name__ == '__main__':
    server_program()

