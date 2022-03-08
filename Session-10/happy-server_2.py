import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#by adding this method: .setsockopt() ---> I can run two servers in the same port

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# -- Waits for a client to connect
print("Waiting for Clients to connect")
ls.accept()

#pero para poder recivir información del client y mandar tenemos que añadir:

# -- Waits for a client to connect
print("Waiting for Clients to connect")
(cs, client_ip_port) = ls.accept()

print("A client has connected to the server!")

# -- Read the message from the client
# -- The received message is in raw bytes
msg_raw = cs.recv(2048)

# -- We decode it for converting it
# -- into a human-redeable string
msg = msg_raw.decode() #to print the information in the console

# -- Print the received message
print(f"Received Message: {msg}")

# -- Close the socket
ls.close()
#The program no longer finish (like before). Now it waits for the clients to connect.
#es importante cerrar los ports de los servers, xq si no otro por no puede run in that port
#when listeninf, the server can contact with many clients, as many as we defined, but when traing to communicate, si no hacemos el loop, solo con 1 client