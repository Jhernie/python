import os  
import csv 

csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

with open(csvpath) as BudgetCSV:
    csvreader = csv.reader(BudgetCSV, delimiter=",")
    next(csvreader, None) # skip the headers, found on stack overflow

    months = []
    ProfitLoss = []

    for i in csvreader:
        # print(i[0]) 
        months.append(i[0])
        ProfitLoss.append(i[1])

    ProfitLossInt = [round(float(i)) for i in ProfitLoss]
    # print(ProfitLossInt)

    ##count total number of months included in the dataset
    # print(len(months))
    # print(len(ProfitLossInt))

    ##perform arithmetic on this isolated p&l list

    NetPL = sum(ProfitLossInt)
    # print(NetPL)

    ##create the average for p&L

    average = NetPL/len(ProfitLossInt)
    print(average)






        



#create a calcultion fro the differences from month to month

#when we perfomr that calculation, think about how to change the loop so that the loop stops at the end

# if i == (i - 1): 

    











