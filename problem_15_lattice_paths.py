grid_size = 21
lattice = []

# create lattice
for i in range(grid_size):
    lattice.append([])
    for j in range(grid_size):
        lattice[i].append('-')

# add ones
for i in range(grid_size):
    lattice[0][i] = 1
    lattice[i][0] = 1

# fill lattice with possible amount of paths on each step
for row in range(1, grid_size):
    for col in range(1, grid_size):
        lattice[row][col] = lattice[row][col - 1] + lattice[row - 1][col]
for r in lattice:
    print(r)
