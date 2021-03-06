import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # We just print a message
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)

        # Print the resource requested (the path)
        print("  Path: " + self.path)


        # Message to send back to the clinet
        if self.path == "/":
            contents = open("info/index.html", "r").read()
        elif self.path == "/info/A.html":
            contents = open("info/A.html", "r").read()
        elif self.path == "/info/C.html":
            contents = open("info/C.html", "r").read()
        elif self.path == "/info/G.html":
            contents = open("info/G.html", "r").read()
        elif self.path == "/info/T.html":
            contents = open("info/T.html", "r").read()
        else:
            try:
                #comprobar con el uracilo: http://127.0.0.1:8080/info/U.html
                contents = open(self.path[1:], "r").read() #cogemos el self.path a partir del index 1 xq el primer "/" no lo queremos, ya que no forma parte del nombre del fichero
            except FileNotFoundError:
                contents = open("info/error.html", "r").read()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()