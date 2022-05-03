import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import jinja2 as j

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

#creamos esta función que vamos a usar mucho a lo largo del código
HTML_FOLDER = "./html/"
def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

LIST_SEQUENCES = ["ACTG", "AACCTTGG", "AAACCCTTTGGG", "GTCA", "GGCCTTAA"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU5A", "U5"]

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file

        url_path = urlparse(self.path)
        print("The old path2 was:", self.path)
        print("The new path is:", url_path.path)
        path = url_path.path

        arguments = parse_qs(url_path.query)
        print("arguments", arguments)

        if self.path == "/":
            #con este método podríamos añadir otra sequence a LIST_SEQUENCES y seguiría funcionando igual
            contents = read_html_file('html/index.html')\
                .render(context={"n_sequence": len(LIST_SEQUENCES),
                                 "genes": LIST_GENES})
        #PING
        elif path == "/ping":
            contents = read_html_file(path[1:]).render()

        #GET
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0]) #hay que poner [0]
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(path[1:] + ".html").render(context={
                "n_sequence": n_sequence,
                "sequence": sequence})
        #GENE
        elif path == "/gene":
            gene_name = arguments["gene_name"][0]
            sequences = Path("./sequences" + gene_name + ".txt").read_text()
            contents = read_html_file(path[1:] + ".html").render(context={
                "gene_name": gene_name,
                "sequence": sequences})

        #OPERATION
        # http://localhost:63342/operation?seq=AACC&operation=Info
        elif path == "/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["operation"][0]
            if operation == "Info":
                pass
                #result = #seq.info() hay que llamar a las correspondientes funciones
                         #pero dnd están estas funciones? Esto ya está dentro de una clase
            elif operation == "Comp":
                pass
            elif operation == "Rev":
                contents = read_html_file(path[1:] + ".html").render(context={
                    #cambiar estos
                    "n_sequence": n_sequence,
                    "sequence": sequence})

            contents = Path('html/operation.html').read_text().format(seq=seq, operation=operation, result=result)
        else:
            contents = Path('html/Error.html').read_text()
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