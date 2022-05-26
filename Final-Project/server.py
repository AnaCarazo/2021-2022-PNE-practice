#para la medium part se puede usar mucho la description

import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import jinja2 as j
import json
from Seq0 import Seq

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

#cuando pongamos la dirección de los html no hace falta poner esto delante para indicar a qué directory pertenece, xq ya lo estamos incluyendo con esta variable
HTML_FOLDER = "./html/"

#creamos esta función que vamos a usar mucho a lo largo del código
def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

#para el medium level:
genes_dict = {"SRCAP": "ENSG00000080603",
              "FRAT1": "ENSG00000165879",
              "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060",
              "RNU6_269P": "ENSG00000212379",
              "MIR633": "ENSG00000207552",
              "TTTY4C": "ENSG00000228296",
              "RBMY2YP": "ENSG00000227633",
              "FGFR3": "ENSG00000068078",
              "KDR": "ENSG00000128052",
              "ANK2": "ENSG00000145362"}

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
        print("arguments:", arguments)

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
            else:
                #contents = Path('html/try.html').read_text()
                message = "The limit introduced is not an integer number in the interval between 0  and 311 (included)"
                contents = read_html_file('error.html') \
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
                contents = read_html_file('error.html') \
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
                    contents = read_html_file('error.html') \
                        .render(context={"error_message": message})
            except KeyError:
                message = "The specie selected was not found in the data base."
                contents = read_html_file('error.html') \
                    .render(context={"error_message": message})
        #esto es para el medium

        elif path == "/geneSeq":
            gene = arguments["gene1"][0]
            params = "&species=human"
            genes = genes_dict.keys()
            print(genes)
            if gene in genes:
                ID = genes_dict[gene]
                #print("ID:", ID)
                answer_ensembl = make_request("/sequence/id/" + ID, params)
                #print(answer_ensembl)
                sequence = answer_ensembl['seq']
                #print("Sequence:", sequence)
                contents = read_html_file('geneSeq.html') \
                    .render(context={"sequence": sequence})
            else:
                message = "The name was not found in the dictionary, try again."
                contents = read_html_file('error.html') \
                    .render(context={"error_message": message})

        elif path == "/geneInfo":
            gene = arguments["gene2"][0]
            params = "&species=human"
            genes = genes_dict.keys()
            print(genes)
            if gene in genes:
                ID = genes_dict[gene]
                print("ID:", ID)
                answer_ensembl = make_request("/sequence/id/" + ID, params)
                print(answer_ensembl)
                print(answer_ensembl.keys())
                start = answer_ensembl['desc'].split(":")[3]
                end = answer_ensembl['desc'].split(":")[4]
                chromosome = answer_ensembl['desc'].split(":")[1]
                length = int(end)-int(start)
                print("start:", start, "end:", end, "Length:", int(end)-int(start), "id:", ID, "Chromosome name:")
                contents = read_html_file('geneInfo.html') \
                    .render(context={"start": start, "end": end, "ID": ID, "length": length, "chromosome_name": chromosome})
            else:
                message = "The name was not found in the dictionary, try again."
                contents = read_html_file('error.html') \
                    .render(context={"error_message": message})

        elif path == "/geneCalc":
            gene = arguments["gene3"][0]
            params = "&species=human"
            genes = genes_dict.keys()
            print(genes)
            if gene in genes:
                ID = genes_dict[gene]
                print("ID:", ID)
                answer_ensembl = make_request("/sequence/id/" + ID, params)
                print(answer_ensembl)
                print(answer_ensembl.keys())
                sequence = answer_ensembl['seq']
                s = Seq(sequence)
                length = s.len()
                dict_bases_perc = s.bases_and_percentages()
                bases = dict_bases_perc.keys()
                list_info = []
                for i, b in enumerate(bases):
                    list_info.append(f"{b}: {list(dict_bases_perc.values())[i][0]} ({list(dict_bases_perc.values())[i][1]}%)")
                contents = read_html_file('geneCalc.html') \
                    .render(context={"length": length, "list_info": list_info})
            #/phenotype/region/homo_sapiens/9:22125500-22136000?feature_type=Variation;content-type=application/json
        elif path == "/geneList":
            print("geneList")
            chromo = arguments["chromosome"][0]
            start = arguments["start"][0]
            end = arguments["end"][0]
            answer_ensemble = make_request(f"/phenotype/region/homo_sapiens/{chromo}:{start}-{end}")
            #print("ensemble request:")
            #termcolor.cprint(answer_ensemble, "yellow")
            list_gene = []
            #comprobar que en la location que el chromosome y el start y end son los que pide el user
            #si coinciden entonces hacemos un append a list_gene, que es lo que vamos a pasar al html
            for e in answer_ensemble:
                list_dicts = e['phenotype_associations']
                print(list_dicts) #esto es una lista de diccionarios
                for d in list_dicts:
                    print(d["attributes"])

            contents = read_html_file('geneList.html')

        else:
            message = "Resource not found."
            contents = read_html_file('error.html') \
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