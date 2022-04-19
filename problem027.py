# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39$.
# However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes
# for the consecutive values 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:

# n^2 + an + b, where |a| < 1000$ and |b| <= 1000
# where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4

# Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the
# maximum number of primes for consecutive values of $n$, starting with n = 0.

# n can go up to a, so there are a number of values to check for each combination of a and b.
# There are 2001 combinations per value of a, and 2000 values of a, which means 2001*2000 = 4_002_000 options to try.
# This can be brute forced.
# Moreover, we always test n = 0 first, such that the first option to test is simply b. This means we only need to
# for b's that are prime.

import eulerproject_functions as ef


def nprimes(a, b):
    valid = True
    n = 0
    while valid:
        p = n**2 + a*n + b
        if not ef.is_prime(p):
            valid = False
        else:
            n += 1
    return n


# Generate primes under 1000 to try
bs = ef.find_primes_below(1000)
longest_chain, longest_a, longest_b = 0, 0, 0
for b in bs:
    for a in range(-999, 1000):
        chain_length = nprimes(a, b)
        if chain_length > longest_chain:
            longest_chain = chain_length
            longest_a, longest_b = a, b

print(longest_a*longest_b)
