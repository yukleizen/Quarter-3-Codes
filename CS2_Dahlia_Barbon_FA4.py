# Names of each person
names = ["Me", "Spencer", "Aaron"]

# Same 2D array of daily steps
steps = [
    [4500, 5000, 5200, 5100, 5500],  # Me
    [3900, 4200, 4100, 4600, 4000],  # Spencer
    [5800, 6000, 6200, 5900, 6100]   # Aaron
]

# Calculate total steps for each person
totals = []
for person_steps in steps:
    totals.append(sum(person_steps))

# Find highest and lowest totals
highest_total = max(totals)
lowest_total = min(totals)

# Identify person with highest total
highest_person = names[totals.index(highest_total)]

# Display results
print("Total steps per person:")
for i in range(len(names)):
    print(f"{names[i]}: {totals[i]}")

print(f"\nHighest total steps: {highest_person} ({highest_total})")
print(f"Difference between highest and lowest total: {highest_total - lowest_total}")
