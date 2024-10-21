# Tuple unchangeable
thistup = ("apple", "banana", "cherry", "apple", "banana", "banana")
#Methods that could be used for tuple
#Count
print(thistup.count("banana"))
#Index
print(thistup.index("cherry"))

# List values are changeable & dupeable
thislist = ["apple", "banana", "cherry", "apple", "banana", "banana"]
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