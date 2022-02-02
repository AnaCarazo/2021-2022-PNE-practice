#
def fib(n): #function fibonacci series
    n1 = 0
    n2 = 1
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        for i in range(2, n): #está bn así, fib(5) no es 5, es 3
            num = n1 + n2
            n1 = n2
            n2 = num
        return num

print("5th Fibonacci's term:", fib(5))
print("10th Fibonacci's term:", fib(10))
print("15th Fibonacci's term:", fib(15))