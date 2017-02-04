"""Find the number of letters used to name the numbers from 1 to 1000 using British convention."""


def name_number(n):
    """For int n, returns English name of n, using British convention. Name excludes hyphens and spaces.
    Assume 1 <= n <= 1000."""
    num = str(n)
    last_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                   "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n <= 19:  # name numbers from 1 to 19 directly
        c = last_digits[int(num[-2:])]
    elif 19 < n < 100:  # name numbers from 20 to 99 by concatenating name for tens digit with name for ones digit
        c = tens[int(num[-2]) - 2] + last_digits[int(num[-1])]
    elif n % 100 == 0 and n < 1000:
        # name numbers from 100 to 900 that are divisible by 100 by taking number in hundreds place and concatenating
        # with "hundred"
        c = last_digits[int(num[0])] + "hundred"
    elif n != 1000:
        # name numbers from 100 to 999 excluding those divisible by 100 by taking number in hundreds place, adding
        # "hundredand", then naming the other 2 decimal places recursively
        c = last_digits[int(num[0])] + "hundredand" + name_number(n % 100)
    else:  # name 1000
        c = "onethousand"
    return c


length_count = 0
for x in range(1, 1001):
    length_count += len(name_number(x))

print(length_count)
