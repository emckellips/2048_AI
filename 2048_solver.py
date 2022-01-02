import copy
import numpy as np
import random

def load_grid():
    grid = np.zeros((4, 4))
    xPos = random.randint(0, 3)
    yPos = random.randint(0, 3)
    grid[xPos, yPos] = 2
    while True:
        xPos = random.randint(0, 3)
        yPos = random.randint(0, 3)
        if grid[xPos, yPos] != 2:
            grid[xPos, yPos] = 2
            break
    print(grid)
    return grid

def compute_lines(row):
    a = row[0]
    b = row[1]
    c = row[2]
    d = row[3]
    if a == 0:
        a = b
        b = c
        c = d
        d = 0
    if b == 0:
        b = c
        c = d
        d = 0
    if c == 0:
        c = d
        d = 0
    if c == d:
        c += d
        d = 0
    if b == c:
        b += c
        c = d
        d = 0
    if a == b:
        a += b
        b = c
        c = d
        d = 0
    if a == 0:
        a = b
        b = c
        c = d
        d = 0
    return [a, b, c, d]

def compute_successors(grid):
    left = copy.deepcopy(grid)
    right = copy.deepcopy(grid)
    up = copy.deepcopy(grid)
    down = copy.deepcopy(grid)

    for i in range(4):

        # Left successor
        left[i] = compute_lines(left[i])

        # Right successor
        tempRow = compute_lines(right[i])
        temp = tempRow[0]
        tempRow[0] = tempRow[3]
        tempRow[3] = temp
        temp = tempRow[1]
        tempRow[1] = tempRow[2]
        tempRow[2] = temp
        right[i] = tempRow

        # Up successor
        a = up[0][i]
        b = up[1][i]
        c = up[2][i]
        d = up[3][i]
        vert_col = [a, b, c, d]
        vert_col = compute_lines(vert_col)
        up[0][i] = vert_col[0]
        up[1][i] = vert_col[1]
        up[2][i] = vert_col[2]
        up[3][i] = vert_col[3]

        # Down successor
        temp = vert_col[0]
        vert_col[0] = vert_col[3]
        vert_col[3] = temp
        temp = vert_col[1]
        vert_col[1] = vert_col[2]
        vert_col[2] = temp
        down[0][i] = vert_col[0]
        down[1][i] = vert_col[1]
        down[2][i] = vert_col[2]
        down[3][i] = vert_col[3]

    return left, right, up, down



if __name__ == '__main__':
    grid = load_grid()
    compute_successors(grid)