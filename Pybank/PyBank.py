#Import CSV AND INIT
import csv 
import os
import numpy as np




#declare path of Data
bank_csv = os.path.join("..\Resources\Budget_data.csv")
#open data file as CSV, splitting month-year and Profit
with open(bank_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#making a new dictionary to hold that info
    bank_dict = {}
#Skipping header 
    next(csv_reader, None)
#Filling Dictionary with Month as Key, profit as value
    for row in csv_reader:
        month = row[0]
        profit = int(row[1])
        bank_dict[month] = profit

#The total number of months included in the dataset
month_count = len(bank_dict)

#The total net amount of "Profit/Losses" over the entire period
NetProfit = sum(list(bank_dict.values()))

#The average change in "Profit/Losses" between months over the entire period

profit_change = []
x = 0
for value in bank_dict.values():
    if value != x:
        y = value
        profit_change.append(abs(x-y))
    x =value
profit_change.pop(0)
Delta_Avg = np.mean(profit_change)

 #The greatest increase in profits (date and amount) over the entire period
   
Greatest_increase_date =  max(bank_dict, key=bank_dict.get)
Greatest_increase_profit = bank_dict[Greatest_increase_date]

#The greatest decrease in losses (date and amount) over the entire period
Greatest_decrease_date =  min(bank_dict, key=bank_dict.get)
Greatest_decrease_profit = bank_dict[Greatest_decrease_date]

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

print(f"\n----------------------------\n")
print(f"Here is a list of the data\n{bank_dict}\n\n")
print(f"List of profit changes is,{profit_change}\n\n")
print(f"\n----------------------------\n")
print(f"\nFinancial Analysis\n")
print(f"{month_count} total monthly entries\n")
print(f"The net profit for this period was {NetProfit}\n")
print(f"The greatest increase in profit occured in  {Greatest_increase_date} with a profit of {Greatest_increase_profit}\n")
print(f"The greatest decrease in profit occured in  {Greatest_decrease_date} with a profit of {Greatest_decrease_profit}\n")
print(f"The Average profit change was {Delta_Avg}\n")


file=open("../Output/Pybank.txt", "w")

output = (
    f"\nFinancial Analysis\n"
    f"\n----------------------------\n"
    f'{month_count} total monthly entries\n'
    f'The net profit for this period was {NetProfit}\n'
    f'The greatest increase in profit occured in  {Greatest_increase_date} with a profit of {Greatest_increase_profit}\n'
    f'The greatest decrease in profit occured in  {Greatest_decrease_date} with a profit of {Greatest_decrease_profit}\n'
    f'The Average profit change was {Delta_Avg}'
    f"\n----------------------------\n"
)
file.write(output)
file.close()
