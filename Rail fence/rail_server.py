import socket

def rail_fence_encrypt(text, rails):
    rail = [['' for _ in range(len(text))]
            for _ in range(rails)]
    direction = None
    row, col = 0, 0

    for char in text:
        if row == 0 or row == rails - 1:
            direction = not direction
        rail[row][col] = char
        col += 1
        row += 1 if direction else -1

    cipher_text = ''.join([''.join(row) for row in rail])
    return cipher_text

def rail_fence_decrypt(cipher_text, rails):
    rail = [['\n' for _ in range(len(cipher_text))]
            for _ in range(rails)]
    direction = None
    row, col = 0, 0

    # Mark the positions of characters in the rail
    for char in cipher_text:
        if row == 0:
            direction = True  # Move down
        elif row == rails - 1:
            direction = False  # Move up

        rail[row][col] = '*'
        col += 1
        row += 1 if direction else -1

    index = 0
    # Fill the marked positions with characters from cipher_text
    for i in range(rails):
        for j in range(len(cipher_text)):
            if rail[i][j] == '*' and index < len(cipher_text):
                rail[i][j] = cipher_text[index]
                index += 1

    result = []
    row, col = 0, 0
    # Read the characters in the zigzag pattern to decrypt
    for i in range(len(cipher_text)):
        if row == 0:
            direction = True  # Move down
        elif row == rails - 1:
            direction = False  # Move up

        result.append(rail[row][col])
        col += 1
        row += 1 if direction else -1

    return ''.join(result).replace('\n', '')  # Remove any newline characters




def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        try:
            # Receive the data
            data = client_socket.recv(4096).decode('utf-8')
            if not data:
                break

            # Split the data based on delimiters
            parts = data.split('|')
            if len(parts) < 3:
                response = "Invalid input format."
            else:
                rails = int(parts[0])
                mode = parts[1]
                text = parts[2]

                if mode not in ['encrypt', 'decrypt']:
                    response = "Invalid mode. Use 'encrypt' or 'decrypt'."
                else:
                    if mode == 'encrypt':
                        result = rail_fence_encrypt(text, rails)
                    elif mode == 'decrypt':
                        result = rail_fence_decrypt(text, rails)
                    response = result
                    print(f"Result: {result}")

            # Send response to the client
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

