from Seq1 import Seq
s = Seq("ACCTTTGGGG")
dict_b_p = s.bases_and_percentages()
print("dict: ", dict_b_p)
list_basis = ["A", "C", "T", "G"]
for i, b in enumerate(list_basis):
    print("percentage of", b,  ":", str(list(dict_b_p.values())[i][1]) + "%")