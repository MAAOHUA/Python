#!/usr/bin/env python3
F = 0
print("Fahrenheit Celsius")
while F <= 250:
    C = (F-32) / 1.8
    print("{:5d} {:7.2f}".format(F,C))
    F += 25

