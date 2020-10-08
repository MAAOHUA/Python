#!/usr/bin/env python3
amount = float(input("enter amount:")) 
inrate = float(input("enter inrate:"))
period = int(input("enter period:"))
value = 0
year = 1
while year <= period:
    value = amount + (inrate*amount)
    print("Year{} Total  {:.2f}".format(year,value))
    amount = value
    year += 1
