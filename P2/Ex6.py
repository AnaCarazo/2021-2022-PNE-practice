from Client0 import Client

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080
# -- Create a client object
c = Client(IP, PORT)
# -- Test the ping method
c.ping()
print(c)
# -- Send a message to the server

from Seq1 import Seq

resp = c.talk("Sending the FRAT1 Gene to the server, in fragments of 10 bases...")
s = Seq()
s.seq_read_fasta("FRAT1")
print("Gene FRAT1:", s)
n1 = 0
n2 = 1
for i in range(0, 5):
    frag = s.frag_10bases(n1, n2)
    print("Fragment", str(n2) + ":", frag)
    resp = c.talk(f"Fragment {n2}: {frag}")
    n1 = n1 + 1
    n2 = n2 + 1
