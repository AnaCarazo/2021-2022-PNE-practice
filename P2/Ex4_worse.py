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
print("\nSending the U5 Gene to the server...")
resp1 = c.talk("Sending the U5 Gene to the server...")
print(f"Response: {resp1}")

# -- Create a Null sequence
s1 = Seq()
# -- Initialize the null seq with the given file in fasta format
s1.seq_read_fasta("U5")
print(s1)
response1 = c.talk(str(s1))
print(f"Response: {response1}")

print("\nSending the FRAT1 Gene to the server...")
resp2 = c.talk("Sending the FRAT1 Gene to the server...")
print(f"Response: {resp2}")
s2 = Seq()
s2.seq_read_fasta("FRAT1")
print(s2)
response2 = c.talk(str(s2))
print(f"Response: {response2}")

print("\nSending the ADA Gene to the server...")
resp3 = c.talk("Sending the ADA Gene to the server...")
print(f"Response: {resp3}")
s3 = Seq()
s3.seq_read_fasta("ADA")
print(s3)
response3 = c.talk(str(s3))
print(f"Response: {response3}")