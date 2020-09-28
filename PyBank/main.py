import os
import csv

dates = []
profit_loss = []

# import csv file and skip headers
with open('/Users/jameswilliams/Desktop/GT_Data_Boot_Camp/GT_Homework/python-challenge/PyBank/Resources/JamesWilliams_budget_data.csv') as csvpath:
    csv_reader = csv.reader(csvpath, delimiter=",")
    next(csv_reader, None)

    # add to predefined lists from csv columns
    for row in csv_reader:
        dates.append(row[0])
        profit_loss.append(row[1])
    # convert list of numbers to integers using map() method found on geeksforgeeks.com
    profit_loss = list(map(int, profit_loss))

    # calculations
    total_months = len(dates) 
    total_profit_loss = sum(profit_loss)
    avg_profit_loss = 
   
print(total_months)
   