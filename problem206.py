# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.

# Lemma 1: Since the square ends in 0, the positive integer n must end with 0.
# Additionally, an integer ending in 0 will have a square ending in 00, so we know that the last "_" must be a zero.
# We can then search for n/10 and find a square of pattern 1_2_3_4_5_6_7_8_9.

# Lemma 2: A square number ending in 9 will have a root ending in 3 or 7. We can thus search numbers ending in 3 or 7

# Lemma 2: We have a lower and upper bound for the square, by filling all the blanks with 0's and 9's respectively.
# The lower and upper bound for our search space is then the root of 1020304050607080900

for i in range(10**8+3, int(2**(1/2))*10**9, 10):
    if str(i**2)[::2] == "123456789":
        print(f"Found it: {i}. Squaring this yields {i**2}")
        break
    if str((i+4)**2)[::2] == "123456789":
        print(f"Found it: {i+4}0. Squaring this yields {(i+4)**2}00")
        break
