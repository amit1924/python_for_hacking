dictionary = {"name": "Amit", "age": "32"}


print(dictionary["name"])

dictionary["id"] = 1
print(dictionary)

for item in dictionary:
    # print(item)
    print(f"{item}:{dictionary[item]}")
