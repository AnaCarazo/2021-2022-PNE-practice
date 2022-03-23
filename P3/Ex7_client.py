from Client0 import Client

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8000
# -- Create a client object
c = Client(IP, PORT)
print(c)
# -- Test the ping method
print("* Testing PING...")
c.ping()

list_seqs = []
print("\n* Testing GET...")
for i in range(0, 4):
    response = c.talk(f"GET {i}")
    print(f"GET {i}: {response}")
    list_seqs.append(response)

print("\n* Testing INFO...")
response4 = c.talk(f"INFO {list_seqs[0]}")
print(f"Sequence: {list_seqs[0]} \nTotal lenght: {len(list_seqs[0])} \n{response4}")

print("Testing COMP...")
response1 = c.talk(f"COMP {list_seqs[0]}")
print("Sequence:", list_seqs[0])
print(f"COMP: {response1}")

print("\n* Testing REV...")
response2 = c.talk(f"REV {list_seqs[0]}")
print("Sequence:", list_seqs[0])
print(f"REV: {response2}")

print("\n* Testing GENE...")
list_names = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for i in range(0, len(list_names)):
    response3 = c.talk(f"GENE {list_names[i]}")
    print(f"GENE {list_names[i]}:\n {response3}")