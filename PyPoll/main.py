import os
import csv

pathwayCSV = os.path.join('Resources','election_data.csv')

with open(pathwayCSV) as PollingCSV:
    csvreader = csv.reader(PollingCSV, delimiter=',')
    next(csvreader, None)
    
    votes = []

    for rows in csvreader:
        votes.append(rows[2])
        #if else statement, can be made in this same for loop - take index of candidate
            #name [2], then start at a value, and loop down through the entire list
            #ask the loop to store the value if it is unique, compare it to the one above
            #and when the next candidate changes, begin storing that and compare the next 
            #value to that

    candidate_count = votes.count("Charles Casper Stockham")
    print(candidate_count)


    
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

#dict - word counters javac
#Initialize dictionalary 
#for each candidate check if thy're in there (if in )
#else not in there intitialze it to 1


#candidate_dict = {}

    #for row in csvreader:
        #pull out the desired values row[2] and add it to the dictionary

#check all the rows to see if the name doesn't exist, 

        

    #print(BallotCol)

#we want to make a dictionary for specific values, candidate : total # of votes
        
        
        

