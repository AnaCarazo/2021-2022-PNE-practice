import Seq0
list_seq = ["U5", "ADA", "FRAT1", "FXN"]
FOLDER = "./seq_dna/"
for l in list_seq:
    print("\nGene", l + ":")
    seq = (seq0.seq_read_fasta(FOLDER + l + ".txt")
    list_count = [seq.count("A"), seq.count("C"), seq.count("T"), seq.count("G")]
    list_basis = ["A", "C", "T", "G"]
    dict_list = dict(zip(list_basis, list_count))
    for key, value in dict_list.items():
        print(key + ":", value)