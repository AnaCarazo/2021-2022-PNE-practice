import http.client
import json
from Seq1 import Seq

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
genes = genes_dict.keys()
print(genes)
for g in genes:
    ID = genes_dict[g]
    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/" + ID  # este es el que va a ir cambiando
    PARAMETERS = "?content-type=application/json"
    URL = SERVER + ENDPOINT + PARAMETERS
    print()
    print(f"\nConnecting to server: {SERVER}:\n")
    print(f"URL: {URL}")
    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMETERS)  # we don't need to put the server when requesting connection
        # -- Read the response message from the server
        r1 = conn.getresponse()

        # -- Print the status line
        print(f"Response received!: {r1.status} {r1.reason}\n")

        # -- Read the response's body
        dict_ensemble = r1.read().decode("utf-8")
        dict_ensemble = json.loads(
            dict_ensemble)  # si no te va a salir: STRING INDICES MUST BE INTEGERS, no se puede usar la notación para acceder a cosas de un diccionario en un string
        # print(dict_ensemble)

        print(f"{g} ")

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

