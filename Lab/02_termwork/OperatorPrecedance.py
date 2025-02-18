# # # Demonstrating Operator Precedence in Python

# # # Parentheses override precedence
# # print("(1) Parentheses override precedence: ", (5 + 3) * 2)  # 8 * 2 = 16

# # # Exponentiation has higher precedence than multiplication
# # print("(2) Exponentiation before multiplication: ", 2**3 * 4)  # (2^3) * 4 = 8 * 4 = 32

# # # Unary operators have higher precedence than multiplication
# # print("(3) Unary minus before multiplication: ", -3 * 4)  # (-3) * 4 = -12

# # # Multiplication and division before addition and subtraction
# # print("(4) Multiplication before addition: ", 10 + 3 * 2)  # 10 + (3*2) = 10 + 6 = 16

# # # Floor division and modulo have the same precedence as multiplication
# # print("(5) Floor division before addition: ", 10 + 9 // 4)  # 10 + (9//4) = 10 + 2 = 12
# # print("(6) Modulo before addition: ", 10 + 9 % 4)  # 10 + (9 % 4) = 10 + 1 = 11

# # # Bitwise AND before Bitwise OR
# # print("(7) Bitwise AND before OR: ", 5 | 3 & 2)  # 5 | (3 & 2) = 5 | 2 = 7

# # # Comparison operators have lower precedence than arithmetic
# # print("(8) Comparison after arithmetic: ", 3 + 2 > 4)  # (3+2) > 4 -> 5 > 4 -> True

# # # Logical NOT before AND, AND before OR
# # print(
# #     "(9) Logical NOT before AND/OR: ", not False and True or False
# # )  # (not False) -> True, True and True -> True

# # # Left-to-right evaluation in case of same precedence
# # print("(10) Left-to-right evaluation: ", 10 - 4 + 2)  # (10 - 4) + 2 = 6 + 2 = 8


# # Demonstrating Operator Precedence in Python

# # Example 1: Basic operator precedence
# result1 = 1 + 2 * 3  # Multiplication has higher precedence than addition
# print("Result of 1 + 2 * 3:", result1)  # Expected output: 7

# # Example 2: Parentheses to change precedence
# result2 = (1 + 2) * 3  # Parentheses change the order of operations
# print("Result of (1 + 2) * 3:", result2)  # Expected output: 9

# # Example 3: Exponentiation and multiplication
# result3 = 5 + 3 * 2 ** 2 // 4
# # Breakdown: 
# # Step 1: 2 ** 2 = 4
# # Step 2: 3 * 4 = 12
# # Step 3: 12 // 4 = 3
# # Step 4: 5 + 3 = 8
# print("Result of 5 + 3 * 2 ** 2 // 4:", result3)  # Expected output: 8

# # Example 4: Multiple operations with same precedence
# result4 = (10 - 4) * (6 / 2) 
# # Breakdown:
# # Step 1: (10 - 4) = 6
# # Step 2: (6 / 2) = 3
# # Step 3: Result = (6 * 3) =18
# print("Result of (10 - 4) * (6 / 2):", result4) # Expected output:18

# # Example of left-to-right evaluation for same precedence
# result5 = 10 / 5 * 4  
# # Both division and multiplication have the same precedence, evaluated left to right.
# print("Result of 10 / 5 * 4:", result5) # Expected output:8.0



# # Simple demonstration of operator precedence in Python

# # Example 1: Multiplication before addition
# result1 = 2 + 3 * 4
# print("2 + 3 * 4 =", result1)  # Expected output: 14

# # Example 2: Using parentheses to change precedence
# result2 = (2 + 3) * 4
# print("(2 + 3) * 4 =", result2)  # Expected output: 20

# # Example 3: Exponentiation has the highest precedence
# result3 = 2 + 3 ** 2
# print("2 + 3 ** 2 =", result3)  # Expected output: 11

# # Example 4: Division and multiplication have the same precedence, evaluated left to right
# result4 = 10 / 2 * 5
# print("10 / 2 * 5 =", result4)  # Expected output: 25.0
# z


print("Parentheses first")
print("(2 + 3) * 4")  
print("actual output", (2 + 3) * 4)    
print("expected output", 2 + 3 * 4)  # Without precedence, it would be (2+3) * 4  
print("-" * 50)

print("Exponentiation before multiplication")
print("2 * 3 ** 2")  
print("actual output", 2 * 3 ** 2)    
print("expected output", (2 * 3) ** 2)  # Left to right: 2 * 3 first, then ** 2  
print("-" * 50)

print("Multiplication before addition")
print("2 + 3 * 4")  
print("actual output", 2 + 3 * 4)    
print("expected output", (2 + 3) * 4)  # Without precedence: (2+3) then * 4  
print("-" * 50)

print("Division before subtraction")
print("10 - 6 / 2")  
print("actual output", 10 - 6 / 2)    
print("expected output", (10 - 6) / 2)  # Without precedence: 10-6 first, then /2  
print("-" * 50)

print("Modulo has same precedence as multiplication")
print("10 + 9 % 4")  
print("actual output", 10 + 9 % 4)    
print("expected output", (10 + 9) % 4)  # Without precedence: 10+9 first, then %4  
print("-" * 50)

print("Floor division before addition")
print("10 + 5 // 2")  
print("actual output", 10 + 5 // 2)    
print("expected output", (10 + 5) // 2)  # Without precedence: 10+5 first, then //2  
print("-" * 50)

print("Comparison operators after arithmetic")
print("2 + 3 * 2 < 10")  
print("actual output", 2 + 3 * 2 < 10)    
print("expected output", (2 + 3) * 2 < 10)  # Without precedence: (2+3)*2 first  
print("-" * 50)

print("Logical NOT before AND, AND before OR")
print("not False and True or False")  
print("actual output", not False and True or False)    
print("expected output", not (False and True) or False)  # Without precedence  
print("-" * 50)

print("Bitwise AND before OR")
print("5 | 2 & 3")  
print("actual output", 5 | 2 & 3)    
print("expected output", (5 | 2) & 3)  # Without precedence: 5|2 first, then &3  
print("-" * 50)

print(" Left shift before bitwise OR")
print("1 << 2 | 1")  
print("actual output", 1 << 2 | 1)    
print("expected output", (1 << 2) | 1)  # Without precedence: 1<<2 first, then |1  
print("-" * 50)

print(" Mixing arithmetic and bitwise operations")
print("8 + 2 >> 1")  
print("actual output", 8 + 2 >> 1)    
print("expected output", (8 + 2) >> 1)  # Without precedence: 8+2 first, then >>1  
print("-" * 50)
