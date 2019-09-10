#Modules
import os
import csv

#Variable
month = []
totalprofit=[]
mon_pro_cha=[]

# Set path for file
csvpath = os.path.join("..", "PyBank","Resources","budget_data.csv")

# Open the CSV File
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=",")
    csv_header = next(csvfile)
    #print(f"header {csv_header }")

    for row in csvreader:
        month.append(row[0])
        totalprofit.append(float(row[1]))
        
# Iterate through the profits in order to get the monthly change in profits

    for x in range(len(totalprofit)-1):
        mon_pro_cha.append(totalprofit[x+1]-totalprofit[x])

# Obtain the max and min of the the montly profit change list
        max_increase_profit = max(mon_pro_cha)
        max_decrease_profit = min(mon_pro_cha)

# Print on Terminal
    print ("Total number of Month: ", len(month) )
    print(f"Total: ${sum(totalprofit)}")
    print(f"Average Change: {round(sum(mon_pro_cha)/len(mon_pro_cha),2)}")
    print(f"Greatest Increase in Profits: $" + str(max_increase_profit))
    print(f"Greatest Decrease in Profits: $" + str(max_decrease_profit))

# Use write function to create and write to text file
output_path = os.path.join("..", "PyBank","Resources","PyBankText.txt")
with open(output_path, 'w', newline='') as file:
    file.write("Financial Analysis \n")
    file.write("------------------------- \n")
    file.write("Total Months:" + str(len(month)) + "\n")
    file.write(f"Total: ${sum(totalprofit)}" + "\n")
    file.write(f"Average Change: {round(sum(mon_pro_cha)/len(mon_pro_cha),2)}" + "\n")
    file.write(f"Greatest Increase in Profits: $" + str(max_increase_profit) + "\n")
    file.write(f"Greatest Decrease in Profits: $" + str(max_decrease_profit) + "\n")
    file.write("------------------------- ")