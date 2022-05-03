import http.client
import json
from Seq1 import Seq
import termcolor

specie = "human"
SERVER = "rest.ensembl.org"
ENDPOINT = "/info/" + specie  # este es el que va a ir cambiando
PARAMETERS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMETERS
print()
print(f"\nServer: {SERVER}")
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
    dict_ensemble = json.loads(dict_ensemble)  # si no te va a salir: STRING INDICES MUST BE INTEGERS, no se puede usar la notación para acceder a cosas de un diccionario en un string
    print(dict_ensemble)


except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()