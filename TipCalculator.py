# -*- coding: utf-8 -*-
pound = u'\u00A3'

print("Welcome to the tip calculator!\n")
totalBill = input(f"What was the total bill? {pound}")
tipPercent = input("What percentage tip would you like to give? ")
totalPeople = input("How many people to split the bill? ")
maths = (float(totalBill) / float(totalPeople)) * ((float(tipPercent)/100)+1)
tip = "{:.2f}".format(maths)

print(f"\nEach person should pay: {pound}{tip}")