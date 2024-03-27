import socket

host, port = "0.0.0.0", 25001

# SOCK_STREAM means TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Bind the socket to the host and port
    server.bind((host, port))
    # Listen for incoming connections
    server.listen(1)
    print("Waiting for data from Unity...")

    # Accept a connection
    connection, address = server.accept()

    with connection:
        print("Connected to Unity:", address)
        # Receive the data from Unity
        data = connection.recv(1024).decode("utf-8")
        print("Received data from Unity:", data)
finally:
    # Close the socket
    server.close()
