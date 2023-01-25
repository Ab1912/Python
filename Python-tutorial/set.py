# Set
print("Set in Python")
a = {"abi", "kavi","deva"}
print(a," type is : ",type(a))
print("Using for loop in set")
for b in a:
    print(a)
print("To add a element in a set")
a.add("suresh") # to add a element to set
print(a)
print("To update 2 sets")
b = {1,2,3,4,5}
a.update(b) # to update to 2 sets
print(a)
print("To remeove a element")
a.remove("deva") # to remove a value
print(a)
print("To discard a element")
a.discard("deva") # to remove a value if value is not found program will continue
print(a)
print("To remove a random element")
a.pop() # to remove a random value
print(a)
print("To clear a set")
a.clear() # to clear values in a set
print(a)
print("To delete a set")
del a # to delete a set
print("Python ignores duplicate elements in a set")
a = {1,2,3,4,5,3} # ignores duplicate elements
print(a)
print("To update 2 sets")
a = {1,2,3,4,5}
b = {6,7,8,9,4}
print(a,b)
c = a.union(b) # adding of 2 sets using 3rd set
print(c)
a.update(b) # adding of 2 sets
print(a)
print("To find intersection elements of 2 sets")
a = {11,12,13,14,15}
b = {16,17,18,19,14}
c = a.intersection(b) # intersection of 2 sets using 3rd set
print(c)
a.intersection_update(b) # intersection of 2 sets
print(a)
print("To find different elements in a set")
a = {21,22,23,24,25}
b = {26,27,28,29,24}
print(a,b)
c = a.symmetric_difference(b) # intersectionof 2 sets
print(c)
a.symmetric_difference_update(b)
print(a)
print("To find wheather sets are disjointed")
a = {21,22,23,24,25}
b = {26,27,28,29,20}
c = a.isdisjoint(b) # to find wheather sets are disjointed
print(c)
print("To find wheather a is subset of b")
a = {"a","b","c"}
b = {"a", "b", "c", "d", "e", "f"}
print(a,b)
c = a.issubset(b) # to find wheather a is subset of b
print(c)
print("To find wheather a is superset of b")
c = a.issuperset(b) # to find wheather a is superset of b
print(c)