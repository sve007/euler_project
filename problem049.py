# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of
# three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating
# the three terms in this sequence?

import eulerproject_functions as ef

primes = ef.find_primes_below(9999)
primes = [p for p in primes if (p > 999 and p < 9999-6660)]

for p in primes:
    if ef.is_prime(p+3330):
        if ef.is_prime(p+3330+3330):
            if set(list(str(p))) == set(list(str(p+3330))):
                if set(list(str(p))) == set(list(str(p+6660))):
                    valid_terms = [p, p + 3330, p + 3330 + 3330]
                    print(f"{valid_terms}")

print(f"Answer to problem 49: {valid_terms[0]}{valid_terms[1]}{valid_terms[2]}")
