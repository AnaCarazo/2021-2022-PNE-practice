import socket

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    # -- Execute this part if there are no errors
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode() #msg = msg_raw.decode().replace("\n", "").strip() : en windows, a veces nos llega el mensaje con un end of line character y con espacios, lo quitamos.
        #del mensaje que nos llega necesritamos separarlo en dos partes, el command y el argumento
        splitted_command = msg.split(" ") #para el PING command, que solo tiene un elemento, necesitamos calcular el argumento solo en el caso de que el command no sea ping
        command = splitted_command[0]
        #argument = splitted_command[1]
        print(command)
        if command != "PING":
            argument = splitted_command[1]
        print(command)
        print(f"Message received: {msg}")

#poner lo del mensaje en color verde, con lo de colorama
        if command == "PING":
            response = "OK!\n"
            print("PING COMMAND")

        elif command == "GET":
            list_seqs = ["ACTGACTG, CCAACCTTGG, GGAACCTTGGCCAATT, TGCATGCA, AACCTTGG"]
            print(list_seqs[int(argument)])

        elif command == "INFO":
            from Seq1 import Seq
            sequence = Seq(argument)
            list_basis = ["A", "C", "T", "G"]
            print("Sequence:", sequence.__str__(), "\nTotal length:", sequence.len(), "\n", str(list_basis[0]) + ":", sequence.count_base()[0], "(" + (sequence.count_base()[0]) * 100 / sequence.len(), ")", "\n", str(list_basis[1]) + ":", sequence.count_base()[1], "(" + (sequence.count_base()[1]) * 100 / sequence.len(), ")", "\n", str(list_basis[2]) + ":", sequence.count_base()[2], "(" + (sequence.count_base()[2]) * 100 / sequence.len(), ")", "\n", str(list_basis[3]) + ":", sequence.count_base()[3], "(" + (sequence.count_base()[3]) * 100 / sequence.len(), ")"

        elif command == "COMP":
            from Seq1 import Seq
            sequence = Seq(argument)
            print(sequence.complementary_seq())

        elif command == "REV":
            from Seq1 import Seq
            sequence = Seq(argument)
            print(sequence.seq_reverse())
        elif command == "GENE":
            from Seq1 import Seq
            # -- Create a Null sequence
            s = Seq()
            # -- Initialize the null seq with the given file in fasta format
            print(s.seq_read_fasta(argument))

        else:
            response = "This command is not available in the server\n"

        cs.send(response.encode())
        cs.close()