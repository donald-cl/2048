import sys
from copy import deepcopy
import random
max_cell = 0
score = 0
grid = [[0 for _ in xrange(4)] for _ in xrange(4)]

def print_grid():
    print ""
    for row in grid:
        print row

def spawn_number():
    done = False
    while not done:
        rand_row = random.randint(0, 3)
        rand_col = random.randint(0, 3)
        rand_val = random.randint(1, 2)
        cell = grid[rand_row][rand_col]
        if  cell == 0:
            grid[rand_row][rand_col] = rand_val * 2
            done = True

def move(direction):
    global score
    if direction == 'up' or direction == 'u':
        starting_row = 1
        starting_col = 0
        for column in xrange(starting_col, len(grid)):
            done_row = 0
            for row in xrange(starting_row, len(grid)):
                if grid[row][column] == 0:
                    continue
                current_row = row
                while current_row > done_row:
                    next_cell = grid[current_row-1][column]
                    current_cell = grid[current_row][column]
                    if next_cell == 0:
                        grid[current_row-1][column] = grid[current_row][column]
                        grid[current_row][column] = 0
                        current_row -= 1
                    elif next_cell == current_cell:
                        grid[current_row][column] = 0
                        grid[current_row-1][column] *= 2
                        score += grid[current_row-1][column]
                        break
                    else:
                        break
    elif direction == 'down' or direction == 'd':
        starting_row = len(grid)-1
        starting_col = 0
        for column in xrange(starting_col, len(grid)):
            done_row = len(grid)-1
            for row in xrange(starting_row, -1, -1):
                if grid[row][column] == 0:
                    continue
                current_row = row
                while current_row < done_row:
                    next_cell = grid[current_row+1][column]
                    current_cell = grid[current_row][column]
                    if next_cell == 0:
                        grid[current_row+1][column] = grid[current_row][column]
                        grid[current_row][column] = 0
                        current_row += 1
                    elif next_cell == current_cell:
                        grid[current_row][column] = 0
                        grid[current_row+1][column] *= 2
                        score += grid[current_row+1][column]
                        break
                    else:
                        break
    elif direction == 'left' or direction == 'l':
        starting_row = 0
        starting_col = 1
        for row in xrange(starting_row, len(grid)):
            done_column = 0
            for col in xrange(starting_col, len(grid)):
                if grid[row][col] == 0:
                    continue
                current_col = col
                while current_col > done_column:
                    next_cell = grid[row][current_col-1]
                    current_cell = grid[row][current_col]
                    if next_cell == 0:
                        grid[row][current_col-1] = grid[row][current_col]
                        grid[row][current_col] = 0
                        current_col -= 1
                    elif next_cell == current_cell:
                        grid[row][col] = 0
                        grid[row][current_col-1] *= 2
                        score += grid[row][current_col-1]
                    else:
                        break
    elif direction == 'right' or direction == 'r':
        starting_row = 0
        starting_col = len(grid) - 1
        for row in xrange(starting_row, len(grid)):
            done_column = len(grid) - 1
            for col in xrange(starting_col, -1, -1):
                if grid[row][col] == 0:
                    continue
                current_col = col
                while current_col < done_column:
                    next_cell = grid[row][current_col+1]
                    current_cell = grid[row][current_col]
                    if next_cell == 0:
                        grid[row][current_col+1] = grid[row][current_col]
                        grid[row][current_col] = 0
                        current_col += 1
                    elif next_cell == current_cell:
                        grid[row][col] = 0
                        grid[row][current_col+1] *= 2
                        score += grid[row][current_col+1]
                    else:
                        break

def same_grid(old_grid, new_grid):
    for i in xrange(0, len(grid)):
        for i2 in xrange(0, len(grid)):
            if old_grid[i][i2] != new_grid[i][i2]:
                return False
    return True

print_grid()
spawn_number()
print_grid()
while True:
    print "your score is :[%d]" % score
    print "enter your move:"
    line = sys.stdin.readline()
    current_grid = deepcopy(grid)
    move(line.strip())
    if not same_grid(current_grid, grid):
        spawn_number()
    print_grid()
    if max_cell == 2048:
        print "Good job you won :)"
