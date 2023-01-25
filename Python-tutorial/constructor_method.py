# Constructor INIT method

class students:
    def __init__(self,name,rollno,age,gender) -> None: 
        self.name = name
        self.rollno = rollno
        self.age = age
        self.gender = gender
    def details(self):
        print("\nStudent Details : ")
        print("Name : ",self.name)
        print("Rollno : ",self.rollno)
        print("Age : ",self.age)
        print("Gender : ",self.gender)

stud1 = students("Abishek",101,36,"Male")
stud1.details()
stud2 = students("Deva",102,34,"Male")
stud2.details()
stud3 = students("Kavi",103,37,"Male")
stud3.details()