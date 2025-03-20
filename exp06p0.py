# Creating a tuple of tuples
nested_tuple = ((1, 2, 3), ('a', 'b', 'c'), (True, False, None))

# Accessing elements from the outer tuple
print("Outer Tuple:", nested_tuple)

# Accessing an inner tuple
print("First inner tuple:", nested_tuple[0])  # (1, 2, 3)

# Accessing elements from an inner tuple
print("Element from first inner tuple:", nested_tuple[0][1])  # 2
print("Element from second inner tuple:", nested_tuple[1][2])  # 'c'
print("Element from third inner tuple:", nested_tuple[2][0])  # True
