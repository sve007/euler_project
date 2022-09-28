# Surprisingly there are only three numbers that can be written
# as the sum of fourth powers of their digits:
#
# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written
# as the sum of fifth powers of their digits.

# The maximum sum for a number is the amount of digits multiplied by 9**5.
# This means that for 7 digit numbers the maximum value is 7*9**5 = 413343,
# which is smaller than the smallest 7 digit number; 1000000. Even better,
# we know that our upper limit is 413343 since the sum has to be equal to
# the original number.

totsum = 0

for n in range(2, 413343):
    sum = 0
    sum_ = [int(letter) for letter in str(n)]
    for i in sum_:
        sum += i**5
    if n == sum:
        totsum += sum

print(totsum)
