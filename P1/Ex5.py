from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

list_basis = ["A", "C", "T", "G"]
list_s = [s1, s2, s3]

for i in range(0, len(list_s)):
    list_count = list_s[i].count_base()
    print("Sequence " + str(i + 1) + ": (Length:", str(list_s[i].len()) + ")", list_s[i], "\n", str(list_basis[0]) + ":", list_count[0], ",", str(list_basis[1]) + ":", list_count[1], ",", str(list_basis[2]) + ":", list_count[2], ",", str(list_basis[3]) + ":", list_count[3])


