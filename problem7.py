# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import prime_functions as pf

generator = pf.generate_primes(1, 10002, indexlim=True)
primes = list(generator)

print(primes[-1])