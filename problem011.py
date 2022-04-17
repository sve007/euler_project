# In the 20×20 grid below (see input file), four numbers along a diagonal line have been marked in red.

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?

with open("input_data/problem011_input.txt") as f:
    grid = [row.split(" ") for row in f.read().split("\n")]

for i, row in enumerate(grid):
    grid[i] = [int(j) for j in row]

greatest_prd = 0

chain_size = 4
# At the edges of the grid, the chain size will be larger than there are numbers left in the grid.
# However, Python slicing will not throw an error and replace the slicing value with the maximum value
# of that dimension. Only in the last cases of diagonal chains this will be a problem since we do not use slices
# and additionally for the left diagonal, negative indices will wrap around.
for row, _ in enumerate(grid):
    for col, _ in enumerate(grid):

        # Check horizontal product
        prd = 1
        for d in grid[row][col:col+chain_size]:
            prd = prd*d
        if prd > greatest_prd:
            greatest_prd = prd

        # Check vertical product
        prd = 1
        for d in [r[col] for r in grid[row:row+chain_size]]:
            prd = prd * d
        if prd > greatest_prd:
            greatest_prd = prd

        # Check right diagonal product.
        prd = 1
        for r, c in zip(range(row, row+chain_size), range(col, col+chain_size)):
            try:
                prd = prd*grid[r][c]
            except IndexError:
                continue
        if prd > greatest_prd:
            greatest_prd = prd

        # Check left diagonal product
        # Here we must be cautious to not include negative indices that will cause the chain to 'wrap around' the grid.
        # We can fix this by shifting the starting position of the col index by the chain size
        prd = 1
        for r, c in zip(range(row, row+chain_size), range(col+chain_size-1, col-1, -1)):
            try:
                prd = prd*grid[r][c]
            except IndexError:
                continue
        if prd > greatest_prd:
            greatest_prd = prd

print(greatest_prd)
