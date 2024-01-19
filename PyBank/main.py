import csv

file_path = 'Resources/budget_data.csv'

# Initialize variables
total_months = 0
total_profit_losses = 0
total_changes = 0
previous_month_value = 0
greatest_increase = 0
greatest_decrease = 0

# Read the CSV file
with open(file_path, mode='r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        total_months += 1
        current_month_value = int(row[1])
        total_profit_losses += current_month_value

        current_change = current_month_value - previous_month_value
        if previous_month_value == 0:
            current_change = 0

        total_changes += current_change

        if current_change > greatest_increase:
            greatest_increase_date = row[0]
            greatest_increase = current_change

        if current_change < greatest_decrease:
            greatest_decrease_date = row[0]
            greatest_decrease = current_change

        previous_month_value = current_month_value

# Compute the average change
average_change = total_changes / (total_months - 1) 


# Print the results

output = f'''
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_losses:,}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:,})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:,})
'''

print(output)

# Write results to a file
output_file = 'analysis/financial_analysis.txt'
with open(output_file, 'w') as file:
    file.write(output)
