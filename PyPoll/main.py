import os
import csv

#Path for file
filepath = '/Users/breannamitchell/Desktop/python-challenge/PyPoll/Resources/election_data.csv'

#Starting count at 0
totalvotes = 0 

#Empty location for values
won_candidate_votes = {}

# Retrieve Data
with open(filepath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    
#Iterate through rows
    for row in reader:
        totalvotes += 1
        won_candidate_votes[row[2]] = won_candidate_votes.get(row[2], 0) + 1  
        

#Results in terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalvotes))
print("-------------------------")

for candidate, votes in won_candidate_votes.items():
    print(f"{candidate}: {votes/totalvotes:.3%} ({votes})")
    print("-------------------------") 

winner = max(won_candidate_votes, key=won_candidate_votes.get)
print(f"Winner: {winner}")

#Text file
filepath = os.path.join('.', 'output.txt')
with open(filepath, "w") as text_file:   
    print('Election Results', file=text_file)
    print("-------------------------", file=text_file)
    print("Total Votes: " + str(totalvotes), file=text_file)
    print("-------------------------", file=text_file)
    

    for candidate, votes in won_candidate_votes.items():
        print(f"{candidate}: {votes/totalvotes:.3%} ({votes})", file=text_file)
        print("-------------------------", file=text_file) 
        
    print(f'Winner: {winner}', file=text_file)
