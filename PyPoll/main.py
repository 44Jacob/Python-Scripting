# csv module for reading the data file.

import csv 
file_name = "election_data.csv"

#  read the data from election_data.csv

with open (file_name, mode = 'r') as file: 
    csvreader = csv.DirectReader(file)
    data = list(csvreader)

#   Analyze the Data , The core of  task involves analyzing the data to compute: 
    
    vote_counts = {}

for row in data:
    candidate = row['Candidate']
    if candidate in vote_counts:
        vote_counts[candidate] += 1
    else:
        vote_counts[candidate] = 1

total_votes = sum(vote_counts.values())

#Calculate Percentages and Determine Winner
#For each candidate, calculate the percentage of votes they received. Also, identify the candidate with the most votes.

winner = None
max_votes = 0

for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print and Save the Results to the terminal and save them to a text file.
        
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += f"-------------------------\nWinner: {winner}\n-------------------------"

print(output)

with open('election_results.txt', mode='w') as file:
    file.write(output)
