# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

with open("input_data/problem013_input.txt") as f:
    input_data = [int(i) for i in f.read().split("\n")]


print(str(sum(input_data))[0:10])