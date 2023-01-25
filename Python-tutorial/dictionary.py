# Dictionary

# Creating a dictionary
abi = {
    "name" : "abishek",
    "age" : 36,
    "place" : "madambakkam"
} 
print(abi) 
print(type(abi)) 
print("----------------")

# Printing elements by calling keys
print(abi["name"])
print(abi["age"])
print(abi["place"])
print("----------------")
# Print elements by using get function
print(abi.get("name"))
print(abi.get("age"))
print(abi.get("place"))
print("----------------")
# Printing elements using values, key , items functions
print(abi.values())
print(abi.keys())
print(abi.items())
print("----------------")

# Dictionary using for loop
for m in abi:
    print(m,abi[m])
# Dictionary for loop using values, key, items functions
for m in abi.get("name"):
    print(m,end="")
print("\n")
for m in abi.values():
    print(m)
print("\n")
for m in abi.keys():
    print(m)
print("\n")
for m in abi.items():
    print(m)
print("----------------")
# if condition in dictionary
print("if condition in dictionary : ")
if "name" in abi:
    print("correct")
else:
    print("Incorrect")
print("----------------")
#Changing values in dictionary
print("Changing values in dictionary")
abi.update({"gender":"Male"})
print("Dictionary updated : \n",abi)
abi["place"] = "Chennai"
print("Value changed : \n",abi)
abi.pop("age")
print("Item has been removed : \n",abi)
abi.clear()
print("Dictionary cleared : ",abi)
del abi # Dictionary deleted
print("----------------")

#Creating a nested dictionary
friends = {
        "abi" : {
            "name" : "Abishek",
            "age" : 36,
            "place" : "Madambakkam",
    },
        "kavi" : {
            "name" : "Kavi Pandian",
            "age" : 37,
            "place" : "Singapore"
    },
        "deva" : {
            "name" : "Devasenan",
            "age"  : 34,
            "place" : "Ekkattuthangal",
        },
}
print(friends)
#Changing values in dictionary
friends["abi"].update({"job":"karate"})
print("Updated nested dictionary : \n",friends["abi"])
friends["kavi"]["place"] = "Chennai"
print("Changed nested dictionary : \n",friends["kavi"])
friends["deva"].pop("age")
print("Removed item in a nested dictionary : \n",friends["deva"])
friends["deva"].clear()
print("cleared a nested dictionary : \n",friends)
del friends["deva"]
print("deleted a nested dictionary : \n",friends)
