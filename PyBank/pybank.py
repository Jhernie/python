##import dependencies
import os  
import csv 

##establish path
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

##open csv file using path
with open(csvpath) as BudgetCSV:
    csvreader = csv.reader(BudgetCSV, delimiter=",")
    ##ignore headers
    next(csvreader, None)

    ##create empty lists to append data to
    months = []
    profit_loss = []
    profit_loss_change = []

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(float(row[1]))

    for rows in range(len(profit_loss)-1):
        profit_loss_change.append(profit_loss[rows + 1] - profit_loss[rows])

    ##define variables
    total_months = len(months)
    sum_profit_loss = round(sum(profit_loss))
    average = round(sum(profit_loss_change)/len(profit_loss_change), 2)
    greatest_increase = max(profit_loss_change)
    greatest_decrease = min(profit_loss_change)

    ##print summary stats
    print(" ")
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Number of Months: {total_months}')
    print(f'Total: ${sum_profit_loss}')
    print(f'Average P&L Change: ${average}')
    print(f'Greatest Increase in Profits: {greatest_increase}') #need to add month
    print(f'Greatest Decrease in Profits: {greatest_decrease}')

##print to txt file
with open("pybank_analysis.txt", "w") as f:
    print("Financial Analysis", file = f)
    print("----------------------------", file = f)
    print(f'Total Number of Months: {total_months}', file = f)
    print(f'Total: ${sum_profit_loss}', file = f)
    print(f'Average P&L Change: ${average}', file = f)
    print(f'Greatest Increase in Profits: {greatest_increase}', file = f) #need to add month
    print(f'Greatest Decrease in Profits: {greatest_decrease}', file = f)





    











