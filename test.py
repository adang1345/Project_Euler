"""https://projecteuler.net/problem=183"""

import math
import sympy


def is_nonterminating(n):
    """Return whether the maximum product of parts of n is nonterminating."""
    num_parts = int(round(n / math.e))
    num_parts //= math.gcd(num_parts, n)
    facs = sympy.factorint(num_parts)
    for x in facs:
        if x != 2 and x != 5:
            return True
    return False


d = 0
for n in range(5, 101):
    print(n, is_nonterminating(n))
    if is_nonterminating(n):
        d += n
    else:
        d -= n
print(d)


"""5 False
6 False
7 True
8 True
9 False
10 False
11 False
12 False
13 False
14 False
15 False
16 True
17 True
18 True
19 True
20 True
21 False
22 False
23 False
24 True
25 True
26 False
27 False
28 False
29 True
30 True
31 True
32 True
33 False
34 True
35 True
36 True
37 True
38 True
39 True
40 True
41 True
42 False
43 False
44 False
45 True
46 True
47 True
48 True
49 True
50 True
51 True
52 True
53 True
54 False
55 False
56 True
57 True
58 True
59 True
60 True
61 True
62 True
63 True
64 True
65 True
66 False
67 False
68 False
69 False
70 True
71 True
72 True
73 True
74 True
75 True
76 True
77 False
78 True
79 True
80 True
81 False
82 True
83 True
84 True
85 True
86 False
87 False
88 False
89 True
90 True
91 True
92 True
93 True
94 True
95 True
96 True
97 True
98 True
99 False
100 True
2438"""