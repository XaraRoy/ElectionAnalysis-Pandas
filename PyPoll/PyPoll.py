#Import CSV AND INIT

import os
import numpy as np
import csv

#declare path of Data
poll_csv = os.path.join("..\Resources\election_data.csv")

# Importing Files
with open(poll_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#Skipping header 
    next(csv_reader, None)

    voters = []
    counties = []
    candidates = []

#Filling Dictionary with Month as Key, Profit/Losses as value
    for row in csv_reader:
       voters.append(row[0])
       counties.append(row[1])
       candidates.append(row[2])
            
print(len(voters))
print(len(counties))
print(len(candidates))
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#print the analysis to the terminal and export a text file with the results.
