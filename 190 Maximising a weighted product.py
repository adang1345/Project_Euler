"""https://projecteuler.net/problem=190

I initially tried using Lagrange multipliers to generate systems of polynomial equations and let Maxima solve them.
However, when I tried to calculate [P7], the equation solver took too long. I then looked for patterns in the solution
for small values and discovered that at the maximum, xn = 2n/(m+1)."""


# def maxima_analyze(s):
#     """Analyze a string s generated by Maxima containing solutions obtained when using the method of Lagrange
#     multipliers. Return the constrained maximum."""
#     s = [[float(y[y.index("=")+1:]) for y in x.split(",") if y[y.index("=")-1] != "l"]
#          for x in s.replace("\n","").strip("[]").split("],[")]
#     m = 0
#     for x in s:
#         prod = 1
#         for e in range(len(s[0])):
#             prod *= x[e] ** (e+1)
#         m = max(prod, m)
#     return m
#
#
# s2 = "[[x1=0.6666666666666666,x2=1.333333333333333,l=1.777777777777778],[x1=2,x2=0,l=0]]"
# s3 = """[x1=0.5,x2=1,x3=1.5,l=3.375],[x1=0,x2=
# 0,x3=3,l=0],[x1=1,x2=2,x3=0,l=0],[x1=0.75,x2=0,x3=2.25,l=0],[x1=0,x2=3,x3=0,l=0],[x1=3,x2=0,x3=0,l=0]]"""
# s4 = """[x1=0.4,x2=0.8,
# x3=1.2,x4=1.6,l=7.247757312],[x1=0.6666666666666666,x2=1.333333333333333,x3=2,x4=0,l=0],[x1=0.5714285714285714,x2=
# 1.142857142857143,x3=0,x4=2.285714285714286,l=0],[x1=1.333333333333333,x2=2.666666666666667,x3=0,x4=0,l=0],[x1=0.5,x2=0
# ,x3=1.5,x4=2,l=0],[x1=0,x2=0,x3=0,x4=4,l=0],[x1=0.8,x2=0,x3=0,x4=3.2,l=0],[x1=1,x2=0,x3=3,x4=0,l=0],[x1=0,x2
# =0,x3=4,x4=0,l=0],[x1=0,x2=4,x3=0,x4=0,l=0],[x1=4,x2=0,x3=0,x4=0,l=0]]"""
# s5 = """[x1=0.3333333333333333,x2=0.6666666666666666,x3=1,x4=1.333333333333333,x5=1.666666666666667,
# l=18.06409366232564],[x1=0.5,x2=1,x3=1.5,x4=2,x5=0,l=0],[x1=0.4545454545454545,x2=0.9090909090909091,x3=
# 1.363636363636364,x4=0,x5=2.272727272727273,l=0],[x1=0.8333333333333334,x2=1.666666666666667,x3=2.5,x4=0,x5=0,l=0],[x1=
# 0.4166666666666667,x2=0.8333333333333334,x3=0,x4=1.666666666666667,x5=2.083333333333333,l=0],[x1=0.625,x2=1.25,x3=0,x4=0
# ,x5=3.125,l=0],[x1=0.7142857142857143,x2=1.428571428571429,x3=0,x4=2.857142857142857,x5=0,l=0],[x1=1.666666666666667,x2
# =3.333333333333333,x3=0,x4=0,x5=0,l=0],[x1=0.3846153846153846,x2=0,x3=1.153846153846154,x4=1.538461538461539,x5=
# 1.923076923076923,l=0],[x1=0.5,x2=0,x3=0,x4=2,x5=2.5,l=0],[x1=0.5555555555555556,x2=0,x3=1.666666666666667,x4=0,x5=
# 2.777777777777778,l=0],[x1=0,x2=0,x3=0,x4=0,x5=5,l=0],[x1=0.8333333333333334,x2=0,x3=0,x4=0,x5=4.166666666666667,l=0
# ],[x1=0.625,x2=0,x3=1.875,x4=2.5,x5=0,l=0],[x1=1.25,x2=0,x3=3.75,x4=0,x5=0,l=0],[x1=1,x2=0,x3=0,x4=4,x5=0,l=0]
# ,[x1=0,x2=0,x3=0,x4=5,x5=0,l=0],[x1=0,x2=0,x3=5,x4=0,x5=0,l=0],[x1=0,x2=5,x3=0,x4=0,x5=0,l=0],[x1=5,x2=0,x3=
# 0,x4=0,x5=0,l=0]]"""
# s6 = """[x1=0.2857142857142857,x2=0.5714285714285714,x3=0.8571428571428571,x4=1.142857142857143,x5=1.428571428571429,x6
# =1.714285714285714,l=52.97370610571192],[x1=0.4,x2=0.8,x3=1.2,x4=1.6,x5=2,x6=0,l=0],[x1=0.375,x2=0.75,x3=1.125,x4=
# 1.5,x5=0,x6=2.25,l=0],[x1=0.6,x2=1.2,x3=1.8,x4=2.4,x5=0,x6=0,l=0],[x1=0.3529411764705883,x2=0.7058823529411765,x3=
# 1.058823529411765,x4=0,x5=1.764705882352941,x6=2.11764705882353,l=0],[x1=0.5,x2=1,x3=1.5,x4=0,x5=0,x6=3,l=0],[x1=
# 0.5454545454545454,x2=1.090909090909091,x3=1.636363636363636,x4=0,x5=2.727272727272727,x6=0,l=0],[x1=1,x2=2,x3=3,x4=0,
# x5=0,x6=0,l=0],[x1=0.3333333333333333,x2=0.6666666666666666,x3=0,x4=1.333333333333333,x5=1.666666666666667,x6=2,l=0],[
# x1=0.4285714285714285,x2=0.8571428571428571,x3=0,x4=0,x5=2.142857142857143,x6=2.571428571428572,l=0],[x1=
# 0.4615384615384616,x2=0.9230769230769231,x3=0,x4=1.846153846153846,x5=0,x6=2.769230769230769,l=0],[x1=0.6666666666666666,
# x2=1.333333333333333,x3=0,x4=0,x5=0,x6=4,l=0],[x1=0.5,x2=1,x3=0,x4=2,x5=2.5,x6=0,l=0],[x1=0.8571428571428571,x2=
# 1.714285714285714,x3=0,x4=3.428571428571428,x5=0,x6=0,l=0],[x1=0.75,x2=1.5,x3=0,x4=0,x5=3.75,x6=0,l=0],[x1=2,x2=4,
# x3=0,x4=0,x5=0,x6=0,l=0],[x1=0.3157894736842105,x2=0,x3=0.9473684210526315,x4=1.263157894736842,x5=1.578947368421053,x6
# =1.894736842105263,l=0],[x1=0.375,x2=0,x3=0,x4=1.5,x5=1.875,x6=2.25,l=0],[x1=0.4,x2=0,x3=1.2,x4=0,x5=2,x6=2.4,l=0
# ],[x1=0.5,x2=0,x3=0,x4=0,x5=2.5,x6=3,l=0],[x1=0.4285714285714285,x2=0,x3=1.285714285714286,x4=1.714285714285714,x5=0,
# x6=2.571428571428572,l=0],[x1=0.6,x2=0,x3=1.8,x4=0,x5=0,x6=3.6,l=0],[x1=0.5454545454545454,x2=0,x3=0,x4=
# 2.181818181818182,x5=0,x6=3.272727272727273,l=0],[x1=0,x2=0,x3=0,x4=0,x5=0,x6=6,l=0],[x1=0.8571428571428571,x2=0,x3=
# 0,x4=0,x5=0,x6=5.142857142857143,l=0],[x1=0.4615384615384616,x2=0,x3=1.384615384615385,x4=1.846153846153846,x5=
# 2.307692307692307,x6=0,l=0],[x1=0.75,x2=0,x3=2.25,x4=3,x5=0,x6=0,l=0],[x1=0.6666666666666666,x2=0,x3=2,x4=0,x5=
# 3.333333333333333,x6=0,l=0],[x1=1.5,x2=0,x3=4.5,x4=0,x5=0,x6=0,l=0],[x1=0.6,x2=0,x3=0,x4=2.4,x5=3,x6=0,l=0],[x1
# =1,x2=0,x3=0,x4=0,x5=5,x6=0,l=0],[x1=0,x2=0,x3=0,x4=0,x5=6,x6=0,l=0],[x1=1.2,x2=0,x3=0,x4=4.8,x5=0,x6=0,l=0]
# ,[x1=0,x2=0,x3=0,x4=6,x5=0,x6=0,l=0],[x1=0,x2=0,x3=6,x4=0,x5=0,x6=0,l=0],[x1=0,x2=6,x3=0,x4=0,x5=0,x6=0,l=0
# ],[x1=6,x2=0,x3=0,x4=0,x5=0,x6=0,l=0]]"""


def p(m):
    """Return [Pm] as indicated in the problem."""
    prod = 1.
    for n in range(1, m+1):
        prod *= (2*n / (m+1)) ** n
    return int(prod)


print(sum(p(m) for m in range(2, 16)))