# Get user input
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

# Check if the given sides form a valid triangle
if a + b <= c or a + c <= b or b + c <= a:
    print("Not a triangle.")
else:
    # Determine the type of triangle
    if a == b == c:
        print("Equilateral Triangle")
    if a == b or b == c or a == c:
        print("Isosceles Triangle")
    if a != b and b != c and a != c:
        print("Scalene Triangle")
