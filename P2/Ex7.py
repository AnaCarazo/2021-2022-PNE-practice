from Client0 import Client

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
#conection to the first server
IP = "127.0.0.1"
PORT = 8080
c1 = Client(IP, PORT)
c1.ping()
print(c1)
#conection to the second server
IP = "127.0.0.1"
PORT = 8081
c2 = Client(IP, PORT)
c2.ping()
print(c2)

from Seq1 import Seq

resp1 = c1.talk("Sending the FRAT1 Gene to the server, in fragments of 10 bases...(odds)")
resp2 = c2.talk("Sending the FRAT1 Gene to the server, in fragments of 10 bases...(evens)")

s = Seq()
s.seq_read_fasta("FRAT1")
print("Gene FRAT1:", s)
n1 = 0
n2 = 1
list_frags = []
for i in range(0, 10):
    frag = s.frag_10bases(n1, n2)
    print("Fragment", str(n2) + ":", frag)
    #resp = c.talk(f"Fragment {n2}: {frag}")
    list_frags.append(frag)
    n1 = n1 + 1
    n2 = n2 + 1

for i in range(0, 10, 2):
    resp = c1.talk(f"Fragment {i + 1}: {list_frags[i]}")
for i in range(1, 10, 2):
    resp = c2.talk(f"Fragment {i + 1}: {list_frags[i]}")