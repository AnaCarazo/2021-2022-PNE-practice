def seq_ping():
    print("OK")

def valid_filename():
    exit = False
    while not exit:
        filename = input("Enter the name of a file: ")
        try:
            f = open("./seq_dna/" + filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("This file does not exist.")
def seq_read_fasta(filename):
        seq = open("./seq_dna/" + filename, "r").read()
        seq = seq[seq.find("\n") + 1:].replace("\n")
        return seq
