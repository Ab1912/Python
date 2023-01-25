# tuple_function
a = (1,2.5,True,"abi")
print(a)
print(type(a))
print(a[0])
print(a[-1])
print(a[1:3])
print(a[:2])
print(a[1:])
b = list(a)
print(b)
print(type(b))
b.append("akash")
print(b)
a = tuple(b)
print(a)
print(type(a))
print("-------------")

for i in a:
    print(i,end=",")
print("\n")
if "abi" in a:
    print("abi is found")
else:
    print("abi not found")
print(len(a))
a =(1,) # for a single value comma is necessary for defining as tuple
print(type(a))
del a # to delete a tuple
a = (1,5,7,8,9)
b = (2,3,5,7,10)
c = a + b # to concatenate a tuple
print(c)
print(c.count(5))

# Nested tuple
a = (1,5,7,8,9)
b = (2,3,5,7,10)
c = (a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][3]) # to print individual value of 1st nested tuple 
print(c[1][2]) # to print individual value of 2nd nested tuple
x = ("abi,")*5
print(x)
print(min(a))
print(max(a))