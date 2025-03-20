# Creating two tuples
tuple1 = (5, 2, 9, 1)
tuple2 = (8, 3, 7, 4)

# Concatenating the tuples
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Sorting in ascending order
ascending_tuple = tuple(sorted(concatenated_tuple))
print("Sorted in Ascending Order:", ascending_tuple)

# Sorting in descending order
descending_tuple = tuple(sorted(concatenated_tuple, reverse=True))
print("Sorted in Descending Order:", descending_tuple)
