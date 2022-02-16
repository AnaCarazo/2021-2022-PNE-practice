import Seq0
list_seq = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
#FOLDER = "./seq_dna/"
for l in list_seq:
    print("Gene", l, "---> Length:", len(Seq0.seq_read_fasta(l)))