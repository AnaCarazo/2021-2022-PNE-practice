def fibosum(n): #function fibonacci series
    n1 = 0
    n2 = 1
    fibterms = []
    if n == 1:
        fibterms.append(n1)
        return sum(fibterms)
    elif n == 2:
        fibterms.append(n1)
        fibterms.append(n2)
        return sum(fibterms)
    else:
        for i in range(2, n):
            num = n1 + n2
            n1 = n2
            n2 = num
            fibterms.append(num)
        return (sum(fibterms) + 1) #sumamos 1 xq en este for loop no estamos incluyendo los dos primeros términos (xq mpezamos en 2 en la range function, osea el término 0 y el término 1 no lo incluímos), q son 0 y 1, su suma es 1 y hay que tenerla en cuenta en el resultado final

print("Sum of the first 5 components of the Fibonacci series:", fibosum(5))
print("Sum of the first 10 components of the Fibonacci series:", fibosum(10))