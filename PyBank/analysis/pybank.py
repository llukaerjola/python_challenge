# Import modules
import csv
import os

# Set file path
csvpath = os.path.join ('budget_data.csv')

#Initialize variables
total_months = 0
total = 0
change_total = 0
previous_month = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""
greatest_increase = 0
change = 0

#Open and read csv
with open(csvpath, newline="")as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row of data after the header for row in csvreader:
    for row in csvreader:
        print(row)
        total_months = total_months + 1
        total = total + int(row[1])
        if previous_month != 0:
            change = int(row[1]) - previous_month
        change_total = change_total + change
        previous_month = int(row[1])
        if (change < greatest_decrease):
            greatest_decrease = change
            greatest_decrease_month = row[0]
        if (change > greatest_increase):
            greatest_increase = change
            greatest_increase_month = row[0]

    print(total_months)

    #Calculate total
    #total = total + int(row[1])

    #Calculate the change between current and previous row
    #change = int(row[1]) - previous_month
    #change_total = change_total + change
    #previous_month = int(row[1])

    

    #Calculate greatest increase in profits
    #if (change < greatest_decrease):
        #greatest_decrease = change
        #greatest_decrease_month = row[0]
    #if (change > greatest_increase):
        #greatest_increase = change
        #greatest_increase_month = row[0]

    #Calculate the average change in profits
    average_change = change_total/(total_months-1)

#Print the results
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total : ${total}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

#Output results to text file
file = open("Financial_Analysis.txt", "w")
file.write("Financial Analysis\n'")
file.write("-------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${total}\n")
file.write(f"Average Change: ${round(average_change,2)}\n")
file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
file.close()