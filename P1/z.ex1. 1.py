from Seq2 import Seq
#we check if the seq is valid before iniciating anything, por eso usamos Seq.valid_sequence2(), que se  puede meter cualquier argumento, xq es an static method
#y si te das cuanta en la funcion de iniciación solo tenemos: self.strbases = strbases, no como en Seq1
st1 = "ACCTGC"
st2 = "Hello? Am I a valid sequence?"
seq_list = [st1, st2]
for st in seq_list:
    if Seq.valid_sequence2(st):
    seq_list.append(Seq(st))
    else:
    seq_list.append(Seq("ERROR"))

for i in range(0, len(seq_list)):
    print("Sequence", str(i) + :, sequence_list[i])