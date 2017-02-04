"""In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right
and down, is indicated in bold red and is equal to 2427.

131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by only moving right and down."""

my_matrix = []
for line in open("81 Matrix.txt"):
    my_matrix.append([int(element) for element in line.strip().split(",")])
num_rows = len(my_matrix)
num_cols = len(my_matrix[0])

for row_num in reversed(range(num_rows)):
    for col_num in reversed(range(num_cols)):
        if row_num == num_rows-1 and col_num == num_cols-1:  # current element is at bottom right corner
            pass
        elif row_num == num_rows-1:  # current element is in bottom row but not right column
            my_matrix[row_num][col_num] += my_matrix[row_num][col_num+1]
        elif col_num == num_cols-1:  # current element is in right column but not bottom row
            my_matrix[row_num][col_num] += my_matrix[row_num+1][col_num]
        else:  # current element is in neither the bottom row nor the right column
            my_matrix[row_num][col_num] += min(my_matrix[row_num][col_num+1], my_matrix[row_num+1][col_num])

print(my_matrix[0][0])
