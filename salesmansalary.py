#!/usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
numberofcamera = int(input("Enter the number of camera:"))
price = float(input("Enter the price of camera:"))
bonus = (bonus_rate * numberofcamera)
commission = (commission_rate * price * numberofcamera)
print("Bonus      = {:6.2f}".format(bonus))
print("commission = {:6.2f}".format(commission))
print("Gross salary= {:6.2f}".format(bonus + commission + basic_salary))
