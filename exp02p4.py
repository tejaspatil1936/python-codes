# Step 1: Define two objects
a = 5
b = 5  # Integers with the same value might have the same identity (small integer caching)

# Step 2: Identity checks
if a is b:
    print("a is b: True")
else:
    print("a is b: False")

if a is not b:
    print("a is not b: True")
else:
    print("a is not b: False")

# Step 3: Modify 'a'
a = a + 1  # Changing 'a' (now a new object 6)

# Step 4: Check identity after modification
print("After modification:")

if a is b:
    print("a is b: True")
else:
    print("a is b: False")

if a is not b:
    print("a is not b: True")
else:
    print("a is not b: False")

