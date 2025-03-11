# Python program to find the maximum and minimum elements in a list


def find_max_min(lst):

    return max(lst), min(lst)


# Example usage
lst = [3, 1, 7, 9, 2, 5]
maximum, minimum = find_max_min(lst)

print("Maximum Element:", maximum)
print("Minimum Element:", minimum)
