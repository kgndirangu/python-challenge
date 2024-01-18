import os
import csv

#path to collect data from Resources folder
election_data = os.path.join('Resources', 'election_data.csv') 

candidates_list = []
candidates_votes = {}
# Read in the CSV file
with open(election_data, 'r') as csvfile:
       

    # Scdplit the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    total_votes = 0
  
    for row in csvreader: 
        
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidates_list: 
            candidates_list.append(candidate_name)
            candidates_votes[candidate_name] = 0
        candidates_votes[candidate_name] += 1
        
      
percentages = {key: round(val / total_votes*100,3) for key,val in candidates_votes.items()}
winning_candidate = max(candidates_votes, key=candidates_votes.get)

output_file = os.path.join('analysis', 'election_analysis.txt') 


with open(output_file, 'w') as txtfile:
    

    output1 = (
            f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n")
    print(output1)
    txtfile.write(output1)


        
    for k,v in candidates_votes.items():
        output2 = f"{k}: {percentages[k]}% ({v})\n"
        print(output2)
        txtfile.write(output2)



    output3 = ( f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"-------------------------"
                )
    print(output3)
    txtfile.write(output3)
