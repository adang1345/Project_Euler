"""Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but
credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin
Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that
each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle
grid and its solution grid.

[image]

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to
employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The
complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be
solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left corner of the solution grid above."""

import copy
import math


class Sudoku:
    """A class for a Sudoku grid."""

    def __init__(self, numbers):
        """Create a Sudoku grid. numbers is a 9x9 2D list containing the start grid. Each element of the 2D list
        is a set containing all possible numbers that can be at the position in a valid grid."""
        self.numbers = numbers

    def __repr__(self):
        """Print the Sudoku grid"""
        s = ""
        for x in range(9):
            if x % 3 == 0 and x != 0:
                s += "-" * 113 + "\n"
            for y in range(9):
                if y % 3 == 0 and y != 0:
                    s += "|\t"
                str_entry = "".join(str(a) for a in self.numbers[x][y])
                s += str_entry + " "*(9-len(str_entry)) + "\t"
                if y == len(self.numbers[0]) - 1:
                    s += "\n"
        return s

    def __eq__(self, other):
        """Return whether two Sudoku boards are equal."""
        if not isinstance(other, Sudoku):
            return False
        for r in range(1, 10):
            if self.row(r) != other.row(r):
                return False
        return True

    def square(self, x, y):
        """Return a list of the elements of the row x, column y 3x3 square of this puzzle. Rows are counted starting
        from the top, and columns are counted starting from the left.
        Precondition: x,y are integers in 1..3"""
        s = []
        r_start = 3*(x-1)
        c_start = 3*(y-1)
        for x in range(r_start, r_start+3):
            for y in range(c_start, c_start+3):
                s.append(self.numbers[x][y])
        return s

    def invsquare(self, x, y):
        """Given the row x, column y position of an element in this grid, return a tuple saying which square this
        element is in."""
        return math.ceil(x/3), math.ceil(y/3)

    def row(self, x):
        """Return row x of the grid as a list. Rows are counted starting from the top."""
        return self.numbers[x-1]

    def column(self, y):
        """Return column y of the grid as a list. Columns are counted starting from the left"""
        return [self.numbers[x][y-1] for x in range(len(self.numbers))]

    def _is_complete(self, l):
        """Return True if list l contains all sets of single integers in 1..9"""
        for n in range(1, 10):
            if {n} not in l:
                return False
        return True

    def is_solved(self):
        """Return whether this puzzle is solved."""
        for x in self.numbers:
            for y in x:
                if len(y) > 1:
                    return False
        for row in range(9):
            if not self._is_complete(self.row(row)):
                return False
        for col in range(9):
            if not self._is_complete(self.column(col)):
                return False
        for row in range(1, 4):
            for col in range(1, 4):
                if not self._is_complete(self.square(row, col)):
                    return False
        return True

    def backtrack_solve(self):
        """Solve this puzzle as much as possible using backtracking. Return True if the puzzle has been solved. Return
        False if the puzzle is unsolvable."""
        # find first unsolved cell
        for s in range(81):
            if len(self.numbers[s//9][s%9]) > 1:
                break
        if s == 80 and len(self.numbers[8][8]) == 1:  # return True if puzzle is solved
            return True
        # try each value in current cell
        ds_copy = self.numbers[s//9][s%9].copy()
        for d in ds_copy:
            square = self.invsquare(s//9+1, s%9+1)
            if {d} in self.row(s//9+1) or {d} in self.column(s%9+1) or {d} in self.square(square[0], square[1]):
                continue
            self.numbers[s//9][s%9] = {d}
            if self.backtrack_solve():
                return True
        # All digits have been tried and have failed, so restore the current cell and return False
        self.numbers[s//9][s%9] = ds_copy
        return False

    def solve(self):
        """Solve this puzzle.
        Precondition: This puzzle has a unique solution."""
        original = copy.deepcopy(self)
        while True:
            for r in range(1, 10):
                for c in range(1, 10):
                    if len(self.numbers[r-1][c-1]) == 1:
                        continue
                    removed = []
                    for n in self.numbers[r-1][c-1]:
                        square = self.invsquare(r, c)
                        if {n} in self.row(r) or {n} in self.column(c) or {n} in self.square(square[0], square[1]):
                            removed.append(n)
                    for x in removed:
                        self.numbers[r-1][c-1].remove(x)
            if self == original:
                break
            else:
                original = copy.deepcopy(self)
        self.backtrack_solve()
        assert self.is_solved()


grids = []
f = open("96 Su Doku.txt")
prev_line = "@"
for line in f:
    if prev_line[0] == "G":
        grids.append(line.rstrip())
    elif line[0] != "G":
        grids[-1] += line.rstrip()
    prev_line = line

c = 0
for grid in grids:
    g = [[{None} for _ in range(9)] for __ in range(9)]
    for x in range(9):
        for y in range(9):
            if grid[9*x+y] == "0":
                g[x][y] = {1,2,3,4,5,6,7,8,9}
            else:
                g[x][y] = {int(grid[9*x+y])}
    s = Sudoku(g)
    s.solve()
    print(s)
    c += 100 * next(iter(s.numbers[0][0])) + 10 * next(iter(s.numbers[0][1])) + next(iter(s.numbers[0][2]))

print(c)
