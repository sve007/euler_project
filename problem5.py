# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def check(n, max_divisor):
    valid = True
    for i in range(1, max_divisor+1):
        if n % i != 0:
            valid = False
            break
    return valid


number = 0
maxd = 20
valid_found = False
while not valid_found:
    number += maxd
    valid_found = check(number, max_divisor=maxd)

print(number)
