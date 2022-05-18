import http.client
import json
from Seq1 import Seq
import termcolor

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
cont_loop = True
while cont_loop:
    gene_name = input("Write the gene name: ")
    if gene_name in genes:
        ID = genes_dict[gene_name]
        cont_loop = False
    else:
        print("The name was not found in the dictionary, try again.")

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/" + ID #añadimos el stable identifier del gene que hemos metido
PARAMETERS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMETERS
print()
print(f"\nConnecting to server: {SERVER}:\n")
print(f"URL: {URL}")
# Connect with the server
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMETERS) #we don't need to put the server when requesting connection
    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    dict_ensemble = r1.read().decode("utf-8")
    dict_ensemble = json.loads(dict_ensemble) #si no te va a salir: STRING INDICES MUST BE INTEGERS, no se puede usar la notación para acceder a cosas de un diccionario en un string
    #print(dict_ensemble)
    termcolor.cprint("Gene: ", 'green', end="")
    print(gene_name)
    s = Seq(dict_ensemble['seq'])
    termcolor.cprint("Description:", 'green', end="")
    print(dict_ensemble['desc'])
    termcolor.cprint("Total length: ", 'green', end="")
    print(len(dict_ensemble['seq']))
    termcolor.cprint("Number of bases and percentage:", 'green')
    list_basis = ["A", "C", "T", "G"]
    list_count = s.count_base()
    dict_bases_perc = s.bases_and_percentages()
    for i, b in enumerate(list_basis):
        print(f"{b}: {list_count[i]} ({list(dict_bases_perc.values())[i][1]}%)")

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()