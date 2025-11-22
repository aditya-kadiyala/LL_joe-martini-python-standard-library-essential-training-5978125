# The array type can hold homogeneous data types and operate
# on them more efficiently while using less memory

# use when you need uniform data

from array import array

# TODO: Create an array of integer numbers
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

arr1 = array('i', arr)
print("Typecode of Array 1 is ", arr1.typecode)
print("Itemsize in Array 1 is ", arr1.itemsize)

# TODO: Add additional items to the array
arr1.insert(0, 0)
arr1.append(22)
arr1.extend([24, 25, 26])
print(arr1)

# TODO: iterate over the array content like any other list

for i, item in enumerate(arr1):
  arr1[i]*=2
print(arr1)

# TODO: Try to add a non-integer number to the array
# arr1.insert(0, 1.0)

# TODO: Create an array to hold bytes instead of ints
arr2 = array('B', [18, 102, 182, 56, 89, 5, 254, 32, 64, 50])
print(arr2.typecode)
print(arr2.itemsize)

arr3 = array('Q', [12345678901234567890])  # Allowed
# arr3 = array('Q', [123456789012345678901]) # overflows
print(arr3.typecode)
print(arr3.itemsize)

# TODO: try to add an item that's out of range 
# arr2.append(256)

# TODO: Convert an array to a list
list1 = arr2.tolist()
print(list1)
print(type(arr2))
print(type(list1))


# 500 ??
# Great question — and no, you cannot store the value 500 in an array of type 'B' because:

# 'B' stores unsigned bytes

# Range = 0 to 255

# So you need the next appropriate type code that can hold 500.

# ✅ Which type should you use for max value = 500?

# The smallest array type that can store 500 is:

# ✔ 'H' → Unsigned short (2 bytes)

# Range: 0 to 65535

# Enough to store 500 efficiently (only 2 bytes)

# Example:

# from array import array

# arr = array('H', [100, 200, 500])
# print(arr)


# Output:

# array('H', [100, 200, 500])

# ❓ Can Python arrays automatically enforce a max of 500?

# ❌ No, Python’s array does NOT support custom max-value limits.
# It only enforces limits based on type code, not a user-defined range.

# But you can enforce it manually:

# ✔ Option 1: Validate before inserting
# MAX_VALUE = 500

# def safe_append(arr, value):
#     if value > MAX_VALUE:
#         raise ValueError(f"Value {value} exceeds max allowed {MAX_VALUE}")
#     arr.append(value)

# arr = array('H')
# safe_append(arr, 300)
# safe_append(arr, 500)
# safe_append(arr, 600)  # raises error

# ✔ Option 2: Create a wrapper class

# You can wrap array('H') inside your own class with validation logic.
