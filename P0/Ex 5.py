import Seq0
list_seq = ["U5", "ADA", "FRAT1", "FXN"]
FOLDER = "./seq_dna/"
for l in list_seq:
    seq = (Seq0.seq_read_fasta(FOLDER + l + ".txt")
    dict_seq = seq_count(seq)
    print("\nGene", l + ":", dict_seq)