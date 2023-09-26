import os
import csv

#path to collect data from Resources folder
election_data = os.path.join('..', 'Resources', 'election_data.csv') 


# Read in the CSV file
with open(election_data, 'r') as csvfile:
       

    # Scdplit the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
#code doesn't run if header skip is left out 
    header = next(csvreader)
    
    total_votes = 0
    vote_c = 0
    vote_d = 0
    vote_r = 0
    #create dictionary to hold candidate names
    candidates = {}
    for i in csvreader: 
        total_votes = total_votes + 1
        #WHY SET TO 0?
        candidates[i[2]] = 0

        if i[2]== "Charles Casper Stockham":
            vote_c = vote_c +1
        elif i[2] == "Diana DeGette": 
            vote_d = vote_d + 1
        else:
            vote_r = vote_r +1
perc_c = (vote_c/total_votes)*100 
perc_d = (vote_d/total_votes)*100 
perc_r = (vote_r/total_votes)*100 

print(total_votes) 
candidate_names = candidates.keys()
print(candidate_names)
print(vote_c)
print(vote_d)
print(vote_r)
print(perc_c)
print(perc_d)
print(perc_r)
#round percentage
print(f"Charles Casper Stockham: {str(perc_c)}, {str(vote_c)}")

#this returns 3
#candidate_votes = len(candidates.keys())
#print(candidate_votes)