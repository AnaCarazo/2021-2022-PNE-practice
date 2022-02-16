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
        seq = open("./seq_dna/" + filename + ".txt", "r").read()
        seq = seq[seq.find("\n") + 1:].replace("\n", "")
        return seq

def seq_count(seq):
    list_count = [seq.count("A"), seq.count("C"), seq.count("T"), seq.count("G")]
    list_basis = ["A", "C", "T", "G"]
    dict_list = dict(zip(list_basis, list_count))
    return dict_list

def seq_reverse(seq):
    frag = seq[:20]
    reverse = frag[::-1]
    return frag, reverse

def complementary_seq(seq):
    list_seq = []
    for c in seq:
        list_seq.append(c)
    i = 0
    cont_loop = True
    while cont_loop and i < len(list_seq):
        if list_seq[i] == "A":
            list_seq[i] = "T"
            i = i + 1
        elif list_seq[i] == "T":
            list_seq[i] = "A"
            i = i + 1
        elif list_seq[i] == "C":
            list_seq[i] = "G"
            i = i + 1
        else:
            list_seq[i] = "C"
            i = i + 1
    complementary = "".join(list_seq)
    return complementary

def most_frecuent_base(seq):
    list_count = [seq.count("A"), seq.count("C"), seq.count("T"), seq.count("G")]
    list_basis = ["A", "C", "T", "G"]
    dict_list = dict(zip(list_basis, list_count))
    import operator
    dict_list_sorted_by_apparences = sorted(dict_list.items(), key=operator.itemgetter(1), reverse=True)
    return dict_list_sorted_by_apparences[0][1]