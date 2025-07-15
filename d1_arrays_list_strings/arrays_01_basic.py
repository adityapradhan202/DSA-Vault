# Complexities of basic array operations

# Append - Insert element at end of array
# On average: O(1), but sometimes O(n)
# Why O(n) sometimes? Google it, or see notes.

A = [1, 2, 3]
A.append(5)
print("Output-1:")
print(A)

# Pop - Deleting element at the end of array - O(1)
print("Output-2:")
A.pop()
print(A)

# Insert (not at end of array) - O(n)
A.insert(2, 100)
print("Output-3:")
print(A)

# Modify an element - O(1)
A[2] = 99
print("Output-4:")
print(A)

# Accessing element given at index i - O(1)
print("Output-5:")
print(A[2])

# Checking if array has an element - O(n)
print("Output-6:")
if 7 in A:
    print(True)
else:
    print(False)

# Append to end of string - O(n)
s = "hello"
b = s + 'z'
print("Output-7:")
print(b)

# Check if something is in the string - O(n)
print("Output-8:")
if "e" in s:
    print(True)

# We also have len function in python
# We can find out the length of a sequential data type by using len function

# It should be O(n)
# But in python it is O(1)\
# Length is already stored as an property that can be looked up
# And this thing is same with the strings -O(1)
print("Output-9:")
print(len(A))

# Note-
# Make sure to revise oops before going further!
