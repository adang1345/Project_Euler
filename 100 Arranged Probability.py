"""If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were
taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing
eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue
discs that the box would contain."""

"""This problem is equivalent to solving the diophantine equation 2B^2-2B-T^2+T=0, where T is the total number of dics
and B is the total number of blue dics. We want the smallest solution in T for which T > 10^12.

From the website https://www.alpertron.com.ar/QUAD.HTM, I found that given one solution (B1,T1), the next largest
solution is  B2 = 3*B1 + 2*T1 - 2  and  T2 = 4*B1 + 3*T1 - 3."""

b = 15
t = 21
while t < 1000000000000:
    b_prev = b
    b = 3 * b + 2 * t - 2
    t = 4 * b_prev + 3 * t - 3

print("There are " + str(b) + " blue discs in a box of " + str(t) + " total dics.")
