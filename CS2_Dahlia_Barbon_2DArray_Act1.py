1. Plan the 2D Array StructureStructure
- What does each row represent?
Each row represents one person’s step counts for the week:
Row 0 → Me
Row 1 → Spencer
Row 2 → Aaron
Row 3 → Derek

- What does each column represent?
Each column represents a day of the week:
Column 0 → Monday
Column 1 → Tuesday
Column 2 → Wednesday
Column 3 → Thursday
Column 4 → Friday

2. Sample 2D Array
# Daily step counts for 5 days (Mon–Fri)
step_counts = [
    [8200, 9100, 10000, 8700, 9500],   # Me
    [7500, 8800, 9200, 8900, 9400],    # Spencer
    [10000, 10500, 9800, 11000, 10800],# Aaron
    [6800, 7200, 7600, 8000, 8300]     # Derek
]

3. Sample Code Operations
- Access a specific value : Aaron's steps on Thursday
print(step_counts[2][3])

- Update a specific value : Correct Spencer's Wednesday steps to 7800
step_counts[3][2] = 7800
