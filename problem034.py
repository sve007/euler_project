# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

# The maximum value for a n-digit number is n*9! For 8-digits numbers,
# the maximum value is 2903040, which is only 7 digits. This means that
# our upper limit is 10**7. Moreover, since the sum of the digits factorial must
# be equal to the input number, 7*9! is in itself our upper limit.
import math

totsum = 0

for n in range(3, 7*math.factorial(9)):
    sum = 0
    digits =[int(d) for d in str(n)]
    for d in digits:
        sum += math.factorial(d)
    if sum == n:
        totsum += n

print(totsum)
