#Modules
import os
import csv

#Variable
# voterid = []
# county = []
# candidate = []
total_vote=0
khan_vote=0
correy_vote=0
li_vote=0
otooley_vote=0

# Set path for file
csvpath = os.path.join("..", "PyPoll","Resources","election_data.csv")

# Open the CSV File
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=",")
    csv_header = next(csvfile)
    print(f"header {csv_header }")

    for row in csvreader:
        # voterid.append(row[0])
        # county.append(row[1])
        # candidate.append(row[2])
        total_vote +=1
        if row[2] == "Khan": 
            khan_vote += 1
        elif row[2] == "Correy":
            correy_vote +=1
        elif row[2] == "Li": 
            li_vote +=1
        elif row[2] == "O'Tooley":
            otooley_vote +=1

# % Calcualtions
khan_percent = (khan_vote/total_vote) *100
correy_percent = (correy_vote/total_vote) * 100
li_percent = (li_vote/total_vote)* 100
otooley_percent = (otooley_vote/total_vote) * 100

# # Print Vote + Vote % on Terminal
print(f"Total Vote: ", total_vote )
print(f"Khan Votes: ", khan_vote )
print(f"Correy Votes:", correy_vote )
print(f"Li Votes:", li_vote )
print(f"O'Tooley Votes:", otooley_vote )

print(f"Khan % Votes: ", khan_percent )
print(f"Correy % Votes:", correy_percent )
print(f"Li % Votes", li_percent )
print(f"O' % Votes:", otooley_percent )


# # Use write function to create and write to text file
# output_path = os.path.join("..", "PyPoll","Resources","PyPollText.txt")
# with open(output_path, 'w', newline='') as file:
#     file.write("Financial Analysis \n")
#     file.write("------------------------- \n")
#     file.write("Total Months:" + str(len(month)) + "\n")
#     file.write(f"Total: ${sum(totalprofit)}" + "\n")
#     file.write(f"Average Change: {round(sum(mon_pro_cha)/len(mon_pro_cha),2)}" + "\n")
#     file.write(f"Greatest Increase in Profits: $" + str(max_increase_profit) + "\n")
#     file.write(f"Greatest Decrease in Profits: $" + str(max_decrease_profit) + "\n")
#     file.write("------------------------- ")