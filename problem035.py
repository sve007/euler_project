# The number, 197, is called a circular prime because
# all rotations of the digits: 197, 971, and 719,
# are themselves prime.
#
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import eulerproject_functions as ef

pl = set(ef.find_primes_below(n=1000000))
pl_check = pl
count = 0
cp = []
for p in pl:
    perms = set([int((str(p)[i:]+str(p)[:i])) for i, _ in enumerate(str(p))])
    if perms.issubset(pl_check):
        count += len(perms)
        cp.append(perms)
        pl_check = pl_check - perms
print(cp)
print(f"Answer to problem 35: {count}")
