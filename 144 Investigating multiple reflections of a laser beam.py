"""https://projecteuler.net/problem=144

Throughout the solution, I assume that the light beam is never perfectly vertical, and it indeed seems to be the case."""
from math import sqrt


points = [(0,10.1), (1.4,-9.6)]  # points encountered on the wall
slopes = [-14.0714]  # slopes of each trajectory

while not (-0.01 <= points[-1][0] <= 0.01 and points[-1][1] > 0):
    x1 = points[-1][0]
    y1 = points[-1][1]
    m1 = slopes[-1]  # slope of previous line
    mp = y1 / (4 * x1)  # slope of perpendicular to point where prev line intersects ellipse

    # slope of next line (formula obtained from http://stackoverflow.com/questions/17395860/how-to-reflect-a-line-over-another-line)
    m2 = (2*mp + m1*mp**2 - m1) / (2*mp*m1 - mp**2 + 1)

    # Compute the two candidate points for the next point of intersection. These formulas were obtained from using
    # Wolfram Alpha to solve the system 4x2^2+y^2=100 and y-y1=m2(x-x1).
    x2_1 = (-2*sqrt(-m2**2*x1**2 + 25*m2**2 + 2*m2*x1*y1 - y1**2 + 100) + m2**2*x1 - m2*y1) / (m2**2 + 4)
    y2_1 = -2*(m2*sqrt(-m2**2*x1**2 + 25*m2**2 + 2*m2*x1*y1 - y1**2 + 100) + 2*m2*x1 - 2*y1) / (m2**2 + 4)
    x2_2 = (2*sqrt(-m2**2*x1**2 + 25*m2**2 + 2*m2*x1*y1 - y1**2 + 100) + m2**2*x1 - m2*y1) / (m2**2 + 4)
    y2_2 = -2*(-m2*sqrt(-m2**2*x1**2 + 25*m2**2 + 2*m2*x1*y1 - y1**2 + 100) + 2*m2*x1 - 2*y1) / (m2**2 + 4)

    # One candidate will always be the previous point of intersection, so choose the other candidate as the next point
    # of intersection.
    if abs(x1-x2_1) < 0.0001 and abs(y1-y2_1) < 0.0001:
        points.append((x2_2,y2_2))
    else:
        points.append((x2_1,y2_1))
    slopes.append(m2)

print(len(slopes)-1)
