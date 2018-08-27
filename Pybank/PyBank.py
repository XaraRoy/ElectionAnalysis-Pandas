#Import CSV AND INIT
import csv 
import os




bank_csv = os.path.join(r"C:\Users\xanen\Documents\Homework\Module3_XAR\python-challenge\Resources\Budget_data.csv")
with open(bank_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    month_list = {'Month': [], 'Profit': []}
    next(csv_reader, None)
    for row in csv_reader:
       
        month = row[0]
        profit = row[1]
        month_list[month] = profit
    

#The total number of months included in the dataset

#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
    print(month_list)
