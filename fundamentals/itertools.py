#!/usr/bin/env python3

from itertools import islice, count
from math import sqrt


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def thousand_primes():
    return islice((x for x in count() if is_prime(x)), 1000)


print(list(thousand_primes()))
print(sum(thousand_primes()))

cities = ['London', 'New York', 'Pittsburg']
x = all(name == name.title() for name in cities)
print(x)
