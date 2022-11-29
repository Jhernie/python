##import dependencies
import os
import csv

##establish path
pathwayCSV = os.path.join('Resources','election_data.csv')

##open csv file using path
with open(pathwayCSV) as PollingCSV:
    csvreader = csv.reader(PollingCSV, delimiter=',')
    ##ignore headers
    next(csvreader, None)
    
    ##create empty lists and dict to append data to
    total_votes = []
    candidates = []
    candidate_votes = []
    
    for row in csvreader:
        total_votes.append(row[0])
        if row[2] not in candidates:
                candidates.append(row[2])
                index = candidates.index(row[2])
                candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1

    ##create empty dictionary to append data to
    results = {}

    ##check if that votes (key) is in the dictionary. if true then add one to the existing key. 
            # if false then add key to dictionary with a value of 1
    
    for tally in total_votes:
        if tally in results.keys():
            results[tally] = results[tally] + 1
        else:
            results[tally] = 1

    ##define variables
    vote_count = len(total_votes)

    print("Election Results")
    print("_"*25)
    print()
    print(f'Total Votes: {vote_count}')
    print("_"*25)
    print(results)

with open("pypoll_analysis.txt", "w") as f:
    print("Election Results", file = f)
    print("_"*25, file = f)
    print(f'Total Votes: {vote_count}', file = f)
    print("_"*25, file = f)
    print(results, file = f)







###____________CODE_GRAVEYARD____________###
    #another way to count votes
    # for count in votes:
    #     if count not in votes:
    #         count += 1
    #         votes.count(count)
    #     print(votes)
    #     break

    #print(votes)
    #break 
    
##Find the function to create a counter, count unique values in a list, then add it to 
    #the dictionary?

    # count = 0
    # candiate_count = []

        #print(rows[0])
        #you can print "break" at the end of the for loop

    
    #for rows ins csv readers print (rows) -- this shows that the reader works
            #BUT DON'T USE FILE IS HUGE

#candidate_dict = {}

    #for row in csvreader:
        #pull out the desired values row[2] and add it to the dictionary

#check all the rows to see if the name doesn't exist, 

    #print(BallotCol)

#we want to make a dictionary for specific values, candidate : total # of votes
        
        
        

