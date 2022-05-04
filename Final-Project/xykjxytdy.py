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

#ensemble_answer = make_call(EMDPOINT, PARAMETERS)

