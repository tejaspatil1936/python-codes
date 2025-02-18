#  Operator Precedence in Python

print("=== Operator Precedence demonstration ===\n")

def show(expression, result):
    print(expression, "=", result)
    print()

print("1. Parentheses have the highest precedence:")
show("(2 + 3) * 4", (2 + 3) * 4)

print("2. Exponentiation before multiplication:")
show("2 * 3 * 2", 2 * 3 * 2)

print("3. Multiplication before addition:")
show("2 + 3 * 4", 2 + 3 * 4)

print("4. Division before subtraction:")
show("10 - 6 / 2", 10 - 6 / 2)

print("5. Modulo before addition:")
show("10 + 9 % 4", 10 + 9 % 4)

print("6. Floor division before addition:")
show("10 + 5 // 2", 10 + 5 // 2)

print("7. Comparison happens after arithmetic:")
show("3 + 2 > 4", 3 + 2 > 4)

print("8. Logical NOT before AND, AND before OR:")
show("not False and True or False", not False and True or False)

print("9. Bitwise AND before OR:")
show("5 | 2 & 3", 5 | 2 & 3)

print("10. Left shift before bitwise OR:")
show("1 << 2 | 1", 1 << 2 | 1)

print("=== End of Explanation ===")