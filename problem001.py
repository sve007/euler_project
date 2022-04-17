# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

n = 1000
base1 = 3
base2 = 5
print(list(range(1000)))
multiples = [number for number in range(n) if not (number % base1) or not (number % base2)]
answer = sum(multiples)
print(answer)