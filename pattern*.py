# *
# **
# ***
# ****
# *****

# num = int(input("Enter the number : "))
# for i in range(1, num+1):
#     for j in range(i):
#         print('*', end='')
#     print()

###########################

#    *
#   * *
#  * * *
# * * * *

# num = int(input("Enter the number : "))

# for i in range(1, num):
#     for j in range(1, num - i):
#         print(" ", end='')
#     for k in range(1, i+1):
#         print('* ', end='')
#     print()

###########################

#     *
#    **
#   ***
#  ****
# *****

# num = int(input("Enter the number : "))

# for i in range(1, num):
#     for j in range(1, num - i):
#         print(" ", end='')
#     for k in range(1, i+1):
#         print('*', end='')
#     print()

###########################

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# num = int(input("Enter the number : "))

# for i in range(num, 0, -1):
#     for j in range(1, num-i+1):
#         print(" ", end='')
#     for k in range(1, i+1):
#         print("* ", end='')
#     print()

# num = int(input("Enter the number: "))

# for i in range(num, 0, -1):
#     print(" " * (num - i) + "* " * i)
