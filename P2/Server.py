import socket #we want to create a server

# Configure the Server's IP and PORT
PORT = 20000
IP = "127.0.0.1" #IP adress in the computers of the labs, si no pongo el ip adress de mi computer no va a funcionar
#if i have no IP adress, solo esto: IP = "", es que estamos abiertos a todas las conexiones, si el client pone localhost va a funcionar la conexión (creo que en realidad va a funcionar ponga lo que ponga el client)
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #we are creating an object of class socket, with two attributes, que vamos a usar para escuchar
try:
    serversocket.bind((IP, PORT)) #specify the adress of the server (IP: where the server is running, PORT: where it is listening to)
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS) #how many clients at the same time we want to allow to attend, if you don't specify, el operative sistem te determina cuántos puede handle, en linux suelen ser 10, en windows 15...

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept() #el server does not execute anything else

        # y ya cuando consguimos una conexión de un cliente, el cliente es el que ejecuta el resto del programa
        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8") #recv(2048) con esto lo que decimos es q estamos listos para recibir información y la vamos a almacenar en 2048 bites y luego esta informacion la transformamos en un string: .decode("utf-8")
        #this clientsocket is specific to this client, porque yo me puedo cumunicar con más clients
        print("Message from client: {}".format(msg))

        # Send the messag
        message = "Hello from the teacher's server" #this string can be sent back to the client
        send_bytes = str.encode(message) #pero en el socket no podemos escribir directamente strings, hay que hacer una conversion--> encoding the string : .encode(message), y cuando quieras leer la info haces la conversión al revés, de bites a string
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close() #when i close the socket el server deja de procesar la información que le llega del cliente, se cierra la comunicaación
        #if I don not close the socket, puede estar bloqueando un server
except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()