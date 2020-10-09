#!/usr/bin/env python3
C = -50
print("Celsius Fahrenheit")
while C <= 50:
    F = 1.8 * C + 32
    print("{:5d} {:7.2f}".format(C,F))
    C +=1


