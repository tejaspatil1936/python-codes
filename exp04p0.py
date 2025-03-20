# Get user input
rows = int(input("Enter the number of rows for Pascal's Triangle: "))

# Generate Pascal's Triangle
for i in range(rows):
    num = 1  # First number in each row is always 1
    for j in range(i + 1):
        print(num, end=" ")  # Print number with space
        num = num * (i - j) // (j + 1)  # Compute next number using formula
    print()  # Move to the next line
