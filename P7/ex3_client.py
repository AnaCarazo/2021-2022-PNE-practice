import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000207552" #este es el que va a ir cambiando
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
    print(f"Gene: MIR633 \nDescription: {dict_ensemble['desc']} \nBases: {dict_ensemble['seq']}")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

