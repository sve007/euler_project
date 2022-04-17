# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1, 332):
    b = a + 1
    c = 1000 - a - b
    while c > b:
        if a**2 + b**2 == c**2:
            if a + b + c == 1000:
                print(a, b, c, a * b * c)
                break
        b += 1
        c -= 1
    else:
        continue
    break
