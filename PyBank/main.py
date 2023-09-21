import os
import csv

#path to collect data from Resources folder
bank = os.path.join('..', 'Resources', 'budget_data.csv') 

# Read in the CSV file
with open(bank, 'r') as csvfile:

    # Scdplit the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
#List to store data
    month_list = []
    amount_list = []

    total_amount = 0
    total_month = 0

    
    
    # Loop through the data
    for row in csvreader:
        
        #month_count = 

        #append to store in amount list; convert to integer 
            amount_list.append(int(row[1]))
            month_list.append(row[0])
    total_amount = sum(amount_list)
    print(total_amount)
    total_month = len(month_list)
    print(total_month)