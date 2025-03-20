def reverse_list_methods(lst):
   
    method1 = lst[:]
    method1.reverse()
    
    method2 = lst[::-1]
    
    method3 = list(reversed(lst))
    
    return method1, method2, method3

lst = [1, 2, 3, 4, 5]
rev1, rev2, rev3 = reverse_list_methods(lst)

print("Original List:", lst)
print("Reversed using reverse():", rev1)
print("Reversed using slicing:", rev2)
print("Reversed using reversed():", rev3)
