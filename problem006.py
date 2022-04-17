# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Brute force, numpy will experience integer overflow at large n
import numpy as np
n = 100
a = np.arange(1, n+1)
sum_squares = sum(a*a)
square_sum = sum(a)**2
print(square_sum - sum_squares)

# Use explicit formula for the series
sum = int(n*(n+1)/2)
print(sum**2 - sum_squares)
