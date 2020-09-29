import os
import csv

dates = []
profit_loss = []

# import csv file and skip headers
with open('Resources/JamesWilliams_budget_data.csv') as csvpath:
    csv_reader = csv.reader(csvpath, delimiter=",")
    next(csv_reader, None)

    # add to predefined lists from csv columns
    for row in csv_reader:
        dates.append(row[0])
        profit_loss.append(row[1])

    # convert list of numbers to integers using map() method found on geeksforgeeks.com
    profit_loss = list(map(int, profit_loss))

    # total months and net total calculations
    total_months = len(dates) 
    total_profit_loss = sum(profit_loss)

    #create successive difference list from profit_loss list (borrowed from geeksforgeeks)
    monthly_change = [profit_loss[i + 1] - profit_loss[i] for i in range(len(profit_loss)-1)] 

    # average function from 03-Python/3/Stu_Functions class activity
    def average(numbers):
        length = len(numbers)
        total = 0
        for number in numbers:
            total += number
        return total / length

    #  calculate average change
    avg_monthly_change = round(average(monthly_change), 2)

    # calculate greatest increase in profits and losses
    max_increase = max(monthly_change)
    max_decrease = min(monthly_change)

    # get index position of greatest increase and decrease values
    max_increase_index = monthly_change.index(max_increase)
    max_decrease_index = monthly_change.index(max_decrease)

    #get the months these values occurred using index positions
    max_increase_month = dates[max_increase_index+1]
    max_decrease_month = dates[max_decrease_index+1]

    #print results and and export to text file 
    output = (
        "\nFinancial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit_loss}\n"
        f"Average  Change: ${avg_monthly_change}\n"
        f"Greatest Increase in Profits: {max_increase_month} $({max_increase})\n"
        f"Greatest Decrease in Profits: {max_decrease_month} $({max_decrease})\n")

    print(output)

    with open('Analysis/PyBank_Financial_Analysis.txt', 'w') as txt_file:
        txt_file.write(output)

