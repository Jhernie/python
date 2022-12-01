
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
    votes = []
    candidates = []
    results_counter = {}

    ##write loop that creates a counter and appends info to lists and dict
    for row in csvreader:
        votes.append(row[0])
        if row[2] not in candidates:
                candidates.append(row[2])
                tally = candidates.index(row[2])
                results_counter[tally] = 1
        else:
            tally = candidates.index(row[2])
            results_counter[tally] = results_counter[tally] + 1

    ##change keys in dictionary
    results_counter["Charles Casper Stockham"] = results_counter.pop(0)
    results_counter["Diana DeGette"] = results_counter.pop(1)
    results_counter["Raymon Anthony Doane"] = results_counter.pop(2) 
    
    ##define variables
    vote_count = len(votes)
        #access the key where the value within the dict is highest
    winner = max(results_counter, key=results_counter.get)

    ##print result summary
    print("Election Results")
    print("_"*25)
    print()
    print(f'Total Votes: {vote_count}')
    print("_"*25)
    print()
    for candidate, tally in results_counter.items():
        message1 = f"{candidate}: {round(((tally/vote_count)*100),3)}% ({tally})"
        message2 = f"Winner: {winner}"
        print(message1)
    print("_"*25)
    print()
    print(message2)
    
##export result summary to txt file

with open("pypoll_analysis.txt", "w") as f:
    print("Election Results", file = f)
    print("_"*25, file = f)
    print(" ", file = f)
    print(f'Total Votes: {vote_count}', file = f)
    print("_"*25, file = f)
    print(" ", file = f)
    for candidate, tally in results_counter.items():
        message1 = f"{candidate}: {round(((tally/vote_count)*100),3)}% ({tally})"
        message2 = f"Winner: {winner}"
        print(message1, file = f)
    print("_"*25, file = f)
    print(" ", file = f)
    print(message2, file = f)


#     print("Election Results", file = f)
#     print("_"*25, file = f)
#     print(f'Total Votes: {vote_count}', file = f)
#     print("_"*25, file = f)
#     #print(results_counter, file = f)
#     file.write(f"{message2}\n")















###____________CODE_GRAVEYARD____________###
     
     #print(results_counter)
     
     
     
        ##check if that votes (key) is in the dictionary. if true then add one to the existing key. 
            # if false then add key to dictionary with a value of 1
    
    # for tally in results_counter:
    #     if tally in results_counter():
    #         results_counter[tally] = results_counter[tally] + 1
                #OR results_counter[tally] += 1
    #     else:
    #         results_counter[tally] = 1
    
    
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
        
        
        

