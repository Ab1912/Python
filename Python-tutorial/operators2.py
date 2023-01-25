# Identity operators(# is & is not)
# 

a = [1,2,3]
b = [1,2,3]
c = a

print("Identity operators : ")
# Equal to
print(a is b) # Is operator checks identity of the object(a,b,c)
print(a is c) 
print(a == b) # == operator checks identity of the values in object
print("--------------")
# Not Equal to
print(a is not b)
print(a is not c)
print(a != b,"\n")

# Membership operators(in & not in)
print("Membership operators : ")
a = [1,2,3,4,5,6]
print(7 in a)
print(7 not in a)
