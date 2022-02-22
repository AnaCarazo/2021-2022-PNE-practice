import Seq0
list_seq = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_seq:
    seq = Seq0.seq_read_fasta(l)
    base = Seq0.most_frecuent_base(seq)
    print("Gene", l + ":", "Most frequent Base:", base)