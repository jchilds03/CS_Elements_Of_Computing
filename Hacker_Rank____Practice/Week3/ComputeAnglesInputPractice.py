"""Given three vertices of a triangle, compute and
display the three sides and three angles"""

import math
#Our three vertices are (x1,y1), (x2,y2) and (x3,y3)
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

# This computes the lengths of the three sides:
a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# This prints the three sides:
print("The three sides have lengths: ", round(a,2), \
    round(b,2), round(c,2))

# This computes the three angles:
A = math.degrees(math.acos((a**2 - b**2 - c**2) / (-2*b*c)))
B = math.degrees(math.acos((b**2 - a**2 - c**2) / (-2*a*c)))
C = math.degrees(math.acos((c**2 - b**2 - a**2) / (-2*a*b)))

# This prints the thtree angles:
print("The three angles are ", round(A*100) / 100.0, \
    round(B*100) / 100.0, round(C*100) / 100.0)