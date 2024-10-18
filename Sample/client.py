import socket

def socket_program():
    host='localhost'
    port=5000

    socket_client=socket.socket()

    socket_client.connect((host,port))

    msg=input("Enter msg:")
    socket_client.send(msg.encode())
    data=socket_client.recv(1024).decode()
    print("received from server:",str(data))

    socket_client.close()

socket_program()