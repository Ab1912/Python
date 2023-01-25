# IF statement
# Program to check Even number

a = int(input('Enter the number to find Even of Odd number :'))
print("Enter the Number : ")
if a % 2 == 0:
    print(a,' is a Even number')
else:
     print(a,' is a Odd number\n')

# Program to check Voting eligibility

name = input('Enter your Name : ')
age = int(input('Enter your Age : '))

if age >= 18:
    print(name,' aged ',age, ' is eligible for voting')
else:
    print(name,' aged ',age, ' is not eligible for voting')

# Program for Else if statement
# Library charges

name = input('Enter the Name : ')
days = int(input('Enter the due days : '))

    
if (days == 0):
    print('No fine for  ', name)

elif (days >=1) and (days <=5) :
    print('Rs.50 fine  ', name)

elif (days >=6) and (days <=15) :
    print('Rs.150 fine for  ', name)    

elif (days >=16) and (days <=30) :
    print('Rs.150 fine for  ', name)  

else :
    print('Membership cancelled for  ', name)
          

        
