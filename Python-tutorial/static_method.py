# Static Method

class student:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def pout(self):
        print("Name : ",self.name,"Age : ",self.age)

    @staticmethod
    def welcome():
        print("Welcome to our institution")

obj = student("Karthik",19)
obj.pout()
obj.welcome()

obj = student("Harish : ",20)
obj.pout()
obj.welcome()