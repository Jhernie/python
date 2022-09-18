import os  
import csv 

csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

#Define the variables of min month and max month as well
#min_month = 0
#max_month = 0


with open(csvpath) as BudgetCSV:
    csvreader = csv.reader(BudgetCSV, delimiter=",")
    next(csvreader, None) # skip the headers, found on stack overflow

    months = []
    ProfitLoss = []

    for row in csvreader:
        months.append(row[0])
        ProfitLoss.append(float(row[1]))
    
    # print(i[0]) 
    # NO NEED #ProfitLossInt = [round(float(i)) for i in ProfitLoss], # print(ProfitLossInt)
    
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

    average = int(sum(plChange)/len(plChange))
    print(f'Average Change:$ {average}')


    #within this for loop, I can actually add this varible and create a condition instea
        #basically to assign the value 
    GreatestedIncrease = max(plChange)
    print(f'Greatest Increase in Profits: {GreatestedIncrease}') #need to add month

    GreatestDecrease = min(plChange)
    print(f'Greatest Decrease in Profits: {GreatestDecrease}')


    #OUTPAth to print to txt




## NOW NEED TO EXPORT TO TXT FILE, and also figure out how to 
    ##reference the specific month..might need a new variable?


#create a calcultion fro the differences from month to month

#when we perfomr that calculation, think about how to change the loop so that the loop stops at the end

# 

    











