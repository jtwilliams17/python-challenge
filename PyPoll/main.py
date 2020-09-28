import os
import csv

voterid = []
county = []
candidate = []

# import csv file and skip headers
with open('Resources/JamesWilliams_election_data.csv') as csvpath:
    csv_reader = csv.reader(csvpath, delimiter=",")
    next(csv_reader, None)

    # add to predefined lists from csv columns
    for row in csv_reader:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    # calculate total votes
    total_votes = len(county)

    # list of candidates using 'set' function found on geeksforgeeks.org
    candidate_list = set(candidate)

    #total votes for each candidate
    Khan_votes = candidate.count('Khan')
    Correy_votes = candidate.count('Correy')
    Li_votes = candidate.count('Li')
    OTooley_votes = candidate.count("O'Tooley")

    #calculate vote percent for each candidate
    Khan_percent = round((Khan_votes / total_votes) * 100, 3)
    Correy_percent = round((Correy_votes / total_votes) * 100, 3)
    Li_percent = round((Li_votes / total_votes) * 100, 3)
    OTooley_percent = round((OTooley_votes / total_votes) * 100, 3)

    # calculate the most votes an winner
    list_of_counts = [Khan_votes, Correy_votes, Li_votes, OTooley_votes]
    
    if max(list_of_counts) == Khan_votes:
        winner = 'Khan'
    elif max(list_of_counts) == Correy_votes:   
        winner = 'Correy'
    elif max(list_of_counts) == Li_votes:   
        winner = 'Li'
    else:   
        winner = "O'Tooley"

    #print results and and export to text file 
    print("Election Results","-------------------------","Total Votes: "+str(total_votes),"-------------------------",\
    "Khan: "+str(Khan_percent)+"% "+"("+str(Khan_votes)+")",\
    "Correy: "+str(Correy_percent)+"% "+"("+str(Correy_votes)+")",\
    "Li: "+str(Li_percent)+"% "+"("+str(Li_votes)+")",\
    "O'Tooley: "+str(OTooley_percent)+"% "+"("+str(OTooley_votes)+")",\
    "-------------------------", "Winner: "+str(winner), "-------------------------", sep="\n")