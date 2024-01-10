import turtle
from pprint import pprint
import random

# Generate a full grid of numbers (fully filled in). This step is more complex as it seems as we cannot just randomly generate 
# numbers to fill in the grid. We have to make sure that these numbers are positioned on the grid following 
# the Sudoku rules. To do so will use a sudoku solver algorithm (backtracking algorithm) that we will apply to 
# an empty grid. We will add a random element to this solver algorithm to make sure that a new grid is generated every time we run it.
# From our full grid, we will then remove 1 value at a time.
# Each time a value is removed we will apply a sudoku solver algorithm to see if the grid can still be solved and to count the number of solutions it leads to.
# If the resulting grid only has one solution we can carry on the process from step 2. If not we will have to put the value we took away back in the grid.
# We can repeat the same process (from step 2) several times using a different value each time to try to remove additional numbers, resulting in a more difficult grid to solve. 
# The number of attempts we will use to go through this process will have an impact on the difficulty level of the resulting grid.

t = turtle.Turtle()

# creates blank grid
grid = []
for i in range(0,9):
    temp = []
    for j in range(0,9):
        temp.append(0)
    grid.append(temp)

numbers = [1,2,3,4,5,6,7,8,9]


# width = 500
# height = 500

# sc = turtle.Screen()
# sc.setup(width,height)

# t.pensize(3)
# t.pendown
# t.goto(-250,250)   


# x = input("de")





def isValid(row, col, num):
    # check to see if the number is in the row
    if num in grid[row]:
        return False
    
    # check to see if the number is in the column
    if num in [grid[n][col] for n in range(0, 9)]:
        return False
    
    # check to see if the number is in the 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

    

def fillNumbers(row, col):
    if row == 9:
        return True
    
    if col == 9:
        return fillNumbers(row + 1, 0)

    if grid[row][col] != 0:
        return fillNumbers(row, col + 1)

    for num in random.sample(numbers, len(numbers)):
        if isValid(row, col, num):
            grid[row][col] = num
            if fillNumbers(row, col + 1):
                return True
            grid[row][col] = 0

    return False    

def fillGrid():
    fillNumbers(0,0)
    pprint(grid)
      

fillGrid() 

