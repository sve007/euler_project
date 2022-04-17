# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

with open("input_data/problem08_input.txt") as f:
    input_data = [i for i in f.read().split("\n")]

# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?
input_data = "".join(input_data)
# Convert elements to ints
ll = 0
ul = 13
input_data = [int(i) for i in input_data]

greatest_prd = 0
numbers = []
# Loop through each set of 13 adjacent digits
while ul <= len(input_data):
    prd = 1
    # Calculate product of set
    for n in input_data[ll:ul]:
        prd = prd * n
    if prd > greatest_prd:
        greatest_prd = prd
        numbers = input_data[ll:ul]
    ll += 1
    ul += 1

print(greatest_prd, numbers)
