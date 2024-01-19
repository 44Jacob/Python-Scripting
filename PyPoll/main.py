# csv module for reading the data file.

import csv 
file_name = "Resources/election_data.csv"

#  read the data from election_data.csv

with open (file_name, mode = 'r') as file: 
    data = csv.DictReader(file)
#   Analyze the Data , The core of  task involves analyzing the data to compute: 
    
    candidates = {}
    total_votes = 0
    win_votes = 0

    for row in data:
        total_votes += 1

        candidate = row['Candidate']

        if candidate not in candidates.keys():
            candidates[candidate] = 0

        candidates[candidate] += 1

output = f"""
Election Results
-------------------------
Total Votes: {total_votes:,}
-------------------------
"""

for candidate in candidates.keys():
    votes = candidates[candidate]
    percentage = (votes / total_votes) * 100

    output += f"{candidate}: {percentage:.3f}% ({votes:,})\n"

    if votes > win_votes:
        win_votes = votes
        winner = candidate

output += f"-------------------------\nWinner: {winner}\n-------------------------"

print(output)

open('analysis/Election_Analysis.txt', mode='w').write(output)
