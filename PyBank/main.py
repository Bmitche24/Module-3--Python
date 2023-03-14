import os
import csv

# Path for file
filepath = '/Users/breannamitchell/Desktop/python-challenge/PyBank/Resources/budget_data.csv'

# Create lists to store the data
months = []
profits = []

# Running through CSV
with open(filepath) as csvf:
    reader = csv.reader(csvf, delimiter=',')
    header = next(reader)  # skip header row
    for row in reader:
        months.append(row[0])
        profits.append(int(row[1]))

# The total number of months and total profit
total_months = len(months)
total_profit = sum(profits)

# Calculate the change in profits 
profit_change = [profits[i+1] - profits[i] for i in range(len(profits)-1)]

# Average change in profit
avg_change = sum(profit_change) / len(profit_change)

# Using Index
profit_inc = profit_change.index(max(profit_change))
profit_dec = profit_change.index(min(profit_change))

# Results in Terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {months[profit_inc+1]} (${max(profit_change)})")
print(f"Greatest Decrease in Profits: {months[profit_dec+1]} (${min(profit_change)})")

# Text.File
with open('output.txt', 'w') as text_file:
    print("Financial Analysis", file=text_file)
    print("------------------------", file=text_file)
    print(f"Total Months: {total_months}", file=text_file)
    print(f"Total: ${total_profit}", file=text_file)
    print(f"Average Change: ${avg_change:.2f}", file=text_file)
    print(f"Greatest Increase in Profits: {months[profit_inc+1]} (${max(profit_change)})", file=text_file)
    print(f"Greatest Decrease in Profits: {months[profit_dec+1]} (${min(profit_change)})", file=text_file)