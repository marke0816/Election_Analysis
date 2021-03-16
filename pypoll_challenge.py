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

#Initialize list of counties
county_list = []

#Initialize dictionary to hold votes by county
county_votes = {}

#Winning candidate (county) and winning count tracker
winning_candidate = ''
winning_county = ''
winning_count = 0
winning_county_count = 0
winning_percentage = 0
winning_county_percentage = 0

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

#Get candidate names and county names
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:

#Add candidate names to the candidate list            
            candidate_options.append(candidate_name)

#Track that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        if county_name not in county_list:

#Add county names to the county list
            county_list.append(county_name)

#Track votes from that county
            county_votes[county_name] = 0
        
        candidate_votes[candidate_name] += 1
        county_votes[county_name] += 1

#Write the results to a .txt file
with open(file_to_save, 'w') as txt_file:
    election_results = (
        f'\nElection Results\n'
        f'--------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'--------------------\n'
    )
    # print(election_results, end='')
    txt_file.write(election_results)
    
    print(election_results, end='')

    #print county data    
    print(f'County Votes:\n'
    f'-------------\n')
    txt_file.write(f'County Votes:\n'
    f'-------------\n')

    for county_name in county_votes:

        votes_by_county = county_votes[county_name]

        vote_percentage_by_county = float(votes_by_county) / float(total_votes) * 100

        county_results = (f'{county_name}: {vote_percentage_by_county:.2f}% ({votes_by_county:,})\n')

        print(county_results)
        txt_file.write(county_results)

        if (votes_by_county > winning_county_count) and (vote_percentage_by_county > winning_county_percentage):

                    winning_county_count = votes_by_county

                    winning_county_percentage = vote_percentage_by_county

                    winning_county = county_name

    winning_county_summary = (
        f'--------------------------\n'
        f'Largest County Turnout: {winning_county}\n'
        f'--------------------------\n'
    )

    txt_file.write(winning_county_summary)
    
    #print candidate data
    print(f'---------------\n'
        f'Candidate Votes\n'
        f'---------------\n')

    for candidate_name in candidate_votes:

        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        #Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f'{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n')

        print(candidate_results)

        txt_file.write(candidate_results)

        #Determine the wining vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f'--------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.2f}%\n'
        f'--------------------------\n'
    )
    
    print(winning_county_summary)
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    

# print(county_list)
# print(county_votes)