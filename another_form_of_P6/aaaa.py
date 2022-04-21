import Seq0
seq = "ACCTTTGGGG"
list_basis = ["A", "C", "T", "G"]
length = f"Total length: {len(seq)}"
d = Seq0.bases_and_percentages(seq)
#first_value = list(word_freq.values())[0]
list_values = list(d.values())
info_A = f"\n{list_basis[0]}: {list_values[0][0]} ({list_values[0][1]}%)"
info_C = f"\n{list_basis[1]}: {list_values[1][0]} ({list_values[1][1]}%)"
info_T = f"\n{list_basis[2]}: {list_values[2][0]} ({list_values[2][1]}%)"
info_G = f"\n{list_basis[3]}: {list_values[3][0]} ({list_values[3][1]}%)"
result = length + info_A + info_C + info_T + info_G
#print(result)

result_1 = ""
for i in range(0, 4):
    result_1 = result_1 + f"\n{list_basis[i]}: {list_values[i][0]} ({list_values[i][1]}%)"
print(result_1)