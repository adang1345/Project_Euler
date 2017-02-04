"""In England the currency is made up of pound and pence, and there are eight coins in general circulation:
1 pence, 2 pence, 5 pence, 10 pence, 20 pence, 50 pence, 100 pence and 200 pence.
How many different ways can 200 pence be made using any number of coins?"""

# This is same as finding all positive integer solutions a, b, c, d, e, f, g, h for which
# a + 2b + 5c + 10d + 20e + 50f + 100g + 200h = 200.

all_solutions = []

for a in range(201):
    # a must be between 0 and 200, inclusively
    for b in range((200 - a)//2 + 1):
        # b must be between 0 and (200 - a)/2, inclusively
        for c in range((200 - a - 2*b)//5 + 1):
            # c must be between 0 and (200 - a - 2*b)/5, inclusively
            for d in range((200 - a - 2*b - 5*c)//10 + 1):
                # d must be between 0 and (200 - a - 2*b - 5*c)/10, inclusively
                for e in range((200 - a - 2*b - 5*c - 10*d)//20 + 1):
                    # e must be between 0 and (200 - a - 2*b - 5*c - 10*d)/20, inclusively
                    for f in range((200 - a - 2*b - 5*c - 10*d - 20*e)//50 + 1):
                        # f must be between 0 and (200 - a - 2*b - 5*c - 10*d - 20*e)/50, inclusively
                        for g in range((200 - a - 2*b - 5*c - 10*d - 20*e - 50*f)//100 + 1):
                            # g must be between 0 and (200 - a - 2*b - 5*c - 10*d - 20*e - 50*f)/100, inclusively
                            for h in range((200 - a - 2*b - 5*c - 10*d - 20*e - 50*f - 100*g)//200 + 1):
                                # h must be between 0 and (200 - a - 2*b - 5*c - 10*d - 20*e - 50*f - 100*g)/200, inclusively
                                if a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h == 200:
                                    all_solutions.append([a, b, c, d, e, f, g, h])

print(len(all_solutions))
