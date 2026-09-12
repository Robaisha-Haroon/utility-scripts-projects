# Utility Program

%%writefile utility.py

import math
# Function for square root
def sqaureroot(a):
    return math.sqrt(a)
# Fuction for factorial   
def factorial(a):
    return math.factorial(a)
# Function for prime checker    
def prime_check(a):
    if a<= 1:
        return (f"{a} is not prime number")
    for i in range (2,a):
            if a%i == 0:
                return (f"{a} is not prime number")
    return (f"{a} is prime number")
# Function for finding sum
def sum_of_natural(a, sum= 0):
    for i in range(1, a+1):
        sum += i
    return sum
