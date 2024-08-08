import csv

# Set the path for the CSV file 
file_path = 'Resources/budget_data.csv'

# Initialize variables for analysis
total_months = 0
net_total = 0
previous_profit_losses = None
changes = []
greatest_increase = {'date': '', 'amount': float('-inf')}
greatest_decrease = {'date': '', 'amount': float('inf')}

# Open the CSV file and read the data
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Store the header row

    for row in reader:
        date = row[0]
        profit_losses = int(row[1])

        total_months += 1
        net_total += profit_losses

        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)

            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = date

            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = date

        previous_profit_losses = profit_losses

# Calculate the average change in Profit/Losses
average_change = sum(changes) / len(changes) if changes else 0

# Prepare the analysis report
analysis_report = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the analysis report to the terminal
print(analysis_report)

# Save the analysis results to a text file
output_file = 'analysis/financial_analysis.txt'
with open(output_file, mode='w') as file:
    file.write(analysis_report)