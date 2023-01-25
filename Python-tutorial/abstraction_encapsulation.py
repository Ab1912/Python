# Abstraction and Encapsulation in Python
# Student (list,Add,Remove)


class student:

  def __init__(self, names):
    self.names = names

  def list_names(self):
    for list_names in self.names:
      print(list_names)

  def add_names(self, add_names):
    if add_names in self.names:
      print("Student already Added")
    else:
      self.names.append(add_names)
      print("Student Added")

  def remove_names(self, remove_names):
    if remove_names in self.names:
      self.names.remove(remove_names)
      print("Student Removed")
    else:
      print("Student not found")


name_list = ["Kavi", "Deva", "Suresh"]
obj = student(name_list)
msg = '''
1. List Students 
2. Add Student
3. Remove Student
4. Exit \n'''

while True:
  print(msg)
  choice = int(input("Enter your Choice : "))
  if choice == 1:
    print("Student List : \n")
    obj.list_names()
    
  elif choice == 2:
    nam = str(input("Enter Student name : "))
    nam1 = nam.title()
    obj.add_names(nam1)
    
  elif choice == 3:
    nam = str(input("Enter Student name : "))
    nam1 = nam.title()
    obj.remove_names(nam1)

  elif choice == 4:
    print("Thank you!!!")
    quit()

  else:
    print("Invalid option, please try again")