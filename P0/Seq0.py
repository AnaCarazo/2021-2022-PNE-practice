#-----Ex1-----
def seq_ping():
    print("OK")

#-----Ex2-----
def valid_filename():
    exit = False
    while not exit:
        filename = input("Enter the name of a file: ")
        try:
            f = open("./seq_dna/" + filename + ".txt", "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("This file does not exist.")

#-----Ex2-----
def seq_read_fasta(filename):
        seq = open("./seq_dna/" + filename + ".txt", "r").read()
        seq = seq[seq.find("\n") + 1:].replace("\n", "")
        return seq

#-----Ex3-----
def seq_len(seq):
    l = len(seq)
    return l

#-----Ex4-----
def seq_count_base(seq, base):
    c = seq.count(base)
    return c

#-----Ex5-----
def seq_count(seq):
    list_count = [seq.count("A"), seq.count("C"), seq.count("T"), seq.count("G")]
    list_basis = ["A", "C", "T", "G"]
    dict_list = dict(zip(list_basis, list_count))
    return dict_list

#-----Ex6-----
def seq_reverse(seq):
    frag = seq
    reverse = frag[::-1]
    return frag, reverse

#-----Ex7-----
def complementary_seq(seq):
    complementary = ""
    for c in seq:
        if c == "A":
            complementary += "T"
        elif c == "T":
            complementary += "A"
        elif c == "C":
            complementary += "G"
        else:
            complementary += "C"
    return complementary

#-----Ex8-----
def most_frecuent_base(seq):
    list_count = [seq.count("A"), seq.count("C"), seq.count("T"), seq.count("G")]
    list_basis = ["A", "C", "T", "G"]
    dict_list = dict(zip(list_basis, list_count))
    import operator
    dict_list_sorted_by_apparences = sorted(dict_list.items(), key=operator.itemgetter(1), reverse=True)
    return dict_list_sorted_by_apparences[0][0]

#----para la práctica 6, meto esta función en este file que voy a importar-----
def bases_and_percentages(seq):
    d = {"A" : 0, "C" : 0, "T" : 0, "G" : 0}
    for b in seq:
        d[b] += 1

    total = sum(d.values())
    for k,v in d.items():
        d[k] = [v, round(((v * 100) / total), 1)]
    return d