from Client0 import Client

PRACTICE = 2
EXERCISE = 4

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
seq_list = ["U5", "FRAT1", "ADA"]
for i in range(0, len(seq_list)):
    print(f"\nSending the {seq_list[i]} Gene to the server...")
    resp = c.talk("Sending the U5 Gene to the server...")
    print(f"Response: {resp}")
    s = Seq()
    s.seq_read_fasta(seq_list[i])
    print(s)
    response = c.talk(str(s))
    print(f"Response: {response}")
