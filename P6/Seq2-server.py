import http.server
import socketserver
import termcolor
from pathlib import Path
import Seq0
#estos dos módulos son mejores opciones para desarollar la práctica
#from urllib.parse import urlparse, parse_qs
#from jinja2 import Template

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
            contents = Path('index.html').read_text()
        #PING
        elif self.path == "/ping?":
            contents = Path('PING.html').read_text()
        #GET
        elif self.path.startswith("/get?"):
            n = int(self.path.split("?n=")[1])
            sequence = list_seq[n]
            print(n, sequence)
            contents = Path('get.html').read_text().format(n, sequence)
        #GENE
        elif self.path.startswith("/gene?"):
            name = self.path.split("?name=")[1]
            gene_seq = Seq0.seq_read_fasta(name)
            contents = Path('gene.html').read_text().format(name, gene_seq)
        #OPERATION
        # http://localhost:63342/operation?seq=AACC&operation=Info
        elif self.path.startswith("/operation?"):
            seq = self.path.split("?seq=")[1].split("&")[0]
            s = Seq0.Seq(seq)
            if s.valid_sequence():
                operation = self.path.split("&operation=")[1]
                if operation == "Info":
                    list_basis = ["A", "C", "T", "G"]
                    length = f"Total length: {len(seq)}"
                    d = s.bases_and_percentages()
                    list_values = list(d.values())
                    result = length
                    for i in range(0, 4):
                        result = result + f"<br>{list_basis[i]}: {list_values[i][0]} ({list_values[i][1]}%)"
                elif operation == "Comp":
                    #poner en una función
                    result = s.complementary_seq()
                elif operation == "Rev":
                    result = seq[::-1]
                contents = Path('operation.html').read_text().format(seq=seq, operation=operation, result=result)
            else:
                contents = Path('invalid_seq.html').read_text()
        else:
            contents = Path('Error.html').read_text()
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(str.encode(contents))))

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