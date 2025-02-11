
flag1 = 0b1100  # 12 in decimal
flag2 = 0b1010  # 10 in decimal

print(flag1, "Bitwise AND", flag2, bin(flag1 & flag2))  
print(flag1, "Bitwise OR", flag2, bin(flag1 | flag2))   
print(flag1, "Bitwise XOR", flag2, bin(flag1 ^ flag2))  
print(flag1, "Bitwise NOT", flag2, bin(~flag1))         
print(flag1, "Left Shift by 1:", bin(flag1 << 1)) 
print(flag1, "Right Shift by 1:", bin(flag1 >> 1))
