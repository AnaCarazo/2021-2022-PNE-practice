def bases_and_percentages(seq):
    d = {"A" : 0, "C" : 0, "T" : 0, "G" : 0}
    for b in seq:
        d[b] += 1

    total = sum(d.values())
    for k,v in d.items():
        d[k] = [v, round(((v * 100) / total), 1)]
    return d

def convert_menssage(d_bases_and_percentages):
    message = ""
    for k,v in d_bases_and_percentages.items():
        message += k + ": " + str(v[0]) + " (" + str(v[1]) + "%)" + "\n"
    return message


dictionary = bases_and_percentages("ACTGACCTTTGGGG")
print(dictionary)
mess = convert_menssage(dictionary)
print(mess)