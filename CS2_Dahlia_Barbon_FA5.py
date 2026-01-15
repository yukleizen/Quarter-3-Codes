# Names of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Same 2D array of daily steps
steps = [
    [4500, 5000, 5200, 5100, 5500],  # Me
    [3900, 4200, 4100, 4600, 4000],  # Spencer
    [5800, 6000, 6200, 5900, 6100]   # Aaron
]

# Calculate total steps per day
daily_totals = []

for col in range(len(days)):
    day_total = 0
    for row in range(len(steps)):
        day_total += steps[row][col]
    daily_totals.append(day_total)
    print(f"{days[col]} - Total Steps: {day_total}")

# Identify most active day
most_active_day = days[daily_totals.index(max(daily_totals))]
print(f"\nMost active day overall: {most_active_day}")

