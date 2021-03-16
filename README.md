# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local congressional election.

    1. Calculate the total number of votes cast for each candidate and from each of the three counties.
    2. Get a complete list of candidates who received votes and which counties those votes came from.
    3. Calculate the total number of votes each candidate received and the total number of votes from each county.
    4. Calculate the percentage of votes each candidate won and the percentage of total votes from each county.
    5. Determine the winner of the election based on the popular vote and which county had the largest voter turnout.

## Resources

* Data Source: election_results.csv
* Software: Python 3.9.2, Visual Studio Code

## Results

The analyses of the election show that

* There were 369,711 votes cast in the election.
* The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

* The candidate results were:
    - Charles Casper Stockham received 23.05% of the vote with 85,213 votes.
    - Diana DeGette received 73.81% of the vote with 272,892 votes.
    - Raymon Anthony Doane received 3.14% of the vote with 11,606 votes.

* The winner of the election was:
    - Diana DeGette

* The counties involved in this election were:
    - Jefferson
    - Denver
    - Arapahoe

* The county results were:
    - Jefferson county contributed 10.5% of the total votes with 38,855 votes.
    - Denver county contributed 82.8% of the total votes with 306,055 votes.
    - Arapahoe county contributed 6.7% of the total votes with 24,801 votes.

* The county with the largest voter turnout was:
    - Denver county


## Summary

This script may be used for other elections as well.  The variables related to candidate and county names pull data directly from the .csv file, so these variables used in this script are not specific to this election; therefore, this script can be used to analyze any election with any number of candidates and any number of counties (provided the .csv file retains the same structure).  If the structure of the .csv file differs from the one used in this analysis, one would simply edit the indices in the candidate and county name variables in lines 61 and 62 of the script.

```
#Get candidate names and county names
        candidate_name = row[2]
        county_name = row[1]

```

If you had more data in the .csv file, such as the ethnicity, age bracket, or other demographic data you wanted to track for voting in an election, it would be as simple as adding another variable to the previous code block.  Suppose we wanted to track the age bracket of voters.  We would simply add:

```
#Get candidate names and county names
        candidate_name = row[2]
        county_name = row[1]
        voter_age = row[3]

```
Supposing the voter's age bracket is the next column after the candidate name.  Next, we would simple add another if statement inside the for loop which loops over all rows in the .csv file.  The old code is

```
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

```

The new code is a simple addition of the new variable and one new if statement.  (Don't forget to initialize the `voter_age_list` and `votes_by_age` objects at the top of the script where the other lists and dictionaries are initialized).

```
#Loop through all rows in file    
    for row in file_reader:

#Tally up total votes
        total_votes += 1

#Get candidate names and county names
        candidate_name = row[2]
        county_name = row[1]
        voter_age = row[3]

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

        if voter_age not in voter_age_list:

#Add this age bracket to the voter age list
            voter_age_list.append(voter_age)

#Track votes from this age bracket
            votes_by_age[voter_age] = 0
        
        candidate_votes[candidate_name] += 1
        county_votes[county_name] += 1
        votes_by_age[voter_age] +=1

```

After that, it's a matter of editing the code after line 84, which controls what you are writing to the output .txt file.