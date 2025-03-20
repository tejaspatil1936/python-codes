# List of elements
lst = [3, 1, 7, 9, 2, 5, 3, 7, 1, 3]

# Using count() function
freq_with_count = {x: lst.count(x) for x in set(lst)}

# Without using count() function
freq_without_count = {}
for num in lst:
    freq_without_count[num] = freq_without_count.get(num, 0) + 1

# Output results
print("Frequency using count():", freq_with_count)
print("Frequency without using count():", freq_without_count)
