#Import CSV AND INIT

import os
from collections import Counter
import copy
import csv


candidates = []
counties_d = {}
counties = []
results = {}
totals = {}
Winner_Votes = 0
    


#declare path of Data
poll_csv = os.path.join("..\Resources\election_data.csv")
# Importing Files
with open(poll_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
#Making Lists from dataset
    for row in csv_reader:
       counties.append(row[1])
       candidates.append(row[2])
       counties_d.setdefault(row[1], 0)


totals_d = {"Total Votes" : 0, "Percentage Won" : 0}           
counties_d.update(totals_d)  

zipped =  zip(candidates, counties)

#Count the votes
counted = Counter(zipped)
for (x, y) in sorted(counted):
    if not x in results.keys():          
        results[x] = copy.deepcopy(counties_d)
    results[x][y] = counted[x, y]

#Find the Winners
for x in results.keys():
    results[x]["Total Votes"] = sum(results[x].values())
    results[x]["Percentage Won"] = results[x]["Total Votes"] / len(counties) * 100
    if results[x]['Total Votes'] > Winner_Votes:
        Winner_Votes = results[x]["Total Votes"]
        Winner_Percent = results[x]["Percentage Won"]
        Winner = x
    totals[x] = results[x]["Total Votes"]

#The total number of votes cast
#A complete list of candidates who received votes
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#print the analysis to the terminal and export a text file with the results.
print(f"\n----------------------------")
print(f"Here is a Summary of the Election")
print(f"----------------------------\n\n")
print(f"The Winner is {Winner} with {Winner_Votes}  Votes or {'{:04.2f}'.format(Winner_Percent)}% of {len(counties)} total votes!\n\n")
print(f"\n----------------------------\n")
print(f"Electoral Analysis\n")
print(f"----------------------------\n\n")
for c in counties_d.keys():
    if c == 'Total Votes':
        break
    County_Votes = 0
    County_Total = 0
  
    print(f"Voting summary {c} county.\n\n")
    for n in results.keys():
        County_Total += results[n][c]
        print(f" {n} had {results[n][c]} votes")
        if results[n][c] > County_Votes:
           County_Votes = results[n][c]
           County_Percent = County_Votes / County_Total * 100
           County_winner = n
        
        
    print(f"\n\nThere were {County_Total} votes in {c} county this year")
    print(f"The winner of {c} county is {County_winner} with {County_Votes} votes or {'{:04.2f}'.format(County_Percent)}%\n")
    print(f"----------------------------\n\n")

file=open("../Output/PyPoll.txt", "w")
output = (
f"\n----------------------------"
f"Here is a Summary of the Election"
f"----------------------------\n\n"
f"The Winner is {Winner} with {Winner_Votes}  Votes or {'{:04.2f}'.format(Winner_Percent)}% of {len(counties)} total votes!\n\n"
f"\n----------------------------\n"
f"Electoral Analysis\n"
f"----------------------------\n\n"
)
file.write(output)
for c in counties_d.keys():
    if c == 'Total Votes':
        break
    County_Votes = 0
    County_Total = 0
  
    output = ( f"Voting summary {c} county.\n\n")
    file.write(output)
    
    for n in results.keys():
        County_Total += results[n][c]
        
        output =(f" {n} had {results[n][c]} votes\n")
        file.write(output)
        
        if results[n][c] > County_Votes:
           County_Votes = results[n][c]
           County_Percent = County_Votes / County_Total * 100
           County_winner = n
        
    output = (    
    f"\n\nThere were {County_Total} votes in {c} county this year\n"
    f"The winner of {c} county is {County_winner} with {County_Votes} votes or {'{:04.2f}'.format(County_Percent)}%\n"
    f"----------------------------\n\n")
    file.write(output)

file.close()