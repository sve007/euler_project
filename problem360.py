# Given two points (x1,y1,z1) and (x2,y2,z2) in three dimensional space, the Manhattan distance between those
# points is defined as
# |x1-x2|+|y1-y2|+|z1-z2|.
#
# Let C(r) be a sphere with radius r and center in the origin O(0,0,0).
# Let I(r) be the set of all points with integer coordinates on the surface of C(r).
# Let S(r) be the sum of the Manhattan distances of all elements of I(r) to the origin O.
#
# E.g. S(45)=34518.
#
# Find S(10**10).

import itertools
import math
import time


def pyth_triplets(r):
    triplets = []
    lim = int(r/2*2**(1/2))+1
    start_b = r
    for a in range(0, lim):
        b = start_b
        while a**2 + b**2 >= r**2:
            if a**2 + b**2 == r**2:
                triplets.append([a, b])
                start_b = b
                break
            b -= 1

    return triplets

        # b = a
        # while r**2 - a**2 - b**2 >= 0:
        #     c = math.sqrt(r ** 2 - a ** 2 - b ** 2)
        #     if c % 1 == 0:
        #         # print(a,b,c)
        #         perms = set(list(itertools.product(*((x, -x) for x in [a, b, c]))))
        #         for p in perms:
        #             for p2 in set(itertools.permutations(p)):
        #                 quads.append(p2)
        #     b += 1

    # return set(quads)


def n_pyth_quads(r):
    quads = []
    for a in range(0, r+1):
        b = a
        while r**2 - a**2 - b**2 >= 0:
            c = math.sqrt(r ** 2 - a ** 2 - b ** 2)
            if c % 1 == 0:
                # print(a,b,c)
                perms = set(list(itertools.product(*((x, -x) for x in [a, b, c]))))
                for p in perms:
                    for p2 in set(itertools.permutations(p)):
                        quads.append(p2)
            b += 1

    return set(quads)


def manhattan_dist(x1, y1, x0=0, y0=0):
    return abs(x1-x0)+abs(y1-y0)


#
r = 45
start = time.time()
qs = pyth_triplets(r)
print(time.time() - start)
print(qs)

m = 0
for q in qs:
    m += manhattan_dist(q[0], q[1])
print(m)
# can't do this because the manhattan distance is not symmetrical
mt = (8*m-4)*(4*m-2)-2*(2*m-1)
print(mt)

# a**2 + b**2 + c**2 = r**2 for all integers

# These pythagorean quadruplets are calculated for all positive a b and c so the entire set is made up of 8 times
# as many. We need only calculate the manhattan distance of this first octant and multiply the end result by 8.
