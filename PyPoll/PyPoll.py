#Import CSV AND INIT

import os
from collections import Counter
import csv

#declare path of Data
poll_csv = os.path.join("..\Resources\election_data.csv")

# Importing Files
with open(poll_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#Skipping header 
    next(csv_reader, None)

    counties_d = {}
    counties = []
    candidates = []
    candidates_d = {}
    
#Making Lists from dataset
    for row in csv_reader:
       counties.append(row[1])
       candidates.append(row[2])
       counties_d.setdefault(row[1], 0)
       candidates_d.setdefault(row[2],counties_d)

      
zipped = zip(candidates, counties)
c = Counter(zipped)
for i in candidates_d.keys():
    for n in counties_d.keys():
        x = c[i, n]
        counties_d[n] = x
    candidates_d[i] = counties_d
    counties_d.clear
    
    # candidates_d[canidates] = {counties_d[val2], count}

    



        
        
       

               
    

    # Results_Dict= {
    #     Canidate1 : { County 1 : Vote_count, County 2: Vote Count ...
    #     Canidate2 : { County 1 : Vote_count, County 2: Vote Count ...
    #     }
    # }




    print(candidates_d)
    print(len(counties))

    
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#print the analysis to the terminal and export a text file with the results.
