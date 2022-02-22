def generate_seqs(pattern, number):
    list_seqs = []
    for i in range(0, number):
        seq = pattern
        list_seqs.append(seq)
        pattern = pattern + list_seqs[0]
    return list_seqs

seq_list1 = generate_seqs("A", 4)
list_n = []
for i in range(1, len(seq_list) + 1):
    list_n.append(i)
seqs_num = zip(seq_list1, list_n) # xq no me deja zippear??
for s, n in seqs_num:
    print("Sequence", n, ":", s, ", Lenght:", s.len())