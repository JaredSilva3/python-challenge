import csv
import os

# Define the file paths
input_file = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('analysis', 'election_analysis.txt')

# Create the analysis folder if it doesn't exist
if not os.path.exists(os.path.dirname(output_file)):
    os.makedirs(os.path.dirname(output_file))

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        total_votes += 1  # Count total votes
        candidate = row['Candidate']
        
        # Count votes for each candidate
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Calculate the percentage of votes and find the winner
winner = ''
winning_votes = 0
candidate_results = []

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_results.append((candidate, votes, percentage))
    
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate

# Print the analysis report to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes, percentage in candidate_results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the analysis results to a text file
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes, percentage in candidate_results:
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")