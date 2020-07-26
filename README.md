# SudokuSolver

## Introduction
A simple visualisation of a sudoku board being solved using backtracking and pygame. There are 2 files that run the algorithm. One simply prints the solved board to the console (sudoku_solver.py) and the second uses pygame to show the algorithm running and produces the solved board (sudoku_solver_gui.py).

## Usage
To run the GUI version, change into the directory where the repository is located, and type into the console _python sudoku_solver_gui.py_. The board will be displayed and you can simple press SPACE to run the algorithm. To change the board to solve, simply replace the "grid" variable in the code to a 9x9 matrix containing the numbers for the board you want to solve. The algorithm may take longer depending on the difficulty of the board you want to use.

## Beware
Once the algorithm is complete, the only way to run it again is to close the program and launch it again, as I didn't implement a way to reset the board.
