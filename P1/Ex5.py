from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

list_s = [s1, s2, s3]
list_basis = ["A", "C", "T", "G"]
list_num = []

for i in range(1, len(list_s) + 1):
    list_num.append(i)
zipped = zip(list_s, list_num)
for s, n in zipped:
    list_count = s.count_base()
    print("Sequence", n, ": (Lenght:", s.len(),")", s, "\n", list_basis[0], ":", list_count[0], ",", list_basis[1], ":", list_count[1], ",", list_basis[2], ":", list_count[2], ",", list_basis[3], ":", list_count[3])


