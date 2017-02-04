"""Computes the product of positive integers abc such that a^2+b^2=c^2, a<b<c, and a+b+c=1000."""

for a in range(1, 333):  # a must between 1 and 332, inclusively

    for b in range(a+1, 500):  # b is between a+1 and 499, inclusively

        for c in [d for d in range(b+1, 998) if a+b+d==1000]:
        # c is between b+1 and 997, inclusively; a+b+c must equal 1000

            if a**2 + b**2 == c**2:
                print(a * b * c)
                break
