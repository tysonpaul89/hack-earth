 # Sieve of Eratosthenes Algorithm
 # Ref: https://www.geeksforgeeks.org/sieve-of-eratosthenes/
num = int(input())
primes = [True for i in range(num+1)]
r = []
p = 2
while (p**2 <= num):
    if (primes[p] == True):
        for i in range(p**2, num+1, p):
            primes[i] = False

    p += 1
print(' '.join([str(p) for p in range(2, num) if primes[p]]))
