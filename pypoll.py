#import modules
import os
import csv
from collections import Counter


#set Variables
count_votes = 0 #counter for vote
count_khan = 0 #counter for Khan vote
count_li = 0 #counter for Li
count_tooley = 0 #counter for O'Tooley vote
count_correy = 0 #counter for Correy vote
winner_list=[]


poll_path = os.path.join("Resources","election_data.csv")

with open(poll_path, 'r') as pollfile:

    pollreader = csv.reader(pollfile, delimiter=',')
    next(pollreader, None)

    #print(pollread)

    for row in pollreader:
        count_votes = count_votes+1

        if (row[2] == "Khan"):
            count_khan = count_khan + 1
            winner_list.append("Khan")

           
        if (row[2]=="Li"):
            count_li = count_li + 1
            winner_list.append("Li")
        
        if (row[2]=="Correy"):
            count_correy = count_correy + 1
            winner_list.append("Correy")
        
        if (row[2] == "O'Tooley"):
            count_tooley = count_tooley + 1
            winner_list.append("O'Tooley")

khan_percentage = round(count_khan/count_votes*100)
#print(str(khan_percentage))#checking the percentage formula is accurate
li_percentage = round(count_li/count_votes*100)
#print(str(li_percentage))
correy_percentage = round(count_correy/count_votes*100)
#print(str(correy_percentage))    
tooley_percentage = round(count_tooley/count_votes*100) 
#print(str(tooley_percentage))   

winner_count = Counter(winner_list)

max_votes = max(winner_count.values())

#print(max_votes)

#Printing All Output
print ("Election Results ")
print ("----------------------------------")
print ("Total Votes: " + str(count_votes))
print ("----------------------------------")
print ("Khan: "+str(khan_percentage) +" % " + str(count_khan))
print ("Correy: "+str(correy_percentage) +" % " + str(count_correy))
print ("Li "+str(li_percentage) +" % " + str(count_li))
print ("O'Tooley: "+str(tooley_percentage) +" % " + str(count_tooley))
print ("----------------------------------")

if (count_khan == max_votes):

    print ("Winner is Khan")

if (count_li == max_votes):

    print ("Winner is Li")

if (count_correy == max_votes):

    print ("Winner is Correy")

if (count_tooley == max_votes):

    print ("Winner is O'Tooley")

#Writing output to another csv file

poll_output = os.path.join("Analysis", "polloutput.csv")

with open(poll_output, "w", newline="") as writefile:
    pollwriter = csv.writer(writefile)
    pollwriter.writerow (["Election Results "])
    pollwriter.writerow  (["----------------------------------"])
    pollwriter.writerow  (["Total Votes: " + str(count_votes)])
    pollwriter.writerow  (["----------------------------------"])
    pollwriter.writerow  (["Khan: "+str(khan_percentage) +" % " + str(count_khan)])
    pollwriter.writerow  (["Correy: "+str(correy_percentage) +" % " + str(count_correy)])
    pollwriter.writerow  (["Li: "+str(li_percentage) +" % " + str(count_li)])
    pollwriter.writerow  (["O'Tooley: "+str(tooley_percentage) +" % " + str(count_tooley)])
    pollwriter.writerow  (["----------------------------------"])
    pollwriter.writerow  (["Winner is Khan"])



