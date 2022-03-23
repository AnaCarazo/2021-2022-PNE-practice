#For accessing to the functions defined in the Seq0 module, you should write this line in the beginning of your programs:
from Seq0 import *
#puedo poner arriba: import Seq0, como he hecho antes, o poner lo que he puesto ahora
#que con eso no hace falta poner el nombre del módulo + . delante de la función e ese módulo
list_seq = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_seq:
    seq = seq_read_fasta(l)
    dict_seq = seq_count(seq)
    print("\nGene", l + ":", dict_seq)