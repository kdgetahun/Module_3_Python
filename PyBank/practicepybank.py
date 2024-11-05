# Dependencies
import csv
import os   # os allows for path manipulation across operating systems
 
# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "kidbudget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "kidbudget_analysis.txt")  # Output file path
 
# Define variables to track the financial data
total_months = 0
total_net = 0     # this shows the total net or profit/losses
net_change_list = []
months = []  
 
# Open and read the csv
with open(file_to_load) as kidbudget_data:   # this is opening the file to load path budget data
    csvreader = csv.reader(kidbudget_data)    # csv reader is set up
    # read the header row
    header = next(csvreader)   # this is the Date/Net row
    # move to the first row
    firstRow = next(csvreader)    #calling "next" will skip the header row 
    total_months = total_months + 1
    total_net += int(firstRow[1])    # net is in index 1      
 
    #establish previous net
    previousNet = int(firstRow[1])  # Changed to int from float
 
    # Process each row of data
    for row in csvreader:            # start of loop
        # Track the total and net change
        total_months = total_months + 1
        total_net += int(row[1])    # net is in index 1
 
        netChange = int(row[1]) - previousNet   # Changed to int from float
        net_change_list.append(netChange)
        months.append(row[0])  # add the first month that the change occurred
 
        #update the previous revenue
        previousNet = int(row[1])  # Changed to int from float
 
#Calculate the average net change per month
averageChangePerMonth = sum(net_change_list) / len(net_change_list)
 
greatest_increase = [months[0], net_change_list[0]]
greatest_decrease = [months[0], net_change_list[0]]
 
for m in range(len(net_change_list)):
    # Calculate the greatest increase in profits (month and amount)   
    if(net_change_list[m] > greatest_increase[1]):
        greatest_increase[1] = int(net_change_list[m])  # Ensure it's an integer
        greatest_increase[0] = months[m]
 
    # Calculate the greatest decrease in losses (month and amount)
    if(net_change_list[m] < greatest_decrease[1]):
        greatest_decrease[1] = int(net_change_list[m])  # Ensure it's an integer
        greatest_decrease[0] = months[m]  
 
# Generate the output summary
output = (
    f"\nFinancial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net:,}\n"
    f"Average Change: ${averageChangePerMonth:,.2f}\n"
    f"Greatest increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,})\n"
)
 
# Print the output
print(output)
 
# Write the results to a text file
with open(file_to_output, "w") as txt_file:    #"w" means write mode
    txt_file.write(output)           # this is writing the output of the variables
