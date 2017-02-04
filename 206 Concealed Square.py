"""Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit."""

for x in range(1010101010, 1389026630, 10):
    square = str(x ** 2)
    if (square[0], square[2], square[4], square[6], square[8], square[10], square[12], square[14], square[16]) == \
            ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        print(x)
        break
