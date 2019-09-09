#Modules
import os
import csv

month = []
profit = []
loss = []
totalList=[]

sum=0
sum1=0
sum2=0

# Set path for file
csvpath = os.path.join("..", "PyBank","Resources","budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=",")
    csv_header = next(csvfile)
    print(f"header {csv_header }")
    for row in csvreader:
    
        month.append(row[0])

        totalList.append(float(row[1]))

        #print ("Month ::"+ row[0])
        #print("PROFIT/LOSS::"+row[1])
      
        if  float(row[1]) > 0: 
           profit.append(float (row[1]))
          # print("profit:"+row[1])
        else: 
            loss.append(float (row[1]))
        
    for num in totalList:
        sum = sum +num
    average  = sum / len(totalList)

    for pronum in profit:
        sum1 = sum1+pronum
    averageprofit = sum1 / len(profit)

    for losnum in loss:
        sum2 = sum2+losnum
    averageloss = sum2 / len(loss)

    print ("Average of profit: ", round(averageprofit,2) )
    print ("Average of loss: ", round(averageloss,2) )
    print ("Total $ : ", sum)
    print ("Average of list element is: ", round(average,2) )
    print ("Total number of Month: ", len(month) )