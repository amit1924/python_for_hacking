my_list = [9, 8, 5, 7, 0, 4, 6, 5, 10, 55, 47, 78, 5]

# Iterate
for item in my_list:
    print(item)


# Select any item with index
print(my_list[0])

# Add any item in list
my_list.append(90)
print(my_list)

# Copy list into another list
new_list = my_list.copy()
print(new_list)

# Count how many times element repeated in list
print(my_list.count(5))

# Add another list in the end of the list
my_list.extend([80, 160, 240])
print(my_list)


# Inserts an element at the specified index.
my_list.insert(0, 900)
print(my_list)

# Removes and returns the element at the specified index. If no index is provided, removes and returns the last element.

my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)


# Removes the first occurrence of a value from the list.
my_list.remove(160)
print(my_list)

# ascending order
my_list.sort()
print(my_list)


# reverse order
my_list.reverse()
print(my_list)


# Clear all elements from the list

my_list.clear()
print(my_list)
