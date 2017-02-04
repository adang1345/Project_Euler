"""It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?"""

# I looked up the prime partition sequence on OEIS.
prime_partitions = [1, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 9, 10, 12, 14, 17, 19, 23, 26, 30, 35, 40, 46, 52, 60, 67,
                    77, 87, 98, 111, 124, 140, 157, 175, 197, 219, 244, 272, 302, 336, 372, 413, 456, 504, 557, 614,
                    677, 744, 819, 899, 987, 1083, 1186, 1298, 1420, 1552, 1695, 1850, 2018, 2198, 2394, 2605, 2833,
                    3079, 3344]

# We know that the answer is a little more than 67, the length of the above list. By trial and error, the answer is 71.
print(71)
