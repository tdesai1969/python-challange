# load dependecies 
import os
import csv

total_vote=0
khan_vote=0
correy_vote=0
li_vote=0
otooley_vote=0
Khan = "Khan"
Correy = "Correy"
Li = "Li"
OTooley = "OTooley"
winner =""

# Set path for file
csvpath = os.path.join("..", "PyPoll","Resources","election_data.csv")

# Open the CSV File
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=",")
    csv_header = next(csvfile)
    #print(f"header {csv_header }")

    for row in csvreader:
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

# Find Higest Vote Candidate and print
higestvote=max(khan_vote,correy_vote,li_vote,otooley_vote)
if higestvote == khan_vote:
    print("Winner:", Khan)
    winner = Khan
if higestvote == correy_vote:
    print("Winner:", Correy)
    winner = Correy
if higestvote == li_vote:
    print("Winner:", Li)
    winner = Li
if higestvote == otooley_vote:
    print("Winner:", OTooley)
    winner = OTooley

# # Print Vote % + vote on Terminal
print(f"Total Vote: ", total_vote )
print(f"Khan :", round(khan_percent,2),"%", str(khan_vote))
print(f"Correy :", round(correy_percent,2),"%", str(correy_vote))
print(f"Li :", round(li_percent,2),"%", str(li_vote))
print(f"O'Tooley :", round(otooley_percent,2),"%", str(otooley_vote))

# # Use write function to create and write to text file

output_path = os.path.join("..", "PyPoll","Resources","PyPollText.txt")
with open(output_path, 'w', newline='') as file:
    file.write("Election Results\n")
    file.write("------------------------- \n")
    file.write(f"Total Votes: {total_vote}" + "\n")
    file.write("------------------------- \n")
    file.write(f"Khan: {khan_percent:.2f}% ({khan_vote})" + "\n")
    file.write(f"Correy: {correy_percent:.2f}% ({correy_vote})" + "\n")
    file.write(f"Li: {li_percent:.2f}% ({li_vote})" + "\n")
    file.write(f"O'Tooley: {otooley_percent:.2f}% ({otooley_vote})" + "\n")
    file.write("------------------------- \n")
    file.write("Winner:" + winner + "\n")
    file.write("------------------------- ")