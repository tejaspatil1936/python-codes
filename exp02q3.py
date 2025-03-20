nested_list = [(1, 2, 3), [4, 5, 6], {7, 8, 9}]
target = 7

for item in nested_list:
    if target in item:  # Directly check if target exists in the item
        print(True)
        break
else:
        print(False)
