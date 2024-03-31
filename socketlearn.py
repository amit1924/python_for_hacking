import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port on which the server will listen
host = "127.0.0.1"
port = 12345

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening on port", port)

# Accept incoming connection
client_socket, client_address = server_socket.accept()

print("Connection from:", client_address)

# Send a message to the client
message = "Hello, client!"
client_socket.send(message.encode())

# Close the connection
client_socket.close()
server_socket.close()
