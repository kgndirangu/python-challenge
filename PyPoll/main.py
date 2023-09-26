import os
import csv

#path to collect data from Resources folder
election_data = os.path.join('..', 'Resources', 'election_data.csv') 


# Read in the CSV file
with open(election_data, 'r') as csvfile:
       

    # Scdplit the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    total_votes = 0
    vote_c = 0
    vote_d = 0
    vote_r = 0
    #plan was to create 2 dictionaries. One with the 3 candidates and percentage votes recieved, 
    # the other with the 3 candidates and total votes, however was unable to write syntax so I solved the 
    #challenge in a roundabout way 
    
    for row in csvreader: 
        
        total_votes = total_votes + 1
        
        if row[2]== "Charles Casper Stockham":
            vote_c = vote_c +1
        elif row[2] == "Diana DeGette": 
            vote_d = vote_d + 1
        else:
            vote_r = vote_r +1


perc_c = (vote_c/total_votes)*100 
perc_d = (vote_d/total_votes)*100 
perc_r = (vote_r/total_votes)*100 

output = (
        f"Election Results\n"
        f"Total Votes: {total_votes}\n"
        f"Charles Casper Stockham: {str(perc_c)}%, ({str(vote_c)})\n"
        f"Diane DeGette: {str(perc_d)}%, ({str(vote_d)})\n"
        f"Raymon Anthony Doane: {str(perc_r)}%, ({str(vote_r)})"
            )

print(output)

#unable to print winner because did not successfully manipulate dictionary to find percentage vote each candidate received