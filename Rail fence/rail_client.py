import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    client_socket.connect((host, port))

    while True:
        rails = input("Enter number of rails: ")
        mode = input("Enter mode (encrypt/decrypt): ")
        text = input("Enter text: ")

        # Prepare the data with delimiters
        message = f"{rails}|{mode}|{text}"

        # Send the data to the server
        client_socket.send(message.encode('utf-8'))

        # Receive the result from the server
        result = client_socket.recv(4096).decode('utf-8')
        print(f"Result: {result}")

        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != 'yes':
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()

