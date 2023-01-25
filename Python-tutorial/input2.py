# input statement
name = (input("Enter your Name : "))
print(name)
print("Enter the Marks :")
tam = int(input("Tamil : "))
eng = int(input("English : "))
mat = int(input("Maths : "))
sci = int(input("Science : "))
his = int(input("History : "))
geo = int(input("Geography : "))
total = tam+eng+mat+sci+his+geo
per = int(total/6)
print("Total Marks : ", total)
print("Percentage : ", per,"%")