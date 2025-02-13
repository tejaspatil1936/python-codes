# 1.Arithmetic operators
num1 = 15
num2 = 4
print()
print("Arithmetic operations")
print("num1:", num1, "num2:", num2)
print(num1, "Addition", num2, ":", num1 + num2)  # 19
print(num1, "Subtraction", num2, ":", num1 - num2)  # 11
print(num1, "Multiplication", num2, ":", num1 * num2)  # 60
print(num1, "Division", num2, ":", num1 / num2)  # 3.75
print(num1, "Exponentiation", num2, ":", num1**num2)  # 50625
print(num1, "Modulus", num2, ":", num1 % num2)  # 3
print(num1, "Floor Division", num2, ":", num1 // num2)  # 3

# 2.Assigment operator
# Example: Updating Score using Assignment Operators
print()
print("Assigment operator")
score = 50
print("Score:", score)
score += 10  # score = score + 10
print("Updated Score by 10:", score)  # 60

score *= 2  # score = score * 2
print("Doubled Score by doubling:", score)  # 120

score //= 5  # score = score // 5
print("Floor Divided Score:", score)  # 24


# 3.compariosn operators
# Example: Comparing Student Marks
mark1 = 85
mark2 = 92
print()
print("compariosn operator")
print("Mark1:", mark1, "Mark2:", mark2)
print("Is mark1 equal to mark2?", mark1 == mark2)  # False
print("Is mark1 greater than mark2?", mark1 > mark2)  # False
print("Is mark1 less than or equal to mark2?", mark1 <= mark2)  # True

# 4.Logical Operators
# Example: Checking Admission Eligibility
print()
print("Logical operator")

a = 10
b = 20

is_a_bigger = a > b
print("a :", a, "b :", b)
print("result of comparison ( a > b ):", is_a_bigger)

# 5.Bitwise Operators
# Example: Bitwise Operations on Binary Flags
print()
print("Bitwise operator")
bit1 = 0b1100  # 12 in decimal
bit2 = 0b1010  # 10 in decimal
print("bit1 :", bit1, ",", "bit2 :", bit2)

print(bit1, "Bitwise AND", bit2, "  :", "In binary -> ",bin(bit1 & bit2),"   in decimal -> ", bit1 & bit2)
print(bit1, "Bitwise OR", bit2, "   :", "In binary -> ",bin(bit1 | bit2),"   in decimal -> ", bit1 | bit2)
print(bit1, "Bitwise XOR", bit2, "  :", "In binary -> ",bin(bit1 ^ bit2),"    in decimal -> ", bit1 ^ bit2)
print(bit1, "Bitwise NOT", bit2, "  :", "In binary -> ",bin(~bit1),"  in decimal -> ", ~bit1)
print(bit1, "Left Shift by 1  :", "In binary -> ",bin(bit1 << 1),"  in decimal -> ", bit1 << 1)
print(bit1, "Right Shift by 1 :", "In binary -> ",bin(bit1 >> 1),"    in decimal -> ", bit1 >> 1)

# 6.Identity Operators
# Example: Identity Check in Python
x = [10, 20, 30]
y = x
z = [10, 20, 30]
print()
print("Identity operator")
print("x is y:", x is y)
print("x is z:", x is z)
print("x == z:", x == z)

# 7.Membership Operators
# Example: Checking Item Presence in a List
fruits = ["apple", "banana", "cherry"]
print()
print("Membership operator")
print("Is 'apple' in the list?", "apple" in fruits)  # True
print("Is 'grape' not in the list?", "grape" not in fruits)
