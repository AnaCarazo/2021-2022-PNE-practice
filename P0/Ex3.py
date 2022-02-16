import Seq0
list_seq = ["ADA", "FRAT", "FXN", "RNU6_269P", "U5"]
FOLDER = "./seq_dna/"
for l in list_seq:
    print("Gene", l, "---> Length:", len(seq0.seq_read_fasta(FOLDER + l + ".txt")))