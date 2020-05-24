grid =   [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]] 

def print_grid(grid): 
    for(i) in range(9): 
        for (j) in range(9): 
            print(str(grid[i][j]) + " ", end="")
        print('\n')

def find_empty(grid):

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return False

def is_valid(grid, row, col, num):
    return valid_row(grid, row, num) and valid_col(grid, col, num) and valid_box(grid, row, col, num)

def valid_row(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
            return False
    return True

def valid_col(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return False
    return True

def valid_box(grid, row, col, num):
    for i in range(3):
        for j in range(3):
            row_check = i + (row - (row % 3))
            col_check = j + (col - (col % 3))
            if grid[row_check][col_check] == num:
                return False
    return True

def solve(grid):

    indices = [0, 0]

    if not find_empty(grid):
        return True
    indices = find_empty(grid)

    row = indices[0]
    col = indices[1]


    for i in range(1, 10):
        if is_valid(grid, row, col, i):
            grid[row][col] = i
            if solve(grid):
                return True
            grid[row][col] = 0

    return False
        

solve(grid)
print_grid(grid)

