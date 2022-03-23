#usando el Teacher's server puedes tener una conversación bidireccional
import socket

PORT = 8080
IP = "localhost"

while True:
  # -- Ask the user for the message
    message = input("Please enter a message: ")
  # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # -- Establish the connection to the Server
    s.connect((IP, PORT))
  # -- Send the user message
    s.send(str.encode(message))
# Receive data from the server
    msg = s.recv(2048)
    print("MESSAGE FROM THE SERVER:")
    print(msg.decode("utf-8"))
  # -- Close the socket
    s.close()


