# 2D array: daily steps (5 days per person)
steps = [
    [4500, 5000, 5200, 5100, 5500],  # Friend 1
    [3900, 4200, 4100, 4600, 4000],  # Friend 2
    [5800, 6000, 6200, 5900, 6100]   # Friend 3
]

# Loop through each row (person)
for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])
    minimum = min(steps[i])
    maximum = max(steps[i])

    print(
        f"Friend {i + 1} - "
        f"Total Steps: {total} | "
        f"Average: {average:.1f} | "
        f"Min: {minimum} | "
        f"Max: {maximum}"
    )

The program goes through each row of the 2D array to show one person’s daily steps, then calculates and displays the total, average, minimum, and maximum step count for that person, with an option to find the overall highest and lowest values in the entire dataset.
