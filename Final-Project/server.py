#para la medium part se puede usar mucho la description

import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import jinja2 as j
import json

# Define the Server's port
PORT = 8080

def make_request(endpoint, params=""):
    SERVER = "rest.ensembl.org"
    PARAMETERS = "?content-type=application/json"
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", endpoint + PARAMETERS + params) #we don't need to put the server when requesting connection
        # -- Read the response message from the server
        r1 = conn.getresponse()

        # -- Print the status line
        print(f"Response received!: {r1.status} {r1.reason}\n")

        # -- Read the response's body
        data1 = r1.read().decode("utf-8")
        return json.loads(data1)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

#creamos esta función que vamos a usar mucho a lo largo del código
HTML_FOLDER = "./html/"
def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

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
        print("The old path was:", self.path)
        print("The new path is:", url_path.path)
        path = url_path.path

        arguments = parse_qs(url_path.query)
        print("arguments", arguments)

        if path == "/":
            contents = Path('html/form.html').read_text()

        elif path == "/listSpecies":
            list_species = []
            answer_ensemble = make_request("/info/species")
            limit = arguments["limit"][0]
            print("limit:", limit, "Is digit?:", limit.isdigit())
            if limit.isdigit() and 0 < int(limit) < 312:
                limit = int(limit)
                for i in range(limit):
                    list_species.append(answer_ensemble["species"][i]["common_name"])
                contents = read_html_file('listSpecies.html') \
                    .render(context={"list_species": list_species}) #la key de este dict es la que tiene que aparecer en el jinja
            else: #the limit introduced is not an integer number in the interval between 0  and 311 (included)
                message = "The limit introduced is not an integer number in the interval between 0  and 311 (included)"
                contents = Path('html/error.html') \
                    .render(context={"error_message": message})

        elif path == "/karyotype": #creo que me está sacando el mismo kariotipo para todas las especies
            specie = arguments["specie"][0].replace(" ", "_")
            try:
                answer_ensemble = make_request("/info/assembly/" + specie)
                print(answer_ensemble["karyotype"])
                contents = read_html_file('karyotype.html') \
                    .render(context={"list_karyotype": answer_ensemble["karyotype"]})
            except KeyError:
                message = "The specie selected was not found in the data base."
                contents = Path('html/error.html') \
                    .render(context={"error_message": message})


        elif path == "/chromosomeLength":
            specie = arguments["specie"][0].replace(" ", "_")
            try:
                answer_ensemble = make_request("/info/assembly/" + specie)
                chromosome = arguments["chromo"][0]
                if chromosome in answer_ensemble["karyotype"]:
                    #todo  hacerlo un while loop
                    for d in answer_ensemble["top_level_region"]: #esto es una lista de dicccionarios
                        if d["coord_system"] == "chromosome" and d["name"] == chromosome:
                            length = d["length"]
                    contents = read_html_file('lengthChromosome.html') \
                        .render(context={"length": length})
                else:
                    message = "The chromosome selected does not belong to the specie selected."
                    contents = Path('html/error.html') \
                        .render(context={"error_message": message})
            except KeyError:
                message = "The specie selected was not found in the data base."
                contents = Path('html/error.html') \
                    .render(context={"error_message": message})


        #elif path == "/geneSeq":      esto es para el medium
            #    gene = int(arguments["gene"][0])
            #    params = "&species=human"
        #    answer_ensembl = make_request("/sequence/id/" + gene, params)
        else:
            message = "Resource not found."
            contents = Path('html/error.html').read_text() \
                    .render(context={"error_message": message})

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