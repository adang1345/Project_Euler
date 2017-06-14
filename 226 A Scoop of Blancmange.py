"""https://projecteuler.net/problem=226

The lower and upper limits of the integral are 0.0789077879653419 and 0.5, respectively. These values were obtained
using the WolframAlpha query "solve Takagi(x)=1/2-sqrt((x-2*x^2)/2) for x".

The formula for integrating the Blancmange curve was obtained from the Wikipedia page
https://en.wikipedia.org/wiki/Blancmange_curve#Integrating_the_Blancmange_curve.
"""


def s(x):
    """The s-function as explained in https://en.wikipedia.org/wiki/Blancmange_curve#Integrating_the_Blancmange_curve.
    Precondition: x is an int or float >= 0"""
    assert x >= 0
    if x <= 0.5:
        return x**2 / 2
    elif x <= 1:
        return -x**2 / 2 + x - 0.25
    else:
        n = int(x)
        return n / 4 + s(x-n)


def i(x, n):
    """Return an estimate of the integral of the Blancmange curve from 0 to x with n iterations. As n increases, the
    estimate becomes more accurate.
    Preconditions: x is an int or float in the range [0, 1]
                   n is an int >= 0"""
    assert 0 <= x <= 1 and n >= 0
    return sum(1/4**a * s(2**a * x) for a in range(n))


# find the area under the Blancmange curve
under_blancmange = i(0.5, 100) - i(0.0789077879653419, 100)

# find area under circle (done using a TI-89 calculator)
under_circle = 0.122310730726

print(round(under_blancmange-under_circle, 8))
