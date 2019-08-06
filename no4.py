"""
    4th problem of the Project Euler
"""
    #Largest palindome made from the product of 3-digit numbers.
import time

def isPalindome(number):
    temp = number
    rev = 0
    while(temp > 0):
        dig = temp % 10
        rev = (rev * 10) + dig
        temp = temp // 10
    if(number == rev):
        return True
    return False

def findingProducts():
    allPalindomes = []
    for i in range(999,100,-1):
        for j in range(i, 100,-1):
            if isPalindome(i*j):
                allPalindomes.append(i*j)
    return allPalindomes

start_time = time.time() * 1000
result = max(findingProducts())  
print("Time it takes = ", (time.time() * 1000) - start_time)
print(result)
