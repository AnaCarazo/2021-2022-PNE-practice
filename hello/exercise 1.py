#calculate de first 11 elements of the fibonacci's series
N = 11
n1 = 0
n2 = 1
print(n1, end=" ")
print(n2, end=" ")
for i in range(2, N): #aquí sólo necesitamos imprimir 9 números, xq fuera del for loop ya habíamos print dos fuera, por eso empezamos en 2
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num   #ni + n2
#si queremos run el code in the terminal, tenemos que añadir un print vacío al final (que es lo mismo que unend of line character) para que el resultado se imprima todo en una línea sólo)