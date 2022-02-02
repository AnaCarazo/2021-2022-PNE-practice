def count_basis(seq):
    #se puede hacer para devolver los resultados con variables, como siempre, pero ahora no vamos a hacer con dictionaries
    d = {"A" : 0, "C" : 0, "G" : 0, "T" : 0,}
    for b in seq:
        #if b == "A":
            #d[b] += 1
        #elif b == "C":
            #d[b] += 1
        #elif b == "G":
            #d[b] += 1
        #elif b == "T":
            #d[b] += 1
        #en vez de hacer esto, como lo que vamos a hacer es lo mismo en todos los casos, podemos poner solo: d[b] += 1, xq en todos los casos va a hacer eso
        d[b] += 1 #esto es siempre suponindo que la sequencia de adn es correcta y todas las bases existen y forman parte de las keys de nuestro dict
    return d

dna_seq = input("Introduce the sequence: ")
print("Total length:", len(dna_seq))
for k, v in count_basis(dna_seq).items():
    print(k + ":", v)