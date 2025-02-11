# 6.Identity Operators
x = [10, 20, 30]
y = x
z = [10, 20, 30]
print(id(x))
print(id(y))
print(id(z))
print("x is y:", x is y)
print("x is z:", x is z)
print("x == z:", x == z)
