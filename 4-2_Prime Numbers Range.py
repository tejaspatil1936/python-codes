a, b = map(int, input("Enter range (a b): ").split())
while a <= b:
    if all(a % i != 0 for i in range(2, int(a**0.5) + 1)) and a > 1:
        print(a, end=' ')
    a += 1
print()
