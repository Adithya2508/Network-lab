import socket

def server_program():

    host='localhost'
    port=5000

    server_socket=socket.socket()
    server_socket.bind((host,port))

    server_socket.listen(2)

    conn,address=server_socket.accept()
    print("incoming connection from:",str(address))
    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
    
        print("msg from client:",str(data))
        msg=input("enter data")
        conn.send(data.encode())

    conn.close()

if __name__=='__main__':
    server_program()