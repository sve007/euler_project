# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

# Could make this recursive
def iterate(n):
    if n % 2 == 0:
        n = int(n/2)
    else:
        n = 3*n + 1

    return n


largest_chain = 0
largest_n = 0

# We can start calculating from half te asked limit, since the length of every chain can be increased by 1 by doubling
# the starting value.
ulim = 1_000_00
for n in range(int(ulim/2), ulim+1):
    init_n = n
    counter = 0
    while n != 1:
        n = iterate(n)
        counter += 1
    if counter > largest_chain:
        largest_chain = counter
        largest_n = init_n

print(f"The starting number {largest_n} generates the longest chain with a length of {largest_chain}")
