import socket

class Client:
    def __init__(self, IP, PORT):
        self.ip = IP
        self.port = PORT

    def ping(self):
        print("OK")

    def __str__(self): # si no  ponemos esto se imprime cómo está guardado en la memoria, pero no como un string
        return f"Connection to SERVER at {self.ip} PORT: {str(self.port)}"

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port)) #no usamos la bind function
        # Send data.
        s.send(str.encode(msg))
        # Receive data
        response = s.recv(2048).decode("utf-8")
        # Close the socket
        s.close()
        # Return the response
        return response