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

def seq_count(seq):
    list_count = [seq.count("A"), seq.count("C"), seq.count("T"), seq.count("G")]
    list_basis = ["A", "C", "T", "G"]
    dict_list = dict(zip(list_basis, list_count))
    return dict_list