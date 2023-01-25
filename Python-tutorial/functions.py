# Functions
'''
1. No return type without Argument function
2. No return type Argument function
3. Return type without Argument function
4. Return type with Argument function
5. Arbitary Argument function
6. Keyword Argument function
7. Arbitary Keyword Argument function
8. Default parameter function
9. Passing list in a function
10.Recursive function
11. Lambda function
'''

# No return type without Argument function
def add(): # No argument passed
    a = 10
    b = 7
    c = a+b
    print("Addition : ",c) # No return type passed

add()

# 2. No return type Argument function
def sub(a,b): # Argument passed
    c = a-b
    print("Subtraction : ",c)

sub(45,21)

# 3. Return type without Argument function
def mul():
    a = 7
    b = 6
    c = a*b
    return c # return type passed

x = mul()
print("Multiplication : ",x)

# 4. Return type with Argument function
def div(a,b): # No argument passed
    c = a/b
    return c # return type passed

y = div(84,24)
print("Division : ",y)

# 5. Arbitary Argument function(*)
print("Arbitary Argument function :")
def friends(*boys):
    print(boys,type(boys))

friends("Abishek", "Kavi", "Deva", "Dinesh", "Suresh")

# 6. Keyword Argument function
print("Keyword Argument function :")
def id(name,age):
    print(name,"age is",age)

id(age=36,name="Abishek")

# 7. Arbitary Keyword Argument function(**)
def bio(**details):
    print(details,type(details))

bio(name = "Abishek",age = 36, gender = "Male")

# 8. Default parameter function
def detail(name,place="Chennai",gender="Male"):
    print(name,"|",place,"|",gender)
detail("Abishek")
detail("Deva")
detail("Kavi","Singapore")

# 9. Passing list in a function
def student(marks):
    return sum(marks)
total =  student([55,65,64,75,45])
print("Total : ",total)

# 10.Recursive function
def factorial(x):
    if x == 1:
        return 1
    else:
        return(x*factorial(x-1))
y = factorial(5)
print("Factorial of 5 is ",y)

print("lambda functions : ")
# 11. lambda function
c = lambda a : a+5
print(c(5))

c = lambda a,b : a*b
print(c(12,6))
