import os  
import csv 

csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

with open(csvpath) as BudgetCSV:
    csvreader = csv.reader(BudgetCSV, delimiter=",")
    next(csvreader, None) # skip the headers, found on stack overflow

    months = []
    ProfitLoss = []

    for row in csvreader:
        # print(i[0]) 
        months.append(row[0])
        ProfitLoss.append(float(row[1]))
    
    # NO NEED #ProfitLossInt = [round(float(i)) for i in ProfitLoss]
    # print(ProfitLossInt)

    ##count total number of months included in the dataset
    print(len(months))
    print(sum(ProfitLoss))

    ##perform arithmetic on this isolated p&l list

    #NetPL = sum(ProfitLossInt)
    # print(NetPL)

    ##create the average for p&L

    # average = NetPL/len(ProfitLossInt)
    # print(average)

    plChange = []

    for i in range(len(ProfitLoss)-1):
        plChange.append(ProfitLoss[i + 1] - ProfitLoss[i])

    average = sum(plChange)/len(plChange)
    print(f'Average Change:$ {average}')

    GreatestedIncrease = max(plChange)
    print(f'Greatest Increase in Profits: {months}, {GreatestedIncrease}')

    GreatestDecrease = min(plChange)
    print(f'Greatest Decrease in Profits: {months}, {GreatestDecrease}')




## NOW NEED TO EXPORT TO TXT FILE, and also figure out how to 
    ##reference the specific month..might need a new variable?


#create a calcultion fro the differences from month to month

#when we perfomr that calculation, think about how to change the loop so that the loop stops at the end

# 

    











