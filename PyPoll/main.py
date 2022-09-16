import os
import csv

pathwayCSV = os.path.join('..','PyPoll','Resources','election_data.csv')

with open(pathwayCSV) as PollingCSV:
    csvreader = csv.reader(PollingCSV, delimiter=',')
    
    #for rows ins csv readers print (rows) -- this shows that the reader works
            #BUT DON'T USE FILE IS HUGE

#dict - word counters javac
#Initialize dictionalary 
#for each candidate check if thy're in there (if in )
#else not in there intitialze it to 1
candidate_dict = {}

    for row in csvreader:
        #pull out the desired values row[2] and add it to the dictionary

#check all the rows to see if the name doesn't exist, 

        

    #print(BallotCol)

#we want to make a dictionary for specific values, candidate : total # of votes
        
        
        

