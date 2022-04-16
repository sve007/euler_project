# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import eulerproject_functions as ef

primes = ef.find_primes_below(2_000_000)
print(sum(primes))