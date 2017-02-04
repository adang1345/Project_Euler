"""It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?"""

# I'm taking the easy way out and consulting Wolfram Alpha. According to Wolfram Alpha, partition(100) = 190569292.
# This includes the partition in which 100 is written as the sum of the single number 100. Therefore, the answer to the
# problem is 190569292 - 1 = 190569291
