#!/usr/bin/env python3
sum = 0
N = 10
count = 1
print("Please Input 10 Numbers:")
while count <= N:
    number = float(input())
    sum += number
    count += 1
average = sum / N
print("N = {},Sum = {}".format(N,sum))
print("average = {:.2f}".format(average))
