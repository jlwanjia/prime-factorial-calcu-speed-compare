
def prime(n):
    prime = 2
    print(prime)
    for prime in range(3, n):
        for divisor in range (2, prime):
            if prime % divisor ==0:
                break
        else:
            print(prime)

def factorial(n):
    factorial = 1
    for i in range(1,n):
        factorial = factorial * (i + 1)
    print(factorial)

import timeit
print(timeit.timeit("prime(100)", "from __main__ import prime",number=1))
print(timeit.timeit("factorial(100)", "from __main__ import factorial",number=1))