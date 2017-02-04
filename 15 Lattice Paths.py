"""Find the number of paths from top left corner of 20x20 grid to bottom right corner, moving only right or down"""

from math import factorial
print(factorial(20+20) // (factorial(20))**2)
