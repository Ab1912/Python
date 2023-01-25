# Function overriding(Overriding already defined function)

class Employee():

    def workinghrs(self):
        self.workinghrs = 65

    def printhrs(self):
        print("Total Working hours : ",self.workinghrs)

class Trainee(Employee):

    def workinghrs(self):
        self.workinghrs = 50

    def resethrs(self):
        self.workinghrs = 60

emp = Employee()
emp.workinghrs()
emp.printhrs()

trn = Trainee()
trn.workinghrs()
trn.printhrs()

trn.resethrs()
trn.printhrs()



