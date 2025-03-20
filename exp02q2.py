# User Input
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
constant = float(input("Enter a constant to add to the area: "))

# Calculate the area of the triangle
area = 0.5 * base * height

# Print the initial area
print("Initial Area:", area)

# Add the constant to the area using compound assignment operator
area += constant

# Print the modified area
print("Area after adding constant:", area)
