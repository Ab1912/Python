# Class attributes

class Student():
    name = "Abishek"
    age = 36

# Access data

print(getattr(Student,"name"))
print(getattr(Student,"age"))
print(getattr(Student,"gender","No such attribute"))

print(Student.name)


# Set data

setattr(Student,"gender","Male")
print(Student.gender)
Student.place = "Chennai"
print(Student.place)

# Delete a attribute

print(Student.__dict__)
delattr(Student,"gender")
print(Student.__dict__)
del Student.place
print(Student.__dict__)
