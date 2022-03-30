import socket
import termcolor


# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]
    print(req_line)
    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    route = req_line.split(" ")[1]
    print("The route is:", route)

    if route == "/":
        # This new contents are written in HTML language
        f = open("html/index.html", "r").read()
    elif route == "/goodbye":
        print("Entering into the goodbye file")
        f = open("html/goodbye.html", "r").read()
    elif route == "/question":
        f = open("html/question.html", "r").read()

    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    #Instead of responding with a string, we will send a message in HTML. It is important to change the Content-type header from text/plain to text/html for indicating that we are sending HTML code instead of plain text
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(f)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + f
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()