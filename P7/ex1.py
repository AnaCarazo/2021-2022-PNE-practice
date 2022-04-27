import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping" #este es el que va a ir cambiando
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
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1) #si no te va a salir: STRING INDICES MUST BE INTEGERS, no se puede usar la notación para acceder a cosas de un diccionario en un string
    # -- Print the received data
    if data1['ping'] == 1: #no puedes poner esto como string, xq al usar json.loads() esto es un integer, no se transforma a string
        # json.loads() intenta transformar everything a su type correspondiente
        print(f"PING OK!!! The data base is running.")
    else:
        print(f"ERROR!!! The data base is not running.")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

