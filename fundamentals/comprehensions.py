#!/usr/bin/env python3

from math import factorial, sqrt
import os
import glob

words = ("Why sometimes I belived as many as six impossible things before "
         "breakfast").split()

x = [len(word) for word in words]
print(x)

# list
f = [factorial(x) for x in range(20)]
print(f)

# set
f = {factorial(x) for x in range(20)}
print(f)

# dictonary
file_sizes = {os.path.realpath(p): os.stat(p).st_size
              for p in glob.glob("*.py")}

print(file_sizes)


# filtering
def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

x = [x for x in range(101) if is_prime(x)]
print("Primes: ", x)

# print prime square divisors
x = {x*x: (1, x, x*x) for x in range(101) if is_prime(x)}
print("Prime Square Divisors: ", x)
