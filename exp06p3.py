# Creating a tuple with three elements
my_tuple = (10, 20, 30)

# Tuple unpacking
a, b, c = my_tuple
print("Before Swapping:")
print("a =", a, "b =", b, "c =", c)

# Swapping values using tuple unpacking
a, b, c = c, a, b
print("After Swapping:")
print("a =", a, "b =", b, "c =", c)
