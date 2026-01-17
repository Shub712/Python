# Duplication not allowed but it overwrites the last key

Information = {"Name" : "Rahul","Age" : 25, "City": "Pune", "Marks": 89.90, "City" : "Mumbai"} 

print(Information)

print(Information["City"])

Information["Age"] = 26     # Mutable
print(Information)

