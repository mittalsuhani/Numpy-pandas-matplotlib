#in this mini python project we will be creaating simple implementation of conway's game of life using python and numpy


import numpy as np
import time
import os

rows, cols = 20, 20

grid = np.random.choice([0, 1], size=(rows, cols))

def display(grid):
    os.system('cls' if os.name == 'nt' else 'clear')

    for row in grid:
        line = ""

        for cell in row:
            if cell == 1:
                line += "⬛"
            else:
                line += "⬜"

        print(line)

#display(grid)

def count_neighbors(grid, x, y):
    rows, cols = grid.shape
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):

            if i == 0 and j == 0:
                continue

            nx = x + i
            ny = y + j

            if 0 <= nx < rows and 0 <= ny < cols:
                count += grid[nx, ny]

    return count

def update(grid):
    rows, cols = grid.shape

    new_grid = grid.copy()

    for i in range(rows):
        for j in range(cols):

            neighbors = count_neighbors(grid, i, j)

            # Rule 1 & 3
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0

            # Rule 4
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1

    return new_grid

for _ in range(100):

    display(grid)

    grid = update(grid)

    time.sleep(0.2)

