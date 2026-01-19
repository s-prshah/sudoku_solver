from copy import deepcopy
from datetime import datetime
from typing import List
import math

# Generic Sudoku Solver
# ******************************
# A sudoku puzzle is one such that given a set of unique characters, each row, column, and
# square grid can only have 1 each character. See https://masteringsudoku.com/sudoku-rules-beginners/
# for more information on how to play.
#
# Your job is to write a solver that takes a sudoku puzzle and fills in all the characters correctly.
# Puzzles for this assignment use any characters, not just traditional numbers 1-9, and the
# size can vary/is not always 9x9 (side length will always be a square number). Spots that are not
# filled in have None in them.
#
# Tips:
# - Sets are your friend!
# - solve is a wrapper; you will need a recursive version of the solve function
# - It is worthwhile to consider what you should initialize before starting your recursive algorithm
# - If you are not sure where to start, use previous backtracking exercises for inspiration
#
# Extensions:
# 1) If you are backtracking in empty cell order, try optimizing the solver by finding more optimal empty
#    cells to use for your subsequent recursive calls. See how fast you can get the 16x16 test to finish!:)
#    Uncomment the 16x16 advanced test to put things to the test (see if you can get it to run in under 10 min)
# 2) Use tkinter to put a UI around the solver, where you can type in your own puzzles to solve!
# 3) Write a Sudoku puzzle creator

class SudokuSolver:

    # Constructor
    # ************************
    # cell_options param might look like ["W", "L", "F", "S", "T", "R", "N", "G", "P"]
    # The size of the grid will always be the length of cell_options  
    def __init__(self, cell_options:List[str]) -> None:
        self.cell_options = cell_options
   
    # solve
    # *************************
    # Takes a sudoku grid with some values filled in (2D array) and returns a solution grid
    # with all cells filled in (also a 2D array).  Empty cell values are None.
    def solve(self, grid:List[List[str]]) -> List[List[str]]:
        all_vals = set(self.cell_options)

        #check if the currently selected value in the for-loop in the recursive function is valid
        def is_valid(row, col, val):
            #if the value is already present in it's row in the grid, automatically return false because val is not valid
            for temp_row in range(len(grid)):
                if grid[temp_row][col] == val:
                    return False
           
           #if the value is already present in it's column in the grid, automatically return false because val is not valid
            for temp_col in range(len(grid)):
                if grid[row][temp_col] == val:
                    return False
           
           #create box contants to check value in each box inside the grid 
           #box size is size of each box
           #box_row and box_num helps find the position of the box on the grid 
            box_size = int(math.sqrt(len(grid)))
            box_num_row = int(row // box_size)
            box_num_col = int(col // box_size)

            #iterate through each value within the selected box on the grid 
            for temp_row in range(box_size):
                for temp_col in range(box_size):
                    if grid[temp_row + (box_num_row * box_size)][temp_col + (box_num_col * box_size)] == val:
                        return False

            return True

        #secondary recursive function/ backtracking function  
        #checks each value of set all_vals until function finds value that's valid for the position (given by row and col parameters) using the is_valid function
        #backtracks if recursive call returns false 
        def check_vals(row, col):
            for val in all_vals:
                if is_valid(row, col, val):
                    grid[row][col] = val
                    if solver(row + 1, col):
                        return True
                    grid[row][col] = None

        #main recursive function 
        #base case starts with (0,0) on grid and with every recursive call, moves onto the next row
        #function skips over a grid location if there's already a value in it
        #calls check_vals function for backtracking
        def solver(row, col):
            if row == len(grid):
                col += 1
                row = 0
                if col == len(grid):
                    return True

            if grid[row][col] != None:
                return solver(row + 1, col)

            return check_vals(row, col)

        #calls recursive function to return grid if the grid is possible 
        if solver(0, 0) == True:
            return grid
        else:
            return None