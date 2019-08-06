"""
    In this code i will try to find the prime factors of a given number
"""
import time
import math
def findSquareRoot(Num):
    i = 1
    while i**2 < Num:
        i += 1 
    return i


def primeFactorization(Number):
    primes = []
    if Number % 2 == 0:
        primes.append(2)
        while Number % 2 == 0:
            Number /= 2
    if Number % 3 == 0:
        primes.append(3)
        while Number % 3 == 0:
            Number /= 3
    
    
    squreRoot = findSquareRoot(Number)
    #squreRoot = int(math.sqrt(Number))    

    
    
    for i in range(5,squreRoot+1,2):
        if Number % i == 0:
            primes.append(i)
            while Number % i == 0:
                Number /= i
    return primes
milis = time.time() * 1000
result = primeFactorization(600851475143)
total_time = (time.time() * 1000) - milis

print("Total time = ",total_time)
print(result , "\n\n")

