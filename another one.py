import socket

host, port = "", 25001

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
sock.bind((host, port))

# Listen for incoming connections
sock.listen(1)

print("Waiting for Unity to connect...")

# Accept a connection from Unity
connection, client_address = sock.accept()

try:
    print("Unity connected.")
    while True:
        # Receive data from Unity
        data = connection.recv(1024).decode("utf-8")
        if data:
            # Process the received data (e.g., print it)
            print("Received data:", data)
        else:
            print("No more data from Unity. Exiting...")
            break
finally:
    # Close the connection
    connection.close()