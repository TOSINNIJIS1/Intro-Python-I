"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1], 'first code')

# Output the second-to-last element: 9
print(a[4], 'second code')

# Output the last three elements in the array: [7, 9, 6]
print(a[3:], 'third code')

# Output the two middle elements in the array: [1, 7]
print(a[2:4], 'fourth code')

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:], 'fifth code')

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:5], 'sixth code')

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[-6:-1], 'seventh code')
print(s[7:12], 'seventh code')