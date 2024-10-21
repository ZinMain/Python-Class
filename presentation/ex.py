# Tuple unchangeable
thistup = ("apple", "banana", "cherry", "apple", "banana", "banana")
# Accessing tuple
print(thistup[0])
# Unpacking tuple
(green, yellow, red, *rest) = thistup
print(green, yellow, red, rest)
#Methods that could be used for tuple
#Count
print("Total of bananas: ", thistup.count("banana"))
#Index
print("Total of cherry: ", thistup.index("cherry"))

# List values are changeable & dupeable
thislist = ["apple", "banana", "cherry", "apple", "banana", "banana"]
# Accessing list items
print(thislist[0])
print(thislist[1:3])
print(thislist[-1])
# Changing a list item
thislist[1] = "orange"
print("After changing a list item\n", thislist)
#Methods that could be used for list
# Appends
thislist.append("orange")
print("After append\n", thislist)
# Copy
thislist_copy = thislist.copy()
print("After copy\n", thislist_copy)
# Insert
thislist.insert(1, "orange")
print("After insert\n", thislist)
# Pop
thislist.pop(1)
print("After pop\n", thislist)
# Remove
thislist.remove("banana")
print("After remove\n", thislist)
# ETC https://www.w3schools.com/python/python_lists_methods.asp

# Dictionary changeable but not dupeable
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
another_thisdict = {
  "name": "John",
  "age": 36,
  "city": "New York"
}
# Accessing dictionary items
print(thisdict["brand"])
print(thisdict.get("model"))
# Using the 'keys' method
print("This is keys\n", thisdict.keys())
# Using the 'values' method
print("This is values\n", thisdict.values())
# Using 'Pop' / 'Popitem' method
thisdict.pop("model")
print("This is after pop\n", thisdict)
another_thisdict.popitem()
print("This is after popitem\n", another_thisdict)