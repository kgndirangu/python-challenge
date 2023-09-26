import os
import csv

#path to collect data from Resources folder
bank = os.path.join('..', 'Resources', 'budget_data.csv') 

# Read in the CSV file
with open(bank, 'r') as csvfile:
       

    # Scdplit the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #code doesn't run if header is not skipped, however 2 removes the header and first row of data
    # leading to underestimate in total amount  
    header = next(csvreader)
    
    #remove first row from amount change calculation
    previous_row = next(csvreader)
    previous_value = int(previous_row[1])
        
#List to store data
    
    month_list = []
    amount_list = []
    change_list = []

    #start at month 1 since we removed first row
    total_month = 1
     
        
    for row in csvreader:
        total_month = total_month + 1
        
        month_list.append(row[0])
        #total amount calculation, append to store in amount list; convert to integer 
        amount_list.append(int(row[1])) 
        #The changes in profit/losses over the entire period, and then the average of those changes 
        change = int(row[1]) - previous_value
        #after calculation reset previous value
        previous_value = int(row[1])
        #store change in list
        change_list.append(change)
        
        
        
        
#first row = 1088983 is missing from total_amount, please advise    
total_amount = sum(amount_list)
avg_change = sum(change_list)/len(change_list)
greatest = max(change_list)
least = min(change_list)
#greatest increase and month
month_g = change_list.index(max(change_list))
#index 78 based on previous line output
month_g2 = month_list[78]
#greatest decrease and month
month_l = change_list.index(min(change_list))
#index 48 based on previous line output
month_l2 = month_list[48]



output = (
        f"Financial Analysis\n"
        f"Total Months: {total_month}\n"
        f"Total: ${total_amount}\n"
        f"Average Change: ${avg_change}\n"
        f"Greatest Increase in Profits: {month_g2} (${greatest})\n"
        f"Greatest Decrease in Profits: {month_l2} (${least})"
    )

print(output)