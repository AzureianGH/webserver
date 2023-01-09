import socket

# Create a socket to connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect(("23.28.183.74", 9000))

while True:
    # Get the command from the user
    command = input("Enter a command: ")
    # Send the command to the server
    client_socket.sendall(command.encode())
    # Receive the response from the server
    response = client_socket.recv(1024).decode()
    print(response)

# Close the socket
client_socket.close()
