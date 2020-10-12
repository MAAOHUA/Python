#!/usr/bin/env python3
import math
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
d = b*b - 4*a*c
if d < 0:
    print("ROOTS are imaginary")
else:
    root1 =float((-b + math.sqrt(d)) / (2 * a))
    root2 = float((-b - math.sqrt(d)) / (2 * a))
    print("Root1={} Root2={}".format(root1,root2))

