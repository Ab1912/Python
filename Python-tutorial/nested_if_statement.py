# Nested IF statement

print("Program to find the student's mark details & grade : ")

"""
if pass grade

90 to 100 - Outstanding
80 to 89  - Excellent
70 to 79  - Very Good
60 to 69  - Good
50 to 59  - Average
35 to 46  - Poor

"""

name = input('Enter the name of the student : ')
lang1 = int(input('Enter language-1 marks : '))
lang2 = int(input('Enter language-2 marks : '))
mat = int(input('Enter maths marks : '))
sci = int(input('Enter science marks : '))
s_sci = int(input('Enter social science marks : '))
total = int(lang1 + lang2 + mat + sci + s_sci)
avg = int(total/5)

print("Student Name : ",name)
print("Total :  ",total,"/ 500")
print('Average : ',avg)

if (lang1 >=35 and lang2 >= 35 and mat >= 35 and sci >=35 and s_sci >=35):
    print("Result :  Pass")
    if (avg >=90 and avg <= 100):
        print("Grade : Outstanding")
    elif(avg >=90 and avg <= 100):
        print("Grade : Outstanding")
    elif(avg >=80 and avg <= 89):
        print("Grade : Excellent")       
    elif(avg >=70 and avg <= 79):
        print("Grade : Very Good")
    elif(avg >=60 and avg <= 69):
        print("Grade : Good")
    elif(avg >=50 and avg <= 59):
        print("Grade : Average")
    else:
        print("Grade : Poor")            
else:
    print("Result : Fail")
    print("No Grade")