import Seq0
list_seq = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_seq:
    print("\nGene", l + ":")
    seq = Seq0.seq_read_fasta(l)
    dict_bases = Seq0.seq_count(seq)
    for key, value in dict_bases.items():
        print(key + ":", value)