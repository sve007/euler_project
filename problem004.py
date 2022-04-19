# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

numbers = []
max_val = 1000
for p in range(100, max_val):
    for q in range(p, max_val):
        numbers.append(p*q)

numbers.sort(reverse=True)
largest_palindrome = None
for n in numbers:
    if str(n) == str(n)[::-1]:
        largest_palindrome = n
        break

print(largest_palindrome)
