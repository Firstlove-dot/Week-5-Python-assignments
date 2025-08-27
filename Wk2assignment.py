"""
This program demonstrates basic list operations such as append, insert,
extend, remove, sort, and finding an index.
"""

# Create an empty list
my_list = []

# # Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# # Insert 15 at the second position (index 1) 0---n-1 0-(4-1) 3
my_list.insert(1, 15)

# # Extend the list with another list
my_list.extend([50, 60, 70])

# # Remove the last element
my_list.pop()

# # Sort the list in ascending order
my_list.sort()

# # Find the index of the value 30
index_of_30 = my_list.index(30)

# print(index_of_30)

# # Print the final list and the index of 30
print("Final List:", my_list)
print("Index of 30:", index_of_30)

# print(my_list)