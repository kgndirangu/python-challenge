import os
import csv

#path to collect data from Resources folder
bank = os.path.join('Resources', 'budget_data.csv') 

# Read in the CSV file
with open(bank, 'r') as csvfile:
       

    # Scdplit the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #remove first row from amount change calculation
    previous_row = next(csvreader)
    previous_value = int(previous_row[1])
      
#List to store data
    
    month_list = []
    amount_list = []
    change_list = []

    max_increase = 0
    max_decrease = 10000000000
    max_inc_month = ""
    max_dec_month = ""


    #start at month 1 since we removed first row
    total_month = 1
    amount_list.append(int(previous_row[1]))   
        
    for row in csvreader:
        total_month = total_month + 1
        
        month_list.append(row[0])
        #total amount calculation, append to store in amount list; convert to integer 
        amount_list.append(int(row[1])) 

        #The changes in profit/losses over the entire period, and then the average of those changes 
        change = int(row[1]) - previous_value
        if max_increase < change:
            max_increase= change
            max_inc_month = row[0]
        if max_decrease > change:
            max_decrease= change
            max_dec_month = row[0]
        #after calculation reset previous value
        previous_value = int(row[1])
        #store change in list
        change_list.append(change)
        

       
   
total_amount = sum(amount_list)
avg_change = round(sum(change_list)/len(change_list), 2)



output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_month}\n"
        f"Total: ${total_amount}\n"
        f"Average Change: ${avg_change}\n"
        f"Greatest Increase in Profits: {max_inc_month} (${max_increase})\n"
        f"Greatest Decrease in Profits: {max_dec_month} (${max_decrease})"
    )

print(output)
output_file = os.path.join('analysis', 'budget_analysis.txt') 

# Read in the CSV file
with open(output_file, 'w') as txtfile:
    txtfile.write(output)
       