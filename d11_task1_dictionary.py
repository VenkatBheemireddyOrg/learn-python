my_dict = {"name": "Ram", "age": 25, "city": "hyderabad"}

# Accessing dictionary
print(my_dict["name"])

# Modifying dictionary
my_dict["age"] = 28
print(my_dict["age"])

# Adding into dictionary
my_dict["occupation"] = "engineer"
print(my_dict["occupation"])

# Deleting from dictionary
del my_dict["city"]
if "city" in my_dict:
    print(my_dict["city"])
else:
    print("city is not present in my_dict")

for key,value in my_dict.items():
    print(key,value)
