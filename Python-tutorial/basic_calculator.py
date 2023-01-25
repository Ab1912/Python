# Basic calculator
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Numder : "))
print("Select Your Operation : ")
print("1. Addition ")
print("2. Substraction ")
print("3. Multiplication ")
print("4. Division ")
choice = input("Enter your choice : 1|2|3|4 : ")

if choice == "1":
        print(num1,"+",num2,"=",add(num1,num2))

if choice == "2":
        print(num1,"-",num2,"=",sub(num1,num2))

if choice == "3":
        print(num1,"*",num2,"=",mul(num1,num2))

if choice == "4":
        print(num1,"/",num2,"=",div(num1,num2))
elif choice == "0" or choice >= "5" :
        print("Invalid input")