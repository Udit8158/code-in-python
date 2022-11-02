dict = {
    "name": "Udit",
    "age": 18,
    "language": ["C", "Python", "JS"]
}

# Append item on the list of dictionary
dict["language"].append("Solidity")
dict["age"] = 19  # update
print(dict["language"], dict["age"])

# Adding new item in dict
dict["ground"] = "MCG"
print(dict)

# Accessing keys and values of dict
# keys = dict.keys()
# values = dict.values()
# print("name" in keys)

# for i in keys:
#     print(i)

# for v in values:
#     print(v)
