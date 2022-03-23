import Seq0
list_seq = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_seq:
    print("\nGene", l + ":")
    seq = Seq0.seq_read_fasta(l)
    list_basis = ["A", "C", "T", "G"]
    for b in list_basis:
        b_count = Seq0.seq_count_base(seq, b)
        print(str(b) + ":", b_count)