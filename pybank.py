#import modules
import os
import csv

#Set Variables
count_months =0
total_revenue = 0
average_change = 0
months = []
difference = []
pl = []
max_profit=0
max_loss=0


#set budget path
budget_path = os.path.join("PyBank","Resources", "budget_data.csv")

with open(budget_path, newline="") as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=',')
    next(budgetreader)

    for row in budgetreader:
        count_months = count_months+1 #months counter
        months.append(row[0])
        total_revenue = total_revenue + float(row[1])
        pl.append(int(row[1])) #Adding profit and loss value to the lists

        #print(count_months) #Just to check if the counter for months works or not
        #print(total_revenue) #Just to check if the counter for revenue work
        #print(pl) #Just to check the accuracy of all profit and loss value in the list
        #print(len(pl)) #checking the length og list is 86

for x in range(count_months-1): 
    difference.append(pl[x+1]-pl[x]) #calculating the difference and adding to the list

    #print(difference)
    total_difference = sum(difference)
    #print(total_difference)

#Calculating average change
average_change = round((total_difference/(count_months-1)),2)
#print (average_change) #checking the average calculation is correct

#Finding max profit and max loss value
max_profit = max(difference)
#print(max_profit)#Checking the value of max profit is correct 
max_loss = min(difference)
#print(max_loss)# Checking the value of max loss in profit is correct


#Finding the maximum profit increase month and maximum Loss in profits month 
max_profit_month = difference.index(max_profit)
max_loss_month = difference.index(max_loss)
profit_month = months[max_profit_month+1]
loss_month = months[max_loss_month+1]

#print(profit_month) #Checking the maximum profit month is correct
#print(loss_month) #checking the maximum loss in profit month is correct

#Gitbash output
print ("Financial Analysis")
print ("----------------------------------------")
print("Total months: "+ str(count_months))
print("Total: $"+str(total_revenue))
print("Average Change: $"+str(average_change))
print("Greatest Increase in Profits: "+profit_month+ "   $" +str(max_profit))
print("Greatest Decrease in Profits: "+loss_month+ "   $" +str(max_loss))


#Writing output to Analysis/analysis.csv
output_path=os.path.join("PyBank","Analysis", "analysis.csv")

with open(output_path,"w", newline="")as outputfile:
    output_write = csv.writer(outputfile)

    output_write.writerow (["Financial Analysis"])
    output_write.writerow (["----------------------------------------"])
    output_write.writerow (["Total months: "+ str(count_months)])
    output_write.writerow (["Total: $"+str(total_revenue)])
    output_write.writerow (["Average Change: $"+str(average_change)])
    output_write.writerow (["Greatest Increase in Profits: "+profit_month+ "   $" +str(max_profit)])
    output_write.writerow (["Greatest Decrease in Profits: "+loss_month+ "   $" +str(max_loss)])












