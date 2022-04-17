# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
# a 15K text file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18.
# It is not possible to try every route to solve this problem,
# as there are 299 altogether! If you could check one trillion (1012) routes every second
# it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

with open("input_data/problem067_input.txt") as f:
    pyr = f.read().split("\n")
    for i, row in enumerate(pyr):
        pyr[i] = [int(j) for j in row.split(" ")]

helper_pyr = pyr[::-1]

for i, row in enumerate(pyr[::-1]):
    if not (i == 0 or i == (len(pyr)-1)):
        for j, number in enumerate(row):
            helper_pyr[i][j] = max(number+helper_pyr[i-1][j], number+helper_pyr[i-1][j+1])

helper_pyr = helper_pyr[::-1]
max_sum = helper_pyr[0][0] + max(helper_pyr[1])

print(max_sum)
