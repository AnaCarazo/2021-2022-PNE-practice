import Seq0
list_seq = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_seq:
    seq = Seq0.seq_read_fasta(l)
    dict_seq = Seq0.seq_count(seq)
    print("\nGene", l + ":", dict_seq)