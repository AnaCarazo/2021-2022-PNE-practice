import http.client
import json
from Seq1 import Seq
import termcolor

specie = "human"
SERVER = "rest.ensembl.org"
ENDPOINT = "/info/species"  # este es el que va a ir cambiando
PARAMETERS = "?content-type=application/json&parameter1=a"
URL = SERVER + ENDPOINT + PARAMETERS
print()
print(f"\nServer: {SERVER}")
print(f"URL: {URL}")

def make_request(URL, PARAMETERS=""):
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", ENDPOINT + PARAMETERS) #we don't need to put the server when requesting connection
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


#ensemble_answer = make_call(EMDPOINT, PARAMETERS)

