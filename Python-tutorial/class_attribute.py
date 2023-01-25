# 1.Class attribute

class Student():
    name = "Abishek"
    age = 36

# 2.Access data(gettr attribute, Dot notation)

print(getattr(Student,"name"))
print(getattr(Student,"age"))
print(getattr(Student,"gender","No such attribute")) # exception attribute

print(Student.name) # Dot notation
print(Student.age)

# 3.Set data in a class & print (setattr & Dot notation)

setattr(Student,"gender","Male")
print(Student.gender)
Student.place = "Chennai"

print(Student.place) # Dot notation

# 4. Delete a attribute(delattr,del)

print(Student.__dict__)
delattr(Student,"place")
print(Student.__dict__)

del Student.gender
print(Student.__dict__)