# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

import csv
import os
# Assign a variable for the file to load from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable for the file to save to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# initialize a total vote counter
total_votes=0

# candidate options and candidate votes
candidate_options=[]
candidate_votes={}
#winner=[]

# Winning candidate and winning count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analise the data here
    # print(election_data)
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # print the header row
    headers = next(file_reader)
    print(headers)

    # print each row in the CSV file
    for row in file_reader:
        #print(row)

        # add to total cote count
        #total_votes=total_votes+1
        total_votes +=1


        # print the candidate name from each row
        candidate_name=row[2]
        
        if candidate_name not in candidate_options:

            #add candidate name to the candidate list
            candidate_options.append(candidate_name)

            #begin tracking that candidate's votes
            candidate_votes[candidate_name]=0
        
        candidate_votes[candidate_name] += 1
        
        
        

    print(candidate_options)
    print(candidate_votes)

    # Determine the percentage of the votes for each candidates by looping through the candidate options
    for candidate_name in candidate_options:
        #retrieve vote count of each candidate
        votes=candidate_votes[candidate_name]
        # calculate the percentage of the votes
        vote_percentage = float(votes)/float(total_votes) * 100
        print(f"{candidate_name} received {vote_percentage:.1f}% of the votes for the total of {candidate_votes[candidate_name]} out of total votes of {total_votes}")

    for candidate_name in candidate_votes:
        #retrieve vote count of each candidate
        votes=candidate_votes[candidate_name]
        # calculate the percentage of the votes
        vote_percentage = float(votes)/float(total_votes) * 100

        print(f"{candidate_name} with {votes:,} votes and {vote_percentage:.1f}% of votes")

        if votes>winning_count and vote_percentage>winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------"

    )
    print(winning_candidate_summary)
    # winner.clear()
    # winner.append(winning_candidate)
    # winner.append(winning_count)
    # winner.append(winning_percentage)
    # print(winner)
    # print(f"**********************\n{winner[0]} is declared the WINNER with {winner[1]} votes and {winner[2]}% of the votes\n**********************\n")



with open(file_to_save,"w") as output:
    output.write(str(total_votes))
   
