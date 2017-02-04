"""The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell
in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by
80 matrix, from the left column to the right column."""

my_matrix = []
for line in open("81 Matrix.txt"):
    my_matrix.append([int(element) for element in line.strip().split(",")])
num_rows = len(my_matrix)
num_cols = len(my_matrix[0])

for col_num in reversed(range(num_cols-1)):
    for row_num in range(num_rows):  # go down column, determining whether it's better to go up or right
        if row_num == 0:  # we are at first row
            my_matrix[row_num][col_num] += my_matrix[row_num][col_num+1]
        else:  # we are not at the first row
            my_matrix[row_num][col_num] += min(my_matrix[row_num][col_num+1], my_matrix[row_num-1][col_num])
    for row_num in reversed(range(num_rows)):  # go up column, determining whether it's best to go down
        if row_num != num_rows-1:
            my_matrix[row_num][col_num] = min(my_matrix[row_num][col_num], my_matrix[row_num+1][col_num] + my_matrix[row_num][col_num])

print(min([my_matrix[row][0] for row in range(num_rows)]))
