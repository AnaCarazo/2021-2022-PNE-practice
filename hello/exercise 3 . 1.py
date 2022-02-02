def count_basis(seq):
    #se puede hacer para devolver los resultados con variables, como siempre, pero ahora no vamos a hacer con dictionaries
    d = {"A" : 0, "C" : 0, "G" : 0, "T" : 0,}
    for b in seq:
        d[b] += 1
    return d

with open("sequences", "r") as f:
    sequences = f.readlines()
    for seq in sequences:
        #necesitamos a new seq with out the end of line characters of seq
        new_seq = seq.replace("\n", "")
        print("Total length:", len(new_seq))
        for k, v in count_basis(new_seq).items():
            print(k + ":", v)