dictionary = {
    "name": "Amit",
    "age": "32",
    "city": "Patna",
    "country": "India",
    "email": "amit@test.com",
}

print(dictionary["name"])

print(f"Convert into tuples:{dictionary.items()}")

# Iterating
for item in dictionary:
    print(item, dictionary[item])


# convert dictionary into tuples dictionary.items()
for key, value in dictionary.items():
    print(f"{key}:{value}")

for idx, (key, value) in enumerate(dictionary.items()):
    print(f"{idx}:{key}:{value}")

# Adding new key-value pairs to dictionary
dictionary["color"] = "blue"
print(dictionary)

# Change value
dictionary["name"] = "Arsh"
print(dictionary)

# Delete key-value pairs from dictionary
del dictionary["color"]
print(dictionary)

# Clear all key-value pairs from dictionary
# dictionary.clear()
# print(dictionary)

# copy
dict = dictionary.copy()
print(f"Copying dictionary:{dict}")

# Get all key-value pairs from dictionary
print(f"get name : {dictionary.get('name')}")

# Display only keys
print(dictionary.keys())

# Remove specified key
print(dictionary.pop("name"))

# Remove last key-value pairs from dictionary
print(dictionary.popitem())
