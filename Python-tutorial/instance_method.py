# Instance Method
class Student:
  name = "Akash"
  std = 10

  def details():
    print("Name : ", Student.name)
    print("class : ",Student.std)


Student.details()
o = Student()
print(o.name)