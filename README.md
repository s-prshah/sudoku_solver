# Sudoku Solver (Backtracking + Constraint Checking)

A Python implementation of a **generic Sudoku solver** using recursive backtracking and constraint validation. The solver supports **variable board sizes** (not limited to 9×9) and works with any set of unique symbols.

> Note: Completed as part of a coursework project. All code shown here was implemented by me and is included in my portfolio.

---

## Features
- Solves Sudoku puzzles using **recursive backtracking**
- Supports **generalized n×n boards** (where n is a perfect square)
- Works with arbitrary symbols (not only numbers)
- Validates candidate values using row/column/subgrid constraints
- Skips pre-filled cells and backtracks on invalid branches

---

## Key Components
- `SudokuSolver(cell_options)`
  - `solve(grid)` → returns solved grid or `None` if unsolvable
- `is_valid(row, col, val)`
  - Checks row, column, and subgrid constraints
- Backtracking engine
  - Tries candidate values, recurses, and undoes assignments on failure

---

## Concepts & Data Structures
- Recursion + backtracking search
- Constraint satisfaction / pruning
- Sets for candidate options
- Subgrid indexing using `sqrt(n)` logic

---

## Author
**Prisha Shah**
