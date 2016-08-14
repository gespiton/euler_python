"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import math


def isprime(n):
    if n == 1:
        return False
    M = math.floor(math.sqrt(n)) + 1
    for i in range(2, M):
        if n % i == 0:
            return False
    return True


def left_to_right(prime):
    for i in range(1, len(prime) + 1):
        # print(prime[:i])
        if not isprime(int(prime[:i])):
            return False
    return True


def right_to_left(prime):
    prime = prime[::-1]
    for i in range(1, len(prime) + 1):
        # print(prime[:i][::-1])
        if not isprime(int(prime[:i][::-1])):
            return False
    return True


count = 0
ite = 11
sum = 0
while True:
    if isprime(ite) and left_to_right(str(ite)) and right_to_left(str(ite)):
        print(ite)
        sum += ite
        count += 1
        if count == 11:
            break
    ite += 1
print(sum())
