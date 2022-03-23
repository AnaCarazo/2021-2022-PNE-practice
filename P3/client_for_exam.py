from Client0 import Client
IP = "127.0.0.1"
PORT = 8000
# -- Create a client object
c = Client(IP, PORT)
print(c)
print("\n* Testing ADD command...")
response = c.talk(f"ADD HHH")
print(response)



