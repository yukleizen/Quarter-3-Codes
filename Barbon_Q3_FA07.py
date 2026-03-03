# Step counts for 4 people over 5 days (Mon–Fri)
step_counts = [
    [8200, 9100, 10000, 8700, 9500],   # Me
    [7500, 8800, 9200, 8900, 9400],    # Spencer
    [10000, 10500, 9800, 11000, 10800],# Aaron
    [6800, 7200, 7600, 8000, 8300]     # Derek
]

people = ["Me", "Spencer", "Aaron", "Derek"]

# Initialize variables to track max and min steps in the dataset
max_steps = step_counts[0][0]
min_steps = step_counts[0][0]

# Loop through each person's step counts
for i in range(len(step_counts)):
    row = step_counts[i]
    total = sum(row)
    average = total / len(row)
    
    # Update max and min
    row_max = max(row)
    row_min = min(row)
    if row_max > max_steps:
        max_steps = row_max
    if row_min < min_steps:
        min_steps = row_min
    
    # Print row summary
    print(f"{people[i]}'s steps: {row}")
    print(f"Total steps: {total}")
    print(f"Average steps: {average:.2f}\n")

# Print overall max and min steps
print(f"Maximum steps in the dataset: {max_steps}")
print(f"Minimum steps in the dataset: {min_steps}")

1. How did using an array help you analyze the data more easily?
Using an array allowed me to store all the step counts in a single organized structure. Each row represented a person, and each column represented a day, which made it easy to locate specific values. I could loop through the array to calculate totals and averages without repeating code. This made comparing the step counts of different people much faster and more efficient.

2. Which part of summarizing the data was easy or difficult?
Calculating the total and average steps for each person was easy because I could use the sum() function and divide by the number of days. Printing each row clearly was also straightforward. The more difficult part was finding the maximum and minimum values across the entire dataset since I had to check every row and column. Overall, the array still made the process much simpler than working with individual values.
