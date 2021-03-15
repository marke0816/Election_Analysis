# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#Initialize accumulator variable
total_votes = 0

#Initialize candidate names
candidate_options = []

#Initialize candidate votes
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

#To do: perform analysis
#Read the file object with the reader function
    file_reader = csv.reader(election_data)

# Print each row in the CSV file
#     for row in file_reader:
#         print(row)

#Print the header row
    headers = next(file_reader)

#Loop through all rows in file    
    for row in file_reader:

#Tally up total votes
        total_votes += 1

#Get candidate names
        candidate_name = row[2]

        if candidate_name not in candidate_options:

#Add candidate names to the candidate list            
            candidate_options.append(candidate_name)

#Track that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1


for candidate_name in candidate_votes:

    #Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    #Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #Determine the wining vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name


    print(f'{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n')

winning_candidate_summary = (
    f'--------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.2f}%\n'
    f'--------------------------\n'
)
print(winning_candidate_summary)

#Using the with statement, open the file as a text file
with open(file_to_save, 'w') as txt_file:
    txt_file.write(winning_candidate_summary)
