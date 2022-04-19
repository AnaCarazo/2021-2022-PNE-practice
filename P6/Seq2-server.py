import http.server
import socketserver
import termcolor
from pathlib import Path

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

        list_seq = ["ACTG", "AACCTTGG", "AAACCCTTTGGG", "GTCA", "GGCCTTAA"]

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        if self.path == "/":
            contents = Path('form-1.html').read_text()
        #PING
        elif self.path == "/ping?":
            contents = Path('PING.html').read_text()
        #GET
        elif self.path.startswith("/get?"):
            n = int(self.path.split("?n=")[1])
            sequence = list_seq[n]
            contents = Path('get.html').read_text().format(n=n, sequence=sequence)
        #GENE
        elif self.path.startswith("/gene?"):
            name = self.path.split("?n=")[1]
            gene_seq = Path("seq_dna/" + name + ".txt").read_text()
            contents = Path('gene.html').read_text().format(name=name, gene_seq=gene_seq)
        #OPERATION
        # http://localhost:63342/operation?seq=AACC&operation=Info
        elif self.path.startswith("/operation?"):
            seq = self.path.split("?seq=")[1].split("&")[0]
            #validar la secuencia con una función que compruebe que es correcta--> if seq.valid():
            #                                                                      .....de la línea 52 a la 71....
            #                                                                      else:
            #                                                                         contents = Path('invalid_seq.html').read_text()
            operation = self.path.split("&operation=")[1]
            if operation == "Info":
                pass
                #result = #seq.info() hay que llamar a las correspondientes funciones
                         #pero dnd están estas funciones? Esto ya está dentro de una clase
            elif operation == "Comp":
                #poner en una función
                result = ""
                for b in seq:
                    if b == "A":
                        result = result + "T"
                    elif b == "T":
                        result = result + "A"
                    elif b == "C":
                        result = result + "G"
                    else:
                        if b == "G":
                            result = result + "C"
            elif operation == "Rev":
                result = seq[::-1]
        contents = Path('operation.html').read_text().format(seq=seq, operation=operation, result=result)

        else:
            contents = Path('Error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

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