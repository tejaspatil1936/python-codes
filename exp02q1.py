# Get user input
num1 = int(input("Enter first decimal number: "))
num2 = int(input("Enter second decimal number: "))

# Display binary conversions
print("\nBinary Conversion:")
print(f"{num1} = {bin(num1)[2:]}")
print(f"{num2} = {bin(num2)[2:]}")

# Display bitwise operations directly in print statements
print("\nBitwise Operations:")
print(f"AND: {bin(num1 & num2)[2:]}")
print(f"OR: {bin(num1 | num2)[2:]}")
print(f"XOR: {bin(num1 ^ num2)[2:]}")
print(f"NOT {num1}: {bin(~num1)}")  # Keeps negative representation
print(f"NOT {num2}: {bin(~num2)}")  # Keeps negative representation

# Logical condition checks directly in print statements
print("\nLogical Conditions:")
print(f"Both AND and OR are non-zero: {(num1 & num2) != 0 and (num1 | num2) != 0}")
print(f"Either XOR or any NOT is non-zero: {(num1 ^ num2) != 0 or (~num1) != 0 or (~num2) != 0}")
print(f"AND, OR, and XOR all positive: {(num1 & num2) > 0 and (num1 ^ num2) > 0 and (num1 | num2) > 0}")
