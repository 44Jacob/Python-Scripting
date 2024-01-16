import csv
import os
data = []

# Ensure the file path is correct
file_path = '/Users/yakupaltinisik/Desktop/Data-Analyst/Projects/Python-Analysis/budget_data.csv'

# Check if the file exists in the specified path
if not os.path.exists(file_path):
      print(f"File not found: {file_path}")
      exit()

# Initialize variables
total_months = 0
total_profit_losses = 0
changes = []
previous_month_value = None

# Read the CSV file
with open(file_path, mode='r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        total_months += 1
        current_month_value = int(row[1])
        total_profit_losses += current_month_value

        if previous_month_value is not None:
            change = current_month_value - previous_month_value
            changes.append(change)

        previous_month_value = current_month_value

# Compute the average change
average_change = sum(changes) / len(changes) 


# Find the greatest increase and decrease in profits
greatest_increase = max(changes, default=0)
greatest_decrease = min(changes, default=0)
greatest_increase_date = ""
greatest_decrease_date = ""

if changes:
    greatest_increase_date = data[changes.index(greatest_increase) + 1][0]
    greatest_decrease_date = data[changes.index(greatest_decrease) + 1][0]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Write results to a file
output_file = '/Users/yakupaltinisik/Desktop/Data-Analyst/Projects/Python-Analysis/financial_analysis.txt'
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
